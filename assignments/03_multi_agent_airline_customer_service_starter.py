"""
Multi-Agent Airline Customer Service System - Starter Code

Fill in the missing implementations following the assignment instructions.
"""

from __future__ import annotations as _annotations

import asyncio
import random
import uuid

from pydantic import BaseModel

from agents import (
    Agent,
    HandoffOutputItem,
    ItemHelpers,
    MessageOutputItem,
    RunContextWrapper,
    Runner,
    ToolCallItem,
    ToolCallOutputItem,
    TResponseInputItem,
    function_tool,
    handoff,
    trace,
)
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

# TODO: Implement the AirlineAgentContext Pydantic model
# Requirements:
# - Inherit from BaseModel
# - Add passenger_name: str | None = None
# - Add confirmation_number: str | None = None
# - Add seat_number: str | None = None
# - Add flight_number: str | None = None


class AirlineAgentContext(BaseModel):
    # TODO: Implement this context model
    pass


# TODO: Implement the FAQ lookup tool
# Requirements:
# - Use @function_tool decorator with name_override and description_override
# - Check for keywords: "bag", "baggage", "luggage", "carry-on", "seat", "wifi", etc.
# - Return appropriate responses for each category
# - Return fallback message for unknown topics


@function_tool(
    name_override="faq_lookup_tool", description_override="Lookup frequently asked questions."
)
async def faq_lookup_tool(question: str) -> str:
    # TODO: Implement the FAQ lookup logic
    # Hint: Use question.lower() to make it case-insensitive
    # Check for keyword categories and return appropriate responses
    pass


# TODO: Implement the update_seat tool
# Requirements:
# - Use @function_tool decorator
# - Accept context, confirmation_number, and new_seat parameters
# - Update context.context.confirmation_number and context.context.seat_number
# - Assert that flight_number exists
# - Return a confirmation message


@function_tool
async def update_seat(
    context: RunContextWrapper[AirlineAgentContext], confirmation_number: str, new_seat: str
) -> str:
    """
    Update the seat for a given confirmation number.

    Args:
        context: The run context containing shared state
        confirmation_number: The confirmation number for the flight
        new_seat: The new seat to update to
    """
    # TODO: Implement the seat update logic
    pass


# TODO: Implement the on_seat_booking_handoff hook
# Requirements:
# - Accept RunContextWrapper[AirlineAgentContext] as parameter
# - Generate a random flight number (format: "FLT-XXX" where XXX is 100-999)
# - Update context.context.flight_number
# - Return None


async def on_seat_booking_handoff(context: RunContextWrapper[AirlineAgentContext]) -> None:
    # TODO: Implement the handoff hook
    pass


# TODO: Implement the FAQ Agent
# Requirements:
# - Name: "FAQ Agent"
# - Appropriate handoff_description
# - Instructions that include RECOMMENDED_PROMPT_PREFIX
# - Add the FAQ lookup tool to tools list
# - Add Triage Agent to handoffs list

faq_agent = Agent[AirlineAgentContext](
    name="FAQ Agent",
    # TODO: Add handoff_description
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    # TODO: Write instructions for the FAQ agent
    # Include a routine for answering questions using the FAQ tool
    """,
    tools=[],  # TODO: Add faq_lookup_tool
    handoffs=[],  # TODO: Add triage_agent
)

# TODO: Implement the Seat Booking Agent
# Requirements:
# - Name: "Seat Booking Agent"
# - Appropriate handoff_description
# - Instructions that include RECOMMENDED_PROMPT_PREFIX
# - Add the update_seat tool to tools list
# - Add Triage Agent to handoffs list
# - Connect to the on_seat_booking_handoff hook using handoff()

seat_booking_agent = Agent[AirlineAgentContext](
    name="Seat Booking Agent",
    # TODO: Add handoff_description
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    # TODO: Write instructions for the seat booking agent
    # Include a routine for collecting confirmation number and desired seat
    """,
    tools=[],  # TODO: Add update_seat tool
    handoffs=[],  # TODO: Add handoff with on_seat_booking_handoff hook
)

# TODO: Implement the Triage Agent
# Requirements:
# - Name: "Triage Agent"
# - Appropriate handoff_description
# - Instructions that include RECOMMENDED_PROMPT_PREFIX
# - No tools
# - Handoffs to FAQ Agent and Seat Booking Agent (with hook)

triage_agent = Agent[AirlineAgentContext](
    name="Triage Agent",
    # TODO: Add handoff_description
    instructions=(
        f"{RECOMMENDED_PROMPT_PREFIX} "
        # TODO: Complete the instructions
    ),
    tools=[],  # Triage agent has no tools
    handoffs=[],  # TODO: Add faq_agent and seat_booking_agent with handoff hook
)

# Setup bidirectional handoffs
faq_agent.handoffs.append(triage_agent)
seat_booking_agent.handoffs.append(triage_agent)


async def main():
    """
    Main function to run the interactive loop.
    
    TODO: Implement the main loop that:
    1. Starts with triage_agent
    2. Maintains input_items list
    3. Creates AirlineAgentContext instance
    4. Generates conversation_id
    5. Loops while True:
       - Gets user input
       - Wraps in trace()
       - Runs agent with Runner.run()
       - Displays all output items
       - Updates current_agent and input_items
    """
    current_agent: Agent[AirlineAgentContext] = triage_agent
    input_items: list[TResponseInputItem] = []
    context = AirlineAgentContext()

    # TODO: Generate a conversation ID using uuid
    conversation_id = "TODO"

    while True:
        # TODO: Get user input
        user_input = input("Enter your message: ")
        
        # TODO: Wrap in trace() with group_id
        with trace("Customer service", group_id=conversation_id):
            # TODO: Add input to input_items
            # TODO: Run the agent
            result = "TODO"

            # TODO: Display output items
            for new_item in result.new_items:
                agent_name = new_item.agent.name
                if isinstance(new_item, MessageOutputItem):
                    print(f"{agent_name}: {ItemHelpers.text_message_output(new_item)}")
                elif isinstance(new_item, HandoffOutputItem):
                    # TODO: Display handoff information
                    pass
                elif isinstance(new_item, ToolCallItem):
                    # TODO: Display tool call information
                    pass
                elif isinstance(new_item, ToolCallOutputItem):
                    # TODO: Display tool output
                    pass
                else:
                    print(f"{agent_name}: Skipping item: {new_item.__class__.__name__}")
            
            # TODO: Update input_items and current_agent
            input_items = "TODO"
            current_agent = "TODO"


if __name__ == "__main__":
    asyncio.run(main())

