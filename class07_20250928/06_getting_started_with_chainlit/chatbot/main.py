import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    print(f"User sent a message: {message.content}")