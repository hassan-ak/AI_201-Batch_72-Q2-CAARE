# Prompt Engineering & MoE Mastery Quiz

> Comprehensive interactive-style quiz based on `readme.md` (prompt engineering fundamentals, advanced strategies, evaluation, MoE impacts, and best practices).

**How to Use**
- One correct answer unless marked *(Select all that apply)*.
- Difficulty: ★ (Easy) · ★★ (Moderate) · ★★★ (Advanced) · ★★★★ (Expert)
- Duplicate this file to keep a clean original; mark answers by adding an `X` into `[ ]`.
- Open the Answer Key only after completion.

---
### Quick Navigation
- [Prompt Engineering \& MoE Mastery Quiz](#prompt-engineering--moe-mastery-quiz)
    - [Quick Navigation](#quick-navigation)
  - [Section 1 – Fundamentals \& Definitions](#section-1--fundamentals--definitions)
  - [Section 2 – Prompt vs Context Engineering](#section-2--prompt-vs-context-engineering)
  - [Section 3 – LLM Mechanics \& Parameters](#section-3--llm-mechanics--parameters)
  - [Section 4 – Core Prompting Techniques](#section-4--core-prompting-techniques)
  - [Section 5 – Advanced Reasoning Strategies](#section-5--advanced-reasoning-strategies)
  - [Section 6 – Best Practices \& Structure](#section-6--best-practices--structure)
  - [Section 7 – Pitfalls \& Failure Modes](#section-7--pitfalls--failure-modes)
  - [Section 8 – Hands-On Applications](#section-8--hands-on-applications)
  - [Section 9 – Testing \& Evaluation](#section-9--testing--evaluation)
  - [Section 10 – Advanced 2025 Techniques](#section-10--advanced-2025-techniques)
  - [Section 11 – Mixture-of-Experts (MoE)](#section-11--mixture-of-experts-moe)
  - [Section 12 – MoE Prompt Adaptations](#section-12--moe-prompt-adaptations)
  - [Section 13 – Optimization \& Troubleshooting](#section-13--optimization--troubleshooting)
  - [BONUS Reflection](#bonus-reflection)
  - [Scoring](#scoring)
    - [Next Practice Loop](#next-practice-loop)

---
## Section 1 – Fundamentals & Definitions

**1. (★)** Prompt engineering is primarily about:  
- [ ] A) How you host the model  
- [ ] B) Crafting instructions to guide outputs  
- [ ] C) Reducing GPU memory usage  
- [ ] D) Compressing embeddings  

**2. (★)** Why is prompt engineering valuable to non-programmers?  
- [ ] A) It eliminates all need for models  
- [ ] B) It unlocks AI capability without coding  
- [ ] C) It guarantees perfect truth  
- [ ] D) It replaces data pipelines  

**3. (★)** The prompt sets model behavior; the context provides:  
- [ ] A) UI styling  
- [ ] B) Knowledge grounding  
- [ ] C) GPU selection  
- [ ] D) Memory cleanup  

**4. (★)** A good one‑liner distinction:  
- [ ] A) Prompt = retrieval, context = output  
- [ ] B) Prompt = how you ask; context = what you show  
- [ ] C) Prompt = database; context = cache  
- [ ] D) Prompt = MoE router; context = experts  

**5. (★)** Few-shot examples are best when they:  
- [ ] A) Are random  
- [ ] B) Represent target diversity & structure  
- [ ] C) Omit edge cases intentionally  
- [ ] D) Are longer than the task itself  

---
## Section 2 – Prompt vs Context Engineering

**6. (★)** Failure mode for weak prompt engineering:  
- [ ] A) Token overflow  
- [ ] B) Incorrect or messy format  
- [ ] C) Always perfect JSON  
- [ ] D) Reduced model size  

**7. (★)** Failure mode for weak context engineering:  
- [ ] A) Hallucination or outdated facts  
- [ ] B) Token duplication exceptions  
- [ ] C) Lossless compression  
- [ ] D) Stable retrieval precision  

**8. (★★)** Which belongs to context engineering levers?  
- [ ] A) Retrieval ranking & chunking  
- [ ] B) Command verbs  
- [ ] C) Output JSON schema  
- [ ] D) Role assignment  

**9. (★★)** Best initial approach for reliable responses:  
- [ ] A) Prompt only, no context  
- [ ] B) Context only, no prompt  
- [ ] C) Prompt + curated relevant context  
- [ ] D) Let model improvise  

**10. (★★)** A policy Q&A bot’s prompt: “Answer only from passages; cite section IDs.” This is:  
- [ ] A) Prompt layer instruction  
- [ ] B) Context chunking directive  
- [ ] C) Retrieval ranking heuristic  
- [ ] D) GPU batching rule  

---
## Section 3 – LLM Mechanics & Parameters

**11. (★)** Temperature mainly affects:  
- [ ] A) Latency only  
- [ ] B) Determinism / creativity trade-off  
- [ ] C) Output token cap override  
- [ ] D) Memory retention duration  

**12. (★)** Low temperature (≈0–0.2) is ideal for:  
- [ ] A) Poetic brainstorming  
- [ ] B) Stochastic art  
- [ ] C) Deterministic parsing tasks  
- [ ] D) Randomization testing  

**13. (★★)** Top-P (nucleus sampling) controls:  
- [ ] A) Cumulative probability mass threshold  
- [ ] B) Number of GPU cores  
- [ ] C) JSON validation  
- [ ] D) Embedding rank  

**14. (★★)** Top-K limits:  
- [ ] A) Max tokens per request  
- [ ] B) Candidate tokens considered  
- [ ] C) Context window compression factor  
- [ ] D) API retries  

**15. (★★)** A “Balanced” config (per guide) might be:  
- [ ] A) Temp 0.2, Top-P 0.95, Top-K 30  
- [ ] B) Temp 0.9, Top-P 0.99, Top-K 40  
- [ ] C) Temp 0.0, Top-P 0.5, Top-K 5  
- [ ] D) Temp 1.0, Top-P 0.8, Top-K 10  

**16. (★★)** Increasing output token limit risks:  
- [ ] A) Lower cost  
- [ ] B) Truncation avoidance always  
- [ ] C) Higher compute spend  
- [ ] D) Model retraining  

**17. (★★)** “LLMs are autocomplete systems” implies:  
- [ ] A) They infer meaning like humans  
- [ ] B) They predict next tokens based on statistical patterns  
- [ ] C) They compute symbolic logic graphs  
- [ ] D) They permanently store prompts  

---
## Section 4 – Core Prompting Techniques

**18. (★)** Zero-shot prompting:  
- [ ] A) Uses no examples  
- [ ] B) Requires exactly one example  
- [ ] C) Always worse than few-shot  
- [ ] D) Needs structured schema  

**19. (★)** Few-shot best practice:  
- [ ] A) Use identical labels only  
- [ ] B) Provide 3–5 varied, clean examples  
- [ ] C) Use unrelated examples  
- [ ] D) Inflate with repetition  

**20. (★)** System prompting:  
- [ ] A) Overrides internal model weights  
- [ ] B) Sets global behavioral framing  
- [ ] C) Disables context  
- [ ] D) Ensures zero hallucination  

**21. (★★)** Role prompting effect:  
- [ ] A) Forces parameter loading  
- [ ] B) Biases tone & viewpoint  
- [ ] C) Alters decoding algorithm  
- [ ] D) Expands context window  

**22. (★★)** Contextual prompting adds:  
- [ ] A) Unrelated filler  
- [ ] B) Domain-relevant background  
- [ ] C) Forced retrieval  
- [ ] D) Random noise  

**23. (★★)** Good structured template includes (Select all that apply):  
- [ ] A) Task  
- [ ] B) Context  
- [ ] C) Output format  
- [ ] D) Example  

---
## Section 5 – Advanced Reasoning Strategies

**24. (★)** “Let’s think step by step” relates to:  
- [ ] A) Chain of Thought  
- [ ] B) ReAct  
- [ ] C) MoE routing  
- [ ] D) Prompt chaining  

**25. (★★)** Self-consistency improves reliability by:  
- [ ] A) Using multiple reasoning samples & voting  
- [ ] B) Disabling temperature  
- [ ] C) Removing output  
- [ ] D) Limiting to one token  

**26. (★★)** Step-back prompting first requests:  
- [ ] A) Narrow execution only  
- [ ] B) Broader principles before specifics  
- [ ] C) Code generation only  
- [ ] D) JSON shape first  

**27. (★★)** ReAct couples reasoning with:  
- [ ] A) Audio rendering  
- [ ] B) Tool actions & observations  
- [ ] C) MoE expert pruning  
- [ ] D) Batch caching  

**28. (★★★)** Tree of Thoughts advantage:  
- [ ] A) Single deterministic path  
- [ ] B) Parallel exploration of alternative branches  
- [ ] C) Guaranteed time savings  
- [ ] D) Eliminates evaluation  

**29. (★★★)** Risk of unbounded ToT exploration:  
- [ ] A) Structured convergence  
- [ ] B) Token explosion & latency  
- [ ] C) Automatic pruning  
- [ ] D) Deterministic uniformity  

**30. (★★★)** ReAct pattern cycle:  
- [ ] A) Action → Thought → Ignore  
- [ ] B) Thought → Action → Observation  
- [ ] C) Answer → Retry → Answer  
- [ ] D) Plan → End  

---
## Section 6 – Best Practices & Structure

**31. (★)** Good prompt style:  
- [ ] A) Explicit, specific, testable  
- [ ] B) Vague but polite  
- [ ] C) Long disclaimers first  
- [ ] D) Hidden requirements  

**32. (★)** “Use action verbs” helps by:  
- [ ] A) Reducing schema  
- [ ] B) Clarifying expected operations  
- [ ] C) Forcing more tokens  ̇ 
- [ ] D) Compressing context  

**33. (★★)** Output contracts (schemas) reduce:  
- [ ] A) Parse ambiguity  
- [ ] B) Cost always  
- [ ] C) Domain drift  
- [ ] D) Token length required  

**34. (★★)** Variables in prompt templates enable:  
- [ ] A) Reusability across domains  
- [ ] B) Free inference  
- [ ] C) Higher hallucination  
- [ ] D) Context deletion  

**35. (★★)** Documenting effective prompts provides:  
- [ ] A) Institutional memory & repeatability  
- [ ] B) Output key encryption  
- [ ] C) Faster GPUs  
- [ ] D) Auto-fine-tuning  

**36. (★★)** Separating Task / Context / Format / Example improves:  
- [ ] A) Maintainability & clarity  
- [ ] B) Token burn only  
- [ ] C) Noise injection  
- [ ] D) Random ordering  

---
## Section 7 – Pitfalls & Failure Modes

**37. (★)** Ambiguous instructions →  
- [ ] A) Predictable precision  
- [ ] B) Unpredictable outputs  
- [ ] C) Hard token limit  
- [ ] D) Guaranteed brevity  

**38. (★)** Too many constraints can:  
- [ ] A) Over-restrict creativity  
- [ ] B) Improve adaptability  
- [ ] C) Increase model awareness  
- [ ] D) Force better memory  

**39. (★★)** Ignoring token limits may cause:  
- [ ] A) Mid-sentence truncation  
- [ ] B) Auto-compression fallback  
- [ ] C) Cost reduction  
- [ ] D) Extension automatically  

**40. (★★)** Not testing variations leads to:  
- [ ] A) Missed optimization opportunities  
- [ ] B) Guaranteed robustness  
- [ ] C) Automatic A/B blending  
- [ ] D) Perfect generalization  

**41. (★★)** Contradictory instructions cause:  
- [ ] A) Model internal rewrite  
- [ ] B) Confused or inconsistent output  
- [ ] C) Fewer tokens emitted  
- [ ] D) Automatic self-heal  

**42. (★★)** Overusing negative “don’t” phrasing vs positive directives may:  
- [ ] A) Clarify style  
- [ ] B) Increase violation risk  
- [ ] C) Guarantee safety  
- [ ] D) Force consistency  

---
## Section 8 – Hands-On Applications

**43. (★)** Improved version of a basic content task added:  
- [ ] A) Audience, tone, constraints & format  
- [ ] B) Only length  
- [ ] C) Random hashtags  
- [ ] D) Irrelevant disclaimers  

**44. (★★)** Data analysis improved prompt includes:  
- [ ] A) Defined output sections & sentiment breakdown  
- [ ] B) Only “analyze this”  
- [ ] C) Pure narrative  
- [ ] D) Hidden examples  

**45. (★★)** Code generation best request includes:  
- [ ] A) Requirements + examples + type hints + docstring  
- [ ] B) “Write code” only  
- [ ] C) Obfuscated instructions  
- [ ] D) Unordered constraints  

**46. (★★)** Prompt chaining decomposes:  
- [ ] A) Single step parallelism  
- [ ] B) Complex tasks into sequential steps  
- [ ] C) JSON into markdown  
- [ ] D) Memory into tokens  

**47. (★★)** Multi-modal prompting requires:  
- [ ] A) Explicit instructions about image focus  
- [ ] B) Ignoring the image  
- [ ] C) Removing text  
- [ ] D) Only color directives  

**48. (★★)** Context management in long chats benefits from:  
- [ ] A) Periodic summarization  
- [ ] B) Random injection  
- [ ] C) Dropping all history  
- [ ] D) Inflating tokens intentionally  

---
## Section 9 – Testing & Evaluation

**49. (★)** Testing framework documents:  
- [ ] A) Prompt versions & outcome notes  
- [ ] B) GPU drivers  
- [ ] C) Source license  
- [ ] D) DNS latency  

**50. (★)** A/B testing compares:  
- [ ] A) Multiple prompt variants for performance  
- [ ] B) GPU voltage  
- [ ] C) Only temperature values  
- [ ] D) UI fonts  

**51. (★★)** Evaluation dimensions include (Select all that apply):  
- [ ] A) Accuracy  
- [ ] B) Relevance  
- [ ] C) Completeness  
- [ ] D) Style fit  

**52. (★★)** Factual accuracy is strengthened by:  
- [ ] A) Forcing creativity  
- [ ] B) Retrieval grounding + citations  
- [ ] C) Removing context  
- [ ] D) Max temperature  

**53. (★★)** Consistency metric means:  
- [ ] A) Same prompt yields similar outputs  
- [ ] B) Faster inference only  
- [ ] C) Higher perplexity  
- [ ] D) Fewer tokens  

**54. (★★)** Logging retrieved context per answer assists:  
- [ ] A) Audit & error analysis  
- [ ] B) Irreversible deletion  
- [ ] C) Token inflation only  
- [ ] D) Style divergence  

---
## Section 10 – Advanced 2025 Techniques

**55. (★)** Structured outputs (JSON etc.) are used for:  
- [ ] A) Downstream machine parsing  
- [ ] B) Random creativity only  
- [ ] C) Cost reduction exclusively  
- [ ] D) Delaying evaluation  

**56. (★★)** Prompt chaining example pattern:  
- [ ] A) Outline → Expand → Refine  
- [ ] B) Final → First Draft → Delete  
- [ ] C) Compress → Lose context  
- [ ] D) Retry → Retry → Retry  

**57. (★★)** Multi-step decomposition helps with:  
- [ ] A) Managing cognitive load & quality control  
- [ ] B) Increasing hallucination  
- [ ] C) Obfuscation  
- [ ] D) Reducing alignment  

**58. (★★)** Using citations in policy Q&A reduces:  
- [ ] A) Traceability  
- [ ] B) Trustworthiness  
- [ ] C) Ambiguity & unverifiable claims  
- [ ] D) Token control  

**59. (★★)** Retrieval deduplication prevents:  
- [ ] A) Redundant noise competing with key signals  
- [ ] B) Schema validation  
- [ ] C) Relevance ranking  
- [ ] D) Compression benefits  

**60. (★★★)** “Optimize chunking” aims to:  
- [ ] A) Align semantic boundaries & retrieval precision  
- [ ] B) Shrink embedding dimension  
- [ ] C) Remove metadata  
- [ ] D) Increase random overlap  

---
## Section 11 – Mixture-of-Experts (MoE)

**61. (★)** MoE activates:  
- [ ] A) All experts per token  
- [ ] B) A sparse subset of experts  
- [ ] C) Only embedding layer  
- [ ] D) GPU kernels manually  

**62. (★)** Core MoE benefit:  
- [ ] A) Uniform dense compute  
- [ ] B) Parameter scaling without proportional compute  
- [ ] C) Eliminates routing risk  
- [ ] D) Removes need for prompting  

**63. (★★)** Gating network function:  
- [ ] A) Pick relevant experts for each token  
- [ ] B) Compress outputs to JSON  
- [ ] C) Enforce citation style  
- [ ] D) Manage GPU scheduling only  

**64. (★★)** Sparse activation yields:  
- [ ] A) Efficiency vs dense models  
- [ ] B) Guaranteed determinism  
- [ ] C) Higher always-on latency  
- [ ] D) Mandatory hallucination  

**65. (★★)** Expert specialization advantage:  
- [ ] A) Uniform mediocrity  
- [ ] B) Better niche task handling  
- [ ] C) Removal of retrieval  
- [ ] D) Static routing only  

**66. (★★)** Drawback of MoE:  
- [ ] A) Impossible scaling  
- [ ] B) Routing instability & load imbalance  
- [ ] C) Lower overall capacity  
- [ ] D) No memory usage  

**67. (★★★)** Load balancing losses help:  
- [ ] A) Prevent expert over-concentration  
- [ ] B) Eliminate need for training  
- [ ] C) Force all experts active  
- [ ] D) Remove routing entirely  

---
## Section 12 – MoE Prompt Adaptations

**68. (★)** Early domain signals help by:  
- [ ] A) Steering router toward relevant experts  
- [ ] B) Reducing vocab size  
- [ ] C) Disabling gating  
- [ ] D) Increasing randomness  

**69. (★★)** Vague prompts in MoE may:  
- [ ] A) Activate generic suboptimal experts  
- [ ] B) Increase guaranteed precision  
- [ ] C) Always route to best specialist  
- [ ] D) Improve determinism  

**70. (★★)** Few-shot exemplars in MoE should:  
- [ ] A) Match domain & format precisely  
- [ ] B) Be intentionally noisy  
- [ ] C) Be cross-domain blended  
- [ ] D) Use mixed languages arbitrarily  

**71. (★★)** Reducing temperature in MoE can reduce:  
- [ ] A) Expert churn across runs  
- [ ] B) Parameter count  
- [ ] C) Context need  
- [ ] D) Routing mechanism  

**72. (★★★)** Sequential multi-step domain hints (plan → solve) can:  
- [ ] A) Guide progressive expert selection  
- [ ] B) Remove chain-of-thought  
- [ ] C) Disable gating  
- [ ] D) Break retrieval  

**73. (★★★)** Overlong preambles risk:  
- [ ] A) Burying crucial routing cues  
- [ ] B) Guaranteed better routing  
- [ ] C) Increasing expert precision  
- [ ] D) Reducing token cost  

**74. (★★★)** Mixed-task (legal + code + marketing) in one prompt may:  
- [ ] A) Cause routing oscillation & diluted focus  
- [ ] B) Improve specialization  
- [ ] C) Lower ambiguity  
- [ ] D) Simplify evaluation  

**75. (★★★)** Prompt ensembles (multiple variants) help mitigate:  
- [ ] A) Routing variability  
- [ ] B) Model size  
- [ ] C) GPU memory errors  
- [ ] D) Token billing  

---
## Section 13 – Optimization & Troubleshooting

**76. (★)** “Front-load domain tokens” addresses:  
- [ ] A) Early routing accuracy  
- [ ] B) Output pagination  
- [ ] C) Schema generation  
- [ ] D) Token billing  

**77. (★★)** Inconsistent answers across runs → first try:  
- [ ] A) Add sharper domain anchor & lower temperature  
- [ ] B) Remove task description  
- [ ] C) Add random prose  
- [ ] D) Increase noise  

**78. (★★)** Model missing intended skill (math) → add:  
- [ ] A) “Task type: quantitative derivation” label + small exemplar  
- [ ] B) Remove numbers  
- [ ] C) Raise temperature  
- [ ] D) Add poetic flair  

**79. (★★)** Mixed-topic responses → solution:  
- [ ] A) Split into sequential focused prompts  
- [ ] B) Add extraneous synonyms  
- [ ] C) Use broad metaphors  
- [ ] D) Expand unrelated context  

**80. (★★★)** Retrieval noise causing dilution → fix:  
- [ ] A) Improve ranking + dedupe + filter  
- [ ] B) Random shuffle  
- [ ] C) Add all documents  
- [ ] D) Increase temperature  

**81. (★★★)** JSON format instability → fix:  
- [ ] A) Provide strict schema + example + validation reminder  
- [ ] B) Remove structure  
- [ ] C) Add emojis  
- [ ] D) Use free-form paragraphs  

**82. (★★★)** Long multi-turn chat drift → mitigate with:  
- [ ] A) Rolling summarized memory  
- [ ] B) Append all history forever  
- [ ] C) Discard system instructions  
- [ ] D) Increase verbosity  

**83. (★★★)** Overfitting prompts to initial tests risks:  
- [ ] A) Poor generalization later  
- [ ] B) Universal robustness  
- [ ] C) Zero variance  
- [ ] D) Automatic adaptation  

**84. (★★★★)** Governance requiring PII redaction before summarization → implement:  
- [ ] A) Preprocessing guardrail & filtered context layer  
- [ ] B) Let model improvise  
- [ ] C) Skip summarization  
- [ ] D) Mix raw + sanitized arbitrarily  

**85. (★★★★)** Hallucination about source doc likely due to:  
- [ ] A) Missing retrieval grounding + answer-only-from-context instruction  
- [ ] B) Structured output contract  
- [ ] C) Proper citations  
- [ ] D) Low temperature usage  

**86. (★★★★)** Unstable MoE expert utilization logs show imbalance → adjust:  
- [ ] A) Routing/aux losses or prompt domain clarity  
- [ ] B) Remove all structure  
- [ ] C) Add noise tokens  
- [ ] D) Force high temperature  

**87. (★★★★)** Latency spike from ToT breadth → fix:  
- [ ] A) Limit breadth & introduce scoring heuristic early  
- [ ] B) Increase branches arbitrarily  
- [ ] C) Remove evaluation  
- [ ] D) Disable pruning  

**88. (★★★★)** Outdated retrieval results → fix:  
- [ ] A) Add freshness filters + recency weighting  
- [ ] B) Keep stale chunks  
- [ ] C) Remove metadata  
- [ ] D) Disable ranking  

**89. (★★★★)** Multi-lingual mix harming routing → fix:  
- [ ] A) Force single-language constraint early  
- [ ] B) Add random language codes  
- [ ] C) Switch languages mid-response  
- [ ] D) Remove domain terms  

**90. (★★★★)** Over-stuffed context window hitting limits → fix:  
- [ ] A) Summarize, compress key points, drop irrelevant  
- [ ] B) Add entire corpus  
- [ ] C) Repeat important passages  
- [ ] D) Inflate examples  

---
## BONUS Reflection

**91. (Reflection)** Draft a reusable multi-step evaluation rubric for your own prompts.

**92. (Reflection)** Write a meta-prompt asking an LLM to improve retrieval grounding for policy Q&A.

---
<details>
<summary><strong>Answer Key (click to reveal)</strong></summary>

1:B 2:B 3:B 4:B 5:B 6:B 7:A 8:A 9:C 10:A 11:B 12:C 13:A 14:B 15:A 16:C 17:B 18:A 19:B 20:B 21:B 22:B 23:A,B,C,D 24:A 25:A 26:B 27:B 28:B 29:B 30:B 31:A 32:B 33:A 34:A 35:A 36:A 37:B 38:A 39:A 40:A 41:B 42:B 43:A 44:A 45:A 46:B 47:A 48:A 49:A 50:A 51:A,B,C,D 52:B 53:A 54:A 55:A 56:A 57:A 58:C 59:A 60:A 61:B 62:B 63:A 64:A 65:B 66:B 67:A 68:A 69:A 70:A 71:A 72:A 73:A 74:A 75:A 76:A 77:A 78:A 79:A 80:A 81:A 82:A 83:A 84:A 85:A 86:A 87:A 88:A 89:A 90:A

</details>

---
## Scoring
| Correct | Level |
|---------|-------|
| 81–90 | Elite Prompt Systems Architect |
| 72–80 | Advanced Practitioner |
| 60–71 | Strong Intermediate |
| 45–59 | Developing – strengthen evaluation & MoE adaptation |
| <45 | Revisit fundamentals & structured experimentation |

---
### Next Practice Loop
1. Choose a real use case (Q&A bot, extractor, planner).  
2. Write baseline zero-shot prompt.  
3. Add structure (Task / Context / Format / Example).  
4. Add retrieval grounding (if applicable).  
5. Add evaluation rubric & log outputs.  
6. Introduce MoE-oriented routing hints (early domain signals).  
7. Compare: accuracy, hallucination rate, consistency.  
8. Iterate with A/B prompt variants.  

---
Mastery compounds through deliberate, instrumented iteration.
