import os
from dotenv import load_dotenv, find_dotenv
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunContextWrapper,
    set_tracing_disabled,
    output_guardrail,
    GuardrailFunctionOutput,
    OutputGuardrailTripwireTriggered,
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


class MessageOutput(BaseModel):
    response: str


class MathOutput(BaseModel):
    is_not_math: bool
    reasoning: str


guardrail_agent2 = Agent(
    name="Guardrail check",
    instructions="Check if the output does not include any math.",
    output_type=MathOutput,
    model=llm_model,
)


@output_guardrail
async def math_guardrail2(
    ctx: RunContextWrapper, agent: Agent, output: MessageOutput
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent2, output.response, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_not_math,
    )

agent2 = Agent(
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    output_guardrails=[math_guardrail2],
    output_type=MessageOutput,
    model=llm_model,
)

try:
    # result = Runner.run_sync(agent2, "Hello, can you help me solve for x: 2x + 3 = 11?")
    result = Runner.run_sync(agent2, "How can i return my product?")
    print(result.final_output)
except OutputGuardrailTripwireTriggered:
    print("Math homework guardrail tripped")
