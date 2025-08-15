from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, OpenAIChatCompletionsModel, set_tracing_disabled

api_key = "your_api_key"
model="gemini-2.5-flash-lite"

external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key,
)
set_default_openai_client(external_client)

llm_model = OpenAIChatCompletionsModel(
    model=model,
    openai_client=external_client,
)

set_tracing_disabled(True)

agent = Agent(
    name="simple_agent",
    instructions="You are a helpful assistant, specialized in providing single line response.",
    model=llm_model
)

def run_agent():
    response = Runner.run_sync(agent, "What is GenAI?")
    print(response.final_output)