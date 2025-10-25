import os
from dotenv import load_dotenv, find_dotenv
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunContextWrapper,
    set_tracing_disabled,
    input_guardrail,
    output_guardrail,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered,
    TResponseInputItem,
)
from pydantic import BaseModel

_: bool = load_dotenv(find_dotenv())
set_tracing_disabled(True)

gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")

# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# 2. Which LLM Model?
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", openai_client=external_client
)


class MathHomeworkOutput(BaseModel):
    is_math_homework: bool
    reasoning: str


guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking you to do their math homework.",
    output_type=MathHomeworkOutput,
    model=llm_model,
)


@input_guardrail
async def math_guardrail(
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math_homework,
    )


class WeatherSanitizer(BaseModel):
    weather_related: bool
    reason: str | None = None


weather_sanitizer = Agent(
    name="WeatherSanitizer",
    instructions="Check if the output is related to weather.",
    model=llm_model,
    output_type=WeatherSanitizer,
)


@output_guardrail
async def weather_guardrails(
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(weather_sanitizer, input, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.weather_related,
    )



base_agent: Agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful assistant.",
    model=llm_model,
    input_guardrails=[math_guardrail],
    output_guardrails=[weather_guardrails],
)

try:
    # res = Runner.run_sync(
    #     base_agent, [{"role": "user", "content": "What's 1 + 1?"}]
    # )
    # res = Runner.run_sync(
    #     base_agent, [{"role": "user", "content": "What's the weather like in SF?"}]
    # )
    res = Runner.run_sync(
        base_agent, [{"role": "user", "content": "What is AI?"}]
    )
    print("[OUTPUT]", res.final_output)
except InputGuardrailTripwireTriggered:
    print("Alert: Guardrail input tripwire was triggered!")
except OutputGuardrailTripwireTriggered:
    print("Alert: Guardrail output tripwire was triggered!")
