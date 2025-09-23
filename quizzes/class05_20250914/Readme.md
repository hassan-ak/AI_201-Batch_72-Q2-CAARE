# Class 05 — MCQ Quiz (Prompt & Context Engineering, Advanced Prompting, MoE, Image/Video Generation)

Instructions
- Choose the best answer (A, B, C, or D).
- Attempt the quiz before checking the answer key at the end.
- This quiz covers: prompt engineering fundamentals, context engineering, advanced prompting (CoT, self-consistency, step-back, ReAct), mixture-of-experts (MoE), and media generation basics.

---

1. Prompt engineering primarily focuses on:
   - A) Training new models
   - B) Crafting instructions and constraints for a model to follow
   - C) Sharding data across GPUs
   - D) Compiling Python to C

2. Context engineering is about:
   - A) Controlling the model's temperature
   - B) Curating and supplying external knowledge (documents, retrieval) to the model
   - C) Installing dependencies
   - D) Building a model from scratch

3. Which of these is a good output contract practice?
   - A) Asking for free-form text without format
   - B) Requesting a strict JSON schema to validate responses
   - C) Leaving the model to decide output fields randomly
   - D) Avoid specifying examples

4. Temperature controls:
   - A) The model’s memory usage
   - B) The randomness/creativity of token sampling
   - C) The number of tokens returned
   - D) The hardware acceleration used

5. Few-shot prompting is best used when:
   - A) You want to provide multiple high-quality examples to show a pattern
   - B) You want to train a model offline
   - C) You need to change the model architecture
   - D) You are compiling code

6. Chain of Thought prompting helps when:
   - A) The answer is trivial
   - B) The task requires step-by-step reasoning or intermediate steps
   - C) You want to reduce token usage only
   - D) You want to bypass safety checks

7. Self-consistency improves reliability by:
   - A) Generating multiple reasoning paths and selecting the most frequent answer
   - B) Enforcing a single deterministic sample always
   - C) Randomly changing the prompt each time
   - D) Using a larger batch size at training time

8. Step-back prompting first asks:
   - A) A low-level implementation detail
   - B) A broad, general question to establish principles before the specific task
   - C) For the model’s training data
   - D) For user credentials

9. ReAct combines reasoning with:
   - A) Heavy-weight model training
   - B) Tool use or actions (searches, API calls) during reasoning
   - C) Automatic GPU scaling
   - D) Only offline computations

10. In retrieval-augmented generation (RAG), the retrieval component should be optimized for:
    - A) Random sampling
    - B) Precision and relevance to the query (ranking)
    - C) Reducing dataset size only
    - D) GPU memory usage

11. Chunking in context engineering refers to:
    - A) Breaking large documents into manageable passages for retrieval
    - B) Compressing images into tiles
    - C) Splitting training into epochs
    - D) Partitioning CPU cores

12. A freshness boost in retrieval means:
    - A) Prioritizing older documents always
    - B) Giving higher rank to recent or time-sensitive documents
    - C) Removing recent docs from index
    - D) Increasing temperature dynamically

13. When building a policy Q&A bot, a good practice is:
    - A) Hide source passages to make answers mysterious
    - B) Instruct the model to cite section IDs and say "Not in policy" if not found
    - C) Let the model hallucinate freely
    - D) Use no retrieval at all

14. Mixture-of-Experts (MoE) architectures are useful to:
    - A) Reduce model size by routing parts of input to specialist subnetworks
    - B) Remove the need for GPUs
    - C) Always increase latency dramatically
    - D) Replace prompt engineering entirely

15. A router in MoE chooses experts based on:
    - A) Random noise
    - B) Input features or task type to pick specialized experts
    - C) The host machine's hostname
    - D) The time of day only

16. MoE can help in prompt engineering by:
    - A) Training separate specialists and routing prompts to best-fit experts
    - B) Eliminating the need for retrieval
    - C) Always decreasing overall throughput
    - D) Constraining outputs to JSON only

17. For image generation prompts, which instruction is most helpful?
    - A) Provide unclear artistic directives
    - B) Specify composition, style, color palette, and reference images when possible
    - C) Use only single-word prompts
    - D) Avoid mentioning aspect ratio

18. Nano Banana and Veo 3 are examples of:
    - A) Small language models only
    - B) Image/video generation tools with model-specific prompting considerations
    - C) Database management systems
    - D) Hardware chips

19. When creating prompts for image editing, provide:
    - A) No guidance and let the model guess
    - B) Clear instructions about region, desired change, and references
    - C) Only the final filename
    - D) Only the original image with no instructions

20. For video generation, high-cost models mean:
    - A) Always run many candidates without cost concerns
    - B) Prefer careful prompt engineering, shorter trials, and staged pipelines to save cost
    - C) Never iterate
    - D) Use high temperature always

21. Output schemas are critical because:
    - A) They slow down inference
    - B) They make programmatic parsing and validation possible
    - C) They guarantee perfect accuracy
    - D) They increase token usage by 100x

22. Logging retrieval results for each answer helps you:
    - A) Verify what was grounded and debug hallucinations
    - B) Automatically reduce compute costs
    - C) Improve GPU utilization directly
    - D) Remove the need for prompt testing

23. Few-shot examples should be:
    - A) Randomly chosen from your dataset
    - B) High-quality, representative, and diverse to show the pattern
    - C) Always more than 20 examples
    - D) Only negative examples

24. When you say "answer only from context" in a prompt, you should also:
    - A) Avoid providing context
    - B) Provide strong instructions about how to handle missing info (e.g., say "Not in context")
    - C) Increase temperature
    - D) Remove output schema

25. For step-by-step math problems, which setting helps produce consistent chains of reasoning?
    - A) Temperature 0 and CoT prompting
    - B) Temperature 1.0 and no CoT
    - C) No context and high Top-P
    - D) Few-shot with random examples

26. Self-consistency requires:
    - A) Running multiple generations and aggregating the most frequent answer
    - B) Using deterministic greedy decoding only once
    - C) Reducing the number of tokens returned
    - D) Training a new model

27. When applying RAG, avoid:
    - A) Verifying the retrieved passages
    - B) Passing too much irrelevant context without ranking/filters
    - C) Logging the retrieval metadata
    - D) Adding citation IDs

28. A good retrieval pipeline will include:
    - A) Chunking, embedding, indexing, ranking, and freshness controls
    - B) Only a simple file read with no indexing
    - C) Blocking all updates forever
    - D) Removing passage metadata

29. For interactive prompt tuning, you should:
    - A) Iterate quickly with short experiments and measure outputs
    - B) Train large models from scratch every tweak
    - C) Avoid user testing
    - D) Use random prompts only

30. When costing experiments with high-cost media models, you should:
    - A) Run full-resolution renders for every trial
    - B) Start with low-res/short-duration trials and increase fidelity after validating prompts
    - C) Ignore cost and run as many as possible
    - D) Only use auto-generated prompts

---

Answer Key
1. B
2. B
3. B
4. B
5. A
6. B
7. A
8. B
9. B
10. B
11. A
12. B
13. B
14. A
15. B
16. A
17. B
18. B
19. B
20. B
21. B
22. A
23. B
24. B
25. A
26. A
27. B
28. A
29. A
30. B
