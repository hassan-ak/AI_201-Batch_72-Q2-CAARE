# Class 04 — MCQ Quiz (Async, Agents Execution Modes, Model Configuration, Design Patterns, Decorators)

### Instructions
- Choose the best answer (A, B, C, or D).
- Explanations are at the end — attempt first before peeking.

## Quiz

1. In the async vs sync diagrams, the main benefit of async execution is:
   - A) It makes CPU-bound tasks faster automatically
   - B) It overlaps waiting tasks so total wall time can shrink
   - C) It eliminates the need for functions
   - D) It increases code verbosity without performance impact

2. In Python, `await` inside an `async def` function means:
   - A) Block the entire interpreter until the result returns
   - B) Yield control so other awaiting tasks can run
   - C) Convert code to multithreaded execution
   - D) Force immediate cancellation of the task

3. `asyncio.gather(a(), b())` does what?
   - A) Runs tasks strictly sequentially
   - B) Runs tasks in parallel (concurrently) and waits for all
   - C) Cancels both tasks
   - D) Returns after the first completes

4. In the sync vs async agent demo, the async version finishes faster because:
   - A) It skips the database logging
   - B) Both agent call and DB log run concurrently
   - C) It uses a faster model
   - D) It caches the agent result

5. `Runner.run_sync(agent, prompt)` vs `await Runner.run(agent, prompt)` differ mainly in:
   - A) Output format
   - B) Whether the call blocks the current thread
   - C) Required API keys
   - D) Model capabilities

6. In model configuration Pattern 1 (global defaults), the agent sets:
   - A) A model object with client
   - B) A plain model name string (resolved via global defaults)
   - C) No model at all
   - D) A RunConfig per call

7. Pattern 2 (agent-level model object) is preferred when:
   - A) All code must share one model
   - B) Each agent might need a distinct provider or settings
   - C) You cannot import `OpenAIChatCompletionsModel`
   - D) You want to avoid explicit model references

8. Pattern 3 (runner-level overrides) uses `RunConfig` to:
   - A) Globally change Python version
   - B) Override model/provider per request
   - C) Patch environment variables automatically
   - D) Disable all tracing always

9. Pattern 4 (debug mode) adds which extra capability?
   - A) Auto-scaling GPU clusters
   - B) Verbose stdout logging + .env based secrets
   - C) Local fine-tuning pipeline
   - D) Built‑in retries disabled

10. The Orchestrator-Workers pattern features:
    - A) One agent doing everything (monolith)
    - B) An orchestrator delegating subtasks to specialized workers
    - C) Only parallel tasks with no coordination
    - D) A single evaluation loop only

11. Parallelization pattern key advantage:
    - A) Reduces cost always
    - B) Allows independent subtasks to run concurrently
    - C) Forces serialization of tasks
    - D) Removes need for error handling

12. Routing pattern chooses an agent based on:
    - A) Random selection
    - B) Task type / intent classification
    - C) Network MAC address
    - D) File system size

13. Prompt Chaining helps mainly with:
    - A) GPU acceleration
    - B) Breaking complex problems into ordered reasoning steps
    - C) Eliminating prompts entirely
    - D) Automatic billing setup

14. Evaluator-Optimizer loop stops when:
    - A) Model quota ends
    - B) Evaluation passes quality threshold
    - C) The first draft is generated
    - D) A random number matches seed

15. In the decorator lesson, `@wraps` from `functools` is used to:
    - A) Encrypt arguments
    - B) Preserve original function metadata (name, docstring)
    - C) Parallelize execution
    - D) Force type checking

16. Order of stacked decorators (top to bottom) means:
    - A) Bottom decorator wraps first, then upward
    - B) Top decorator always runs last internally
    - C) Order never matters
    - D) Python randomizes order

17. The `repeat(n)` decorator factory returns:
    - A) A constant string
    - B) A configured decorator that calls the wrapped function n times
    - C) An async event loop
    - D) A caching proxy

18. A timing decorator typically measures:
    - A) CPU cycles only
    - B) Wall-clock elapsed time around the call
    - C) Memory allocation exclusively
    - D) Source code length

19. Logging decorators improve:
    - A) Disk fragmentation
    - B) Observability of calls (arguments/results)
    - C) Network bandwidth
    - D) Python install size

20. Using environment variables instead of hard-coded keys primarily improves:
    - A) Performance of CPU-bound code
    - B) Secret hygiene and deployment flexibility
    - C) The number of returned tokens
    - D) Function recursion depth

21. Disabling tracing (`set_tracing_disabled(True)`) reduces:
    - A) Core agent logic correctness
    - B) Overhead / logging noise
    - C) Access to models
    - D) Ability to run asynchronously

22. `asyncio.create_task(coro)` is useful because it:
    - A) Blocks until completion
    - B) Schedules coroutine to run concurrently with others
    - C) Converts coroutine to thread directly
    - D) Forces cancellation

23. In the sync demo, total duration approximates the sum of steps because:
    - A) Steps are overlapped
    - B) Steps are sequential and blocking
    - C) The DB call is skipped
    - D) The agent result is cached

24. In the async demo, two tasks were run concurrently using:
    - A) threading.Thread
    - B) asyncio.gather on created tasks
    - C) subprocess.run
    - D) multiprocessing.Pool

25. A per-run override is most helpful when:
    - A) You always use one static model
    - B) You switch models based on user tier or experiment
    - C) You never log outputs
    - D) You cannot import RunConfig

26. A routing agent that misclassifies tasks primarily harms:
    - A) Orchestrator uptime
    - B) Task quality / correctness
    - C) Disk storage
    - D) Python versioning

27. Prompt chaining risk if overdone:
    - A) Faster runtime always
    - B) Unnecessary latency and token cost
    - C) Reduced clarity of intermediate reasoning
    - D) Guaranteed model failure

28. Parallelization downside:
    - A) All tasks must share same model
    - B) Coordination/aggregation complexity increases
    - C) Impossible to handle errors
    - D) Forces synchronous fallback

29. Evaluator-Optimizer loop danger:
    - A) Infinite refinement without stop condition
    - B) Immediate model deletion
    - C) No chance to improve outputs
    - D) Required GPU usage

30. Decorator factories differ from plain decorators because they:
    - A) Must return strings
    - B) Accept parameters and return a decorator
    - C) Disable other decorators automatically
    - D) Are only valid on classes

## Answer Key
1. B
2. B
3. B
4. B
5. B
6. B
7. B
8. B
9. B
10. B
11. B
12. B
13. B
14. B
15. B
16. A
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
30. B
