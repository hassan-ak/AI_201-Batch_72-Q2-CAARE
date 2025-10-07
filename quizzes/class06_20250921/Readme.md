# Class 06 — MCQ Quiz (Swarm, Anthropic Patterns, Decorators, Tools, Model Settings, Dataclasses, Generics)

Instructions
- Choose the best answer (A, B, C, or D).
- Attempt the quiz before checking the answer key at the end.
- This quiz covers: Swarm/Agents concepts, Anthropic design patterns, Python decorators, tool calling, model settings, dataclasses, and generics.

---

1. OpenAI's Swarm framework primarily introduces which two abstractions?
   - A) Models and embeddings
   - B) Agents and handoffs
   - C) Dataclasses and generics
   - D) Prompts and contexts

2. A handoff in a multi-agent system is:
   - A) A way to cache model outputs
   - B) Transferring control and context from one agent to another
   - C) The final output formatting step
   - D) A function decorator

3. The Orchestrator-Workers pattern is best used when:
   - A) A single agent can handle all tasks without coordination
   - B) You need to decompose tasks and assign specialized workers
   - C) You want to avoid parallelization at all costs
   - D) The model must be retrained online

4. In the Anthropic design patterns, Prompt Chaining means:
   - A) Running multiple models in parallel
   - B) Breaking a task into ordered steps where each builds on the previous
   - C) Only using few-shot examples
   - D) Using chains of environment variables

5. Routing pattern requires:
   - A) A random selection mechanism
   - B) A classifier/router that directs requests to appropriate agents
   - C) A single monolithic model for all tasks
   - D) No context at all

6. A good use of Parallelization is:
   - A) When subtasks are independent and I/O-bound
   - B) When every step strictly depends on previous outputs
   - C) Only for GPU-bound training loops
   - D) To eliminate the need for error handling

7. Evaluator-Optimizer loops are useful for:
   - A) Infinite retries without stop conditions
   - B) Iteratively improving outputs via evaluate → refine cycles
   - C) Converting code into decorators
   - D) Storing data in dataclasses

8. Python decorators are best described as:
   - A) Language-level syntax for creating classes
   - B) Higher-order functions that wrap other functions to add behavior
   - C) A type of dataclass
   - D) A multiprocessing primitive

9. Which of the following preserves function metadata when writing decorators?
   - A) functools.wraps
   - B) typing.TypeVar
   - C) dataclasses.field
   - D) asyncio.gather

10. Order of stacked decorators:
    - A) Bottom decorator wraps first, then top wraps the result
    - B) Top decorator executes before the bottom one internally
    - C) Python ignores decorator order
    - D) Decorators must not be stacked

11. A decorator factory (e.g., `@repeat(n)`) is:
    - A) A decorator that requires no parameters
    - B) A function that returns a decorator, allowing parameters to be configured
    - C) Only valid in Python 2
    - D) Equivalent to functools.wraps

12. Tool calling in agents is used to:
    - A) Offload tasks that require external data or actions (weather, calculator)
    - B) Replace the model entirely
    - C) Store model weights
    - D) Increase token limits

13. A safe principle for tools is:
    - A) Each tool should do many unrelated jobs
    - B) One job per tool with predictable JSON outputs
    - C) Tools should expose secrets directly to the model
    - D) Avoid input validation for speed

14. In `ModelSettings`, `tool_choice="required"` means:
    - A) The agent must use tools when available
    - B) Tools are disabled completely
    - C) Tools are optional and chosen by chance
    - D) The model will use only a single tool forever

15. Temperature controls:
    - A) The model's randomness/creativity
    - B) The API key rotation frequency
    - C) The model's token budget
    - D) The dataclass immutability

16. `max_tokens` is used to:
    - A) Limit the length of the model's response
    - B) Set the model’s temperature
    - C) Choose which tool to call
    - D) Configure dataclass defaults

17. Parallel tool calls allow:
    - A) Multiple tools to be invoked concurrently for a single agent's decision
    - B) Only sequential tool usage
    - C) The model to run with multi-GPU automatically
    - D) Replacing `asyncio` altogether

18. Dataclasses automatically generate which methods by default?
    - A) __init__, __repr__, __eq__
    - B) train(), predict(), save()
    - C) __enter__, __exit__
    - D) compile(), link()

19. `field(default_factory=list)` is recommended to:
    - A) Share a single list instance across instances
    - B) Provide a fresh list for each instance to avoid shared mutable defaults
    - C) Make the dataclass frozen
    - D) Disable typing checks

20. `frozen=True` on a dataclass makes:
    - A) Objects immutable (assignment raises an error)
    - B) The dataclass unusable
    - C) __post_init__ run twice
    - D) Default_factory invalid

21. `__post_init__` in dataclasses is used to:
    - A) Run additional initialization or validation after auto-generated __init__
    - B) Replace __init__ entirely
    - C) Make the dataclass generic
    - D) Automatically serialize to JSON

22. `ClassVar` in dataclasses indicates:
    - A) A transient field to be stored in instances
    - B) A class-level attribute that should not be treated as a field
    - C) A private attribute
    - D) An outdated pattern not used anymore

23. A `TypeVar` is used to:
    - A) Define a placeholder type for generics
    - B) Store a runtime configuration parameter
    - C) Serialize dataclasses
    - D) Decorate functions automatically

24. `Generic[T]` on a class means:
    - A) The class is deprecated
    - B) The class is generic over type variable T for static typing
    - C) The class will be serialized to JSON automatically
    - D) The class must be frozen

25. Protocols in typing are useful for:
    - A) Structural typing (duck-typing for static checks)
    - B) Runtime enforcement of types at execution
    - C) Replacing dataclasses
    - D) Increasing temperature

26. When combining generics and dataclasses you should:
    - A) Avoid using TypeVar
    - B) Use TypeVar, Generic and proper annotations for type safety
    - C) Only use plain dicts
    - D) Always set frozen=True

27. In swarm and multi-agent systems, testing is easier when:
    - A) Agents are tightly coupled and stateful across the system
    - B) Agents are designed small, modular, and testable with clear handoffs
    - C) You avoid writing unit tests
    - D) The orchestrator does everything

28. A router that always misdirects tasks will primarily affect:
    - A) The price of cloud GPUs
    - B) Task quality and correctness
    - C) Dataclass defaults
    - D) Typing annotations

29. When writing decorators, use `wraps` to:
    - A) Preserve original function name and docstring
    - B) Make the function asynchronous
    - C) Convert dataclass into a decorator
    - D) Automatically time the function

30. A good practice for model settings experimentation is:
    - A) Change many knobs at once and compare
    - B) Change one setting at a time and measure effects
    - C) Never change defaults
    - D) Only use random seeds

---

Answer Key
1. B
2. B
3. B
4. B
5. B
6. A
7. B
8. B
9. A
10. A
11. B
12. A
13. B
14. A
15. A
16. A
17. A
18. A
19. B
20. A
21. A
22. B
23. A
24. B
25. A
26. B
27. B
28. B
29. A
30. B
