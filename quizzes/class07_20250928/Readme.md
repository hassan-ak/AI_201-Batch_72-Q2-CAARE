# Class 07 — MCQ Quiz (Local Context, Callables, Dynamic Instructions, Streaming, Agent Cloning, Chainlit)

Instructions
- Choose the best answer (A, B, C, or D).
- Attempt the quiz before checking the answer key at the end.
- This quiz covers: local context management, callables in Python, dynamic instructions, streaming outputs, agent cloning and shallow vs deep copy, and Chainlit basics.

---

1. Local context passed to `Runner.run(..., context=...)` is:
   - A) Sent to the LLM as part of the conversation
   - B) An internal object accessible to tools and not exposed to the LLM
   - C) Automatically logged to external services
   - D) Converted to JSON and appended to the prompt

2. `RunContextWrapper` is used to:
   - A) Wrap the LLM responses
   - B) Provide typed access to the local context inside tools and hooks
   - C) Persist context between runs permanently
   - D) Encrypt context for transport

3. A callable in Python is:
   - A) Any object that can be called like a function (e.g., implements `__call__`)
   - B) Only a regular function defined with `def`
   - C) Equivalent to a decorator
   - D) A special syntax available only in C extensions

4. `typing.Callable[[int, int], int]` describes:
   - A) A coroutine that returns nothing
   - B) A function that accepts two ints and returns an int
   - C) A dataclass with two int fields
   - D) A decorator factory

5. Dynamic instructions allow an agent to:
   - A) Change its behavior at runtime based on context or rules
   - B) Permanently change the model's weights
   - C) Bypass API authentication
   - D) Replace Python functions with SQL

6. A time-based dynamic instruction means:
   - A) The instruction changes depending on the current time or schedule
   - B) The instruction is always static
   - C) The instruction slows down execution artificially
   - D) The instruction causes the model to sleep

7. Streaming agent outputs are useful because:
   - A) They buffer all output until the run finishes
   - B) They allow real-time processing and event-driven handling of partial results
   - C) They make the model deterministic
   - D) They disable tool calls

8. In a streamed run, `tool_call_output_item` indicates:
   - A) The model is starting up
   - B) A tool returned a value during the run
   - C) The run has ended
   - D) The model will not generate messages

9. Agent cloning typically performs a shallow copy by default, meaning:
   - A) All nested objects are deeply duplicated
   - B) Mutable lists like `tools` are shared between original and clone unless replaced
   - C) The clone is completely independent in all ways
   - D) Cloning is impossible with SDK agents

10. To create an independent clone with its own tools list you should:
    - A) Use the same tools list and modify it later
    - B) Pass a new list for `tools` when calling `.clone(...)`
    - C) Modify the original agent’s tools after cloning
    - D) Use shallow copy utilities from the standard library

11. Shallow vs deep copy: shallow copies share references while deep copies:
    - A) Also share references
    - B) Duplicate nested objects recursively so changes don't affect the original
    - C) Only copy immutable objects
    - D) Are not useful in agent cloning

12. Chainlit is primarily used for:
    - A) Low-level model training
    - B) Creating interactive chat UIs for agent demos quickly
    - C) File compression
    - D) Scheduling background jobs only

13. A typical Chainlit chatbot project will include:
    - A) `main.py` code wiring, translations, and a `pyproject.toml` with dependencies
    - B) Only HTML files
    - C) No dependencies or configuration
    - D) A single binary executable

14. Local context should be designed as:
    - A) A random dict with mixed types and no schema
    - B) A typed object (dataclass/Pydantic) for clarity and safety
    - C) A JSON string only
    - D) Always serializable to database rows

15. Tools that access `wrapper.context` expect:
    - A) The wrapper to be a plain dict only
    - B) A typed `RunContextWrapper[T]` so the tool can use `wrapper.context` safely
    - C) No arguments at all
    - D) The LLM to read the context directly

16. In callables demo, an object with `__call__` implemented:
    - A) Cannot be used where a function is expected
    - B) Can be passed to functions that accept a callable parameter
    - C) Is slower than a function in all cases
    - D) Is equivalent to a dataclass automatically

17. Dynamic instruction fallbacks are important because:
    - A) Dynamic changes never fail
    - B) They provide a safe default behavior when dynamic logic errors or returns None
    - C) They speed up the model
    - D) They are only required for chained agents

18. Streaming best practice: handle event types explicitly because:
    - A) All events are identical
    - B) Different event items (tool output vs message) require different handling and display
    - C) Streaming is deprecated
    - D) Events are only for logs and should be ignored

19. When cloning agents for A/B testing, a good practice is:
    - A) Share the same objects to ensure identical behavior
    - B) Create independent clones with differing settings while keeping base consistent
    - C) Avoid versioning or documenting the clones
    - D) Use the same random seed for all tests only

20. Chainlit translations folder contains:
    - A) Only binary files
    - B) JSON language translation files used by UI localization
    - C) The model checkpoints
    - D) Compiled CSS only

21. Local context vs LLM context: LLM context is:
    - A) Never used for generation
    - B) The conversation/messages the model sees (system, user, assistant messages)
    - C) Only metadata stored in files
    - D) The Python runtime environment

22. `Runner.run(..., context=...)` requires that all parts of a single agent run:
    - A) Use different context types arbitrarily
    - B) Share the same context type to maintain consistency across tools/hooks
    - C) Serialize context to JSON first
    - D) Always be None

23. A callable type annotation improves:
    - A) Runtime speed
    - B) Code clarity and static type checking for function parameters
    - C) Model outputs directly
    - D) The network stack

24. Streaming can improve user experience by:
    - A) Making the user wait longer
    - B) Delivering partial results early so UIs can update progressively
    - C) Hiding intermediate steps completely
    - D) Removing the need for client-side handling

25. Which is true about deep copying an agent's tools list?
    - A) It is unnecessary because tools are always immutable
    - B) It prevents modifications to the original affecting the clone
    - C) It will always break tool references
    - D) It is faster than shallow copying

26. Dynamic instructions can be implemented via:
    - A) Static strings only
    - B) Functions that compute instructions at runtime based on context or state
    - C) Database schema migrations
    - D) Pure CSS changes

27. In the streaming example, `ItemHelpers.text_message_output(event.item)` is used to:
    - A) Compress the event
    - B) Extract and format the message output text from a stream event item
    - C) Translate text to another language
    - D) Stop the stream

28. Chainlit `pyproject.toml` mainly lists:
    - A) UI translations only
    - B) Python dependencies, entry points, and project metadata for the Chainlit demo
    - C) The full model weights
    - D) Only the README content

29. When designing local context, avoid including:
    - A) Sensitive secrets that must not leak to any part of the runtime
    - B) Typed helper objects like loggers
    - C) Small lookup caches used by tools
    - D) References to in-memory helpers

30. A practical exercise for local context is:
    - A) Passing a `UserInfo` dataclass instance to tools and using `wrapper.context.name` inside a tool
    - B) Writing context as raw text into prompts
    - C) Sending context to external APIs automatically
    - D) Storing context as global variables only

---

Answer Key
1. B
2. B
3. A
4. B
5. A
6. A
7. B
8. B
9. B
10. B
11. B
12. B
13. A
14. B
15. B
16. B
17. B
18. B
19. B
20. B
21. B
22. B
23. B
24. B
25. B
26. B
27. B
28. B
29. A
30. A
