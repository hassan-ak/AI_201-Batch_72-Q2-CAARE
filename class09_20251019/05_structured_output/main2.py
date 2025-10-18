import os
import asyncio
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    set_tracing_disabled,
)
from pydantic import BaseModel
from rich import print
from typing import Optional, List

# 🌿 Load environment variables
load_dotenv()
set_tracing_disabled(disabled=True)

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

# 🔐 Setup Gemini client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

external_client = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=BASE_URL)
llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", openai_client=external_client
)


class ProductInfo(BaseModel):
    name: str  # Text
    price: float  # Decimal number
    in_stock: bool  # True/False
    categories: List[str]  # List of text items
    discount_percent: Optional[int] = 0  # Optional number, default 0
    reviews_count: int  # Whole number


# Create agent with structured output
agent = Agent(
    name="ProductExtractor",
    instructions="Extract product information from product descriptions.",
    output_type=ProductInfo,
    model=llm_model,
)


async def main():
    result = await Runner.run(
        agent,
        "The iPhone 15 Pro costs $999.99, it's available in electronics and smartphones categories, currently in stock with 1,247 reviews.",
    )

    # Now you get perfect structured data!
    print("Type:", type(result.final_output))  # <class 'PersonInfo'>
    print(
        "Output:", result.final_output
    )  # ProductInfo(name='iPhone 15 Pro', price=999.99, in_stock=True, categories=['electronics', 'smartphones'], discount_percent=0, reviews_count=1247)
    # print("Name:", result.final_output.name)         # "iPhone 15 Pro"
    # print("Price:", result.final_output.price)      # 999.99
    # print("In Stock:", result.final_output.in_stock) # True
    # print("Categories:", result.final_output.categories) # ['electronics', 'smartphones']
    # print("Discount:", result.final_output.discount_percent) # 0
    # print("Reviews:", result.final_output.reviews_count)   # 1247


if __name__ == "__main__":
    asyncio.run(main())
