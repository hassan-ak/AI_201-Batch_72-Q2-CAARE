# Getting started with Chainlit

1. Create a uc project `uv init chatbot`
2. Naviagte to the newly created project directory `cd chatbot`
3. Install chainlit in the application `uv add chainlit`
4. Run chainlit hello code `uv run chainlit hello`
5. Create `main.py`

   ```py
   import chainlit as cl

   @cl.on_message
   async def main(message: cl.Message):
      print(f"User sent a message: {message.content}")
   ```

6. Run the file `uv run chainlit run main.py -w`
