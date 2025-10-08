import chainlit as cl
from rich import print
from agent.main import create_main_agent
from agents import Runner, Agent
from agents.stream_events import (
    RawResponsesStreamEvent,
    RunItemStreamEvent,
    AgentUpdatedStreamEvent,
)
from typing import cast
from openai.types.responses import ResponseTextDeltaEvent

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Morning routine ideation",
            message="Can you help me create a personalized morning routine that would help increase my productivity throughout the day? Start by asking me about my current habits and what activities energize me in the morning.",
            icon="/public/logo.svg",
        ),

        cl.Starter(
            label="Explain superconductors",
            message="Explain superconductors like I'm five years old.",
            icon="/public/logo.svg",
        ),
        cl.Starter(
            label="Python script for daily email reports",
            message="Write a script to automate sending daily email reports in Python, and walk me through how I would set it up.",
            icon="/public/logo.svg",
            command="code",
        ),
        cl.Starter(
            label="Text inviting friend to wedding",
            message="Write a text asking a friend to be my plus-one at a wedding next month. I want to keep it super short and casual, and offer an out.",
            icon="/public/logo.svg",
        )
    ]
    
@cl.on_chat_start
async def on_chat_start():
    agent = create_main_agent()

    cl.user_session.set("agent", agent)

    cl.user_session.set("message_history", [])


@cl.on_message
async def on_msg(message: cl.Message):

    msg = cl.Message(content="Thinking...")

    await msg.send()

    try:
        agent = cast(Agent, cl.user_session.get("agent"))

        message_history = cl.user_session.get("message_history", [])

        message_history.append({"role": "user", "content": message.content})

        # Run in streaming mode and update the message incrementally
        result = Runner.run_streamed(agent, message_history)

        async for event in result.stream_events():

            if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
            ):

                if msg.content == "Thinking...":
                    msg.content = ""

                await msg.stream_token(event.data.delta)

        # When streaming completes, ensure final_output (if provided) is shown and save history
        if result.final_output is not None:
            msg.content = result.final_output
            await msg.update()

        cl.user_session.set("message_history", result.to_input_list())

    except Exception as e:
        msg.content = f"There is an error while processing your request. Please review the following before trying again. \n\n Error: {e}"
        await msg.update()
