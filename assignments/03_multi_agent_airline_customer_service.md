# Multi-Agent Airline Customer Service System

## 📋 Problem Statement

Build an intelligent customer service system for an airline that uses multiple AI agents to handle different types of customer inquiries. The system should route customers to specialized agents who can answer their questions or complete specific tasks using dedicated tools.

### Business Context

AirlineX has been struggling with their customer service operations. They receive thousands of calls daily asking about:

- Flight information and policies (baggage limits, seating, wifi availability)
- Seat changes and upgrades

Currently, human agents handle all inquiries, leading to long wait times and inconsistent responses. The company wants to implement an AI-powered multi-agent system where:

1. A **Triage Agent** acts as the initial point of contact and routes customers to appropriate specialized agents
2. A **FAQ Agent** answers general questions about airline policies
3. A **Seat Booking Agent** helps customers modify their seating arrangements

The system should maintain context throughout the conversation and seamlessly transfer customers between agents when needed.

---

## 🎯 Learning Objectives

By completing this assignment, you will learn to:

✅ Implement a multi-agent AI system architecture  
✅ Use Pydantic for context management  
✅ Create async functions and tools  
✅ Handle agent handoffs dynamically  
✅ Implement custom hooks and callbacks  
✅ Use the `agents` framework for building conversational AI  
✅ Trace and debug multi-agent conversations  
✅ Manage shared state across agents

---

## 📐 System Architecture

### Agent Hierarchy

```
Triage Agent (Entry Point)
├── FAQ Agent (General Questions)
└── Seat Booking Agent (Seat Modifications)
```

Each agent can hand customers back to the Triage Agent if they receive requests outside their domain.

### Context Schema

The system maintains shared context in `AirlineAgentContext` with the following fields:

- `passenger_name`: Name of the passenger (optional)
- `confirmation_number`: Flight confirmation number (optional)
- `seat_number`: Current or desired seat number (optional)
- `flight_number`: The flight number (optional)

### Agent Responsibilities

#### 1. **Triage Agent** (Entry Point)

- **Role**: Initial contact and routing
- **Responsibilities**:
  - Greet customers
  - Identify the customer's intent
  - Hand off to appropriate specialist agent
- **Tools**: None
- **Handoffs**: FAQ Agent, Seat Booking Agent

#### 2. **FAQ Agent** (Information Specialist)

- **Role**: Answer general airline questions
- **Responsibilities**:
  - Answer questions about baggage policies
  - Provide information about seating arrangements
  - Share details about in-flight wifi
  - Any other frequently asked questions
- **Tools**:
  - `faq_lookup_tool`: Searches for answers to common questions
- **Handoffs**: Triage Agent

#### 3. **Seat Booking Agent** (Action Specialist)

- **Role**: Handle seat modifications
- **Responsibilities**:
  - Request confirmation number from customer
  - Ask for desired seat preference
  - Update the seat assignment
- **Tools**:
  - `update_seat`: Updates the seat for a given confirmation
- **Handoffs**: Triage Agent
- **Special Hook**: `on_seat_booking_handoff` - Automatically generates a flight number when customer is handed off

---

## 🔧 Functional Requirements

### Core Features

1. **Interactive Loop**:

   - Continuously accept user input until program ends
   - Maintain conversation state across interactions
   - Display agent responses, tool calls, and handoffs

2. **FAQ Lookup Tool**:

   - Answer questions about:
     - **Baggage**: Size, weight limits, carry-on policies
     - **Seating**: Total seats, class distribution, exit rows, Economy Plus
     - **Wifi**: Network name and availability
   - Return appropriate responses or say "I don't know" for unknown topics

3. **Seat Update Tool**:

   - Accept confirmation number and new seat number
   - Update the shared context
   - Return confirmation message

4. **Dynamic Routing**:

   - Triage Agent must identify intent and route appropriately
   - Specialized agents should return to Triage for out-of-scope requests

5. **Context Management**:

   - Maintain passenger information across agent handoffs
   - Auto-populate flight number on seat booking handoff
   - Update context when customers provide information

6. **Tracing and Observability**:
   - Trace all agent interactions with unique conversation ID
   - Display agent name in all outputs
   - Show handoff events clearly

---

## 🛠️ Technical Requirements

### Dependencies

```bash
pydantic>=2.0.0
agents-framework  # Provided by instructor
```

### Required Imports

Your code must include:

```python
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
```

### Project Structure

```
airline_agents/
├── agents/
│   ├── __init__.py
│   └── [agent definitions]
├── tools/
│   ├── __init__.py
│   └── [tool functions]
├── hooks/
│   ├── __init__.py
│   └── [hook functions]
├── context.py
└── main.py
```

### Async Pattern

All functions should be async and use `asyncio.run(main())` to start the program.

---

## 📝 Implementation Requirements

### 1. Context Model

Create a Pydantic model `AirlineAgentContext` with:

- All fields optional (nullable)
- Proper typing hints
- Inherits from `BaseModel`

### 2. FAQ Lookup Tool

Implement `faq_lookup_tool` that:

- Accepts a question string
- Checks for keywords related to:
  - Baggage/luggage/carry-on
  - Seating/seats/plane
  - Wifi/internet/connectivity
- Returns appropriate pre-defined answers
- Returns "I'm sorry, I don't know the answer to that question" for unknown topics
- Uses `@function_tool` decorator with name and description overrides

**Expected Baggage Response:**
"You are allowed to bring one bag on the plane. It must be under 50 pounds and 22 inches x 14 inches x 9 inches."

**Expected Seating Response:**
"There are 120 seats on the plane. There are 22 business class seats and 98 economy seats. Exit rows are rows 4 and 16. Rows 5-8 are Economy Plus, with extra legroom."

**Expected Wifi Response:**
"We have free wifi on the plane, join Airline-Wifi"

### 3. Update Seat Tool

Implement `update_seat` that:

- Accepts context (wrapped in `RunContextWrapper`), confirmation number, and new seat
- Updates the context with confirmation number and seat number
- Validates that flight number exists (using assert)
- Returns a confirmation string
- Must use `@function_tool` decorator

### 4. Hook Function

Implement `on_seat_booking_handoff` that:

- Generates a random flight number in format "FLT-XXX" where XXX is 100-999
- Updates the context's flight_number
- Takes only `RunContextWrapper` as parameter
- Returns None

### 5. Agent Definitions

#### FAQ Agent

- Name: "FAQ Agent"
- Handoff description explaining its purpose
- Instructions include RECOMMENDED_PROMPT_PREFIX
- Define routine for handling customer queries
- Add FAQ lookup tool
- Include Triage Agent in handoffs

#### Seat Booking Agent

- Name: "Seat Booking Agent"
- Handoff description explaining its purpose
- Instructions include RECOMMENDED_PROMPT_PREFIX
- Define routine for collecting confirmation number, desired seat, and updating
- Add update_seat tool
- Include Triage Agent in handoffs
- Connect to `on_seat_booking_handoff` hook

#### Triage Agent

- Name: "Triage Agent"
- Handoff description explaining its purpose
- Instructions include RECOMMENDED_PROMPT_PREFIX
- No tools
- Handoffs to FAQ Agent and Seat Booking Agent (with hook)
- No circular dependencies initially

### 6. Main Loop

Implement `main()` function that:

- Starts with Triage Agent
- Maintains input items list
- Creates new context instance
- Generates unique conversation ID
- Infinite loop that:
  - Gets user input
  - Wraps in `trace()`
  - Runs agent with Runner
  - Displays all output items properly
  - Updates current agent and input items
- Handles MessageOutputItem, HandoffOutputItem, ToolCallItem, ToolCallOutputItem

---

## 🎁 Bonus Challenge

Add a fourth agent for handling complaints or special requests. The agent should:

- Be accessible from Triage
- Have at least one custom tool
- Use a hook to capture complaint details
- Display appropriate empathy and follow-up questions

---

## 🎮 Sample Interactions

### Interaction 1: FAQ about Baggage

```
Enter your message: What's the baggage policy?
Triage Agent: I'll transfer you to our FAQ specialist who can answer that question.
Handed off from Triage Agent to FAQ Agent
FAQ Agent: Our baggage policy allows one bag on the plane. It must be under 50 pounds and 22 inches x 14 inches x 9 inches.
```

### Interaction 2: Seat Change

```
Enter your message: I want to change my seat
Triage Agent: I'll transfer you to our seat booking specialist.
Handed off from Triage Agent to Seat Booking Agent
Seat Booking Agent: May I have your confirmation number, please?
Enter your message: ABC123
Seat Booking Agent: What seat would you like?
Enter your message: 12A
Seat Booking Agent: Calling a tool
Seat Booking Agent: Tool call output: Updated seat to 12A for confirmation number ABC123
```

### Interaction 3: Out-of-Scope Question

```
Enter your message: What's the weather today?
FAQ Agent: I'm sorry, I don't know the answer to that question. Let me transfer you back to our main agent.
Handed off from FAQ Agent to Triage Agent
Triage Agent: I'm sorry, I don't have access to weather information. Is there anything else I can help you with regarding your flight?
```

---

## 🚀 Getting Started

### Step 1: Setup Project

```bash
mkdir airline_agents
cd airline_agents
# Set up your Python environment with uv
# Install required dependencies
```

### Step 2: Create File Structure

```
touch airline_agents/__init__.py
touch tools.py
touch context.py
touch agents.py
touch main.py
```

### Step 3: Import Dependencies

Ensure all imports from the Technical Requirements section are included.

### Step 4: Implement in Order

1. Create the context model
2. Implement FAQ lookup tool
3. Implement update seat tool
4. Create the hook function
5. Define the three agents
6. Build the main loop

### Step 5: Test Your Implementation

Run various scenarios:

- Ask about baggage
- Request seat changes
- Test handoffs back to Triage
- Verify context updates

---

## 📚 Resources

- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Python Async/Await Tutorial](https://realpython.com/async-io-python/)
- [Multi-Agent Systems](https://docs.anthropic.com/claude/docs/multi-agent-systems)

---

## ⚠️ Common Pitfalls

1. **Forgetting async/await**: All functions must be async
2. **Wrong tool signatures**: Tools need specific signatures with `RunContextWrapper`
3. **Missing handoffs**: Agents must have bidirectional handoffs
4. **Context not updating**: Make sure to modify `context.context.property`
5. **Assertion failures**: Validate flight number exists before updating seat
6. **Output display**: Properly handle all output item types

---

## 📤 Submission Instructions

1. Create a repository for your project
2. Commit all code files
3. Include a README.md with:
   - Setup instructions
   - How to run the application
   - Example conversations
4. Submit the GitHub repository link

---

## 💡 Hints

- Start by understanding what each agent's role is
- Use the RECOMMENDED_PROMPT_PREFIX for consistency
- Test each tool individually before integrating
- The hook only fires on handoff, not on initial assignment
- Use meaningful agent names and descriptions
- Trace calls help debug the conversation flow

---

**Good luck! Build an amazing multi-agent system! 🚀**
