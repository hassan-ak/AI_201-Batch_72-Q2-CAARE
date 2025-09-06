# Prompt and Context Engineering: Effective AI Communication  
**Level 1 Certification Exam**  
**Exam Code:** L1:P0-PTE  
**Total Questions:** 130  
**Duration:** 2 Hours 30 Minutes  
**Difficulty Level:** Beginner Level  

> This Level 1 exam validates foundational competency in prompt engineering, context engineering, structured reasoning strategies, configuration parameters, MoE-aware prompting, and integrated agent design concepts.

---
## Key Topics Covered
The exam is divided into thematic sections, progressing from fundamentals to applied scenarios.

| Section | Topic Theme | Question Range | Count |
|---------|-------------|----------------|-------|
| 1 | Fundamentals | 1–15 | 15 |
| 2 | Configuration | 16–25 | 10 |
| 3 | Prompting Techniques | 26–40 | 15 |
| 4 | Best Practices & Pitfalls | 41–55 | 15 |
| 5 | Testing & Evaluation | 56–65 | 10 |
| 6 | Advanced Techniques & Tips | 66–75 | 10 |
| 7 | Mixture-of-Experts (MoE) | 76–85 | 10 |
| 8 | Practical Application | 86–95 | 10 |
| 9 | Context Engineering Integration (RAG + Prompts) | 96–105 | 10 |
|10 | Comprehensive / Applied Scenarios | 106–112 | 7 |
|11 | Context Engineering Core | 113–122 | 10 |
|12 | 6-Step Prompting Framework | 123–130 | 8 |
|   | **Total** |  | **130** |

---
## Instructions
- Unless marked (Select all that apply), there is exactly ONE correct answer.
- Multi-select questions list "(Select all that apply)"; all correct options must be chosen to receive credit.
- T/F questions: A = True, B = False (unless otherwise stated).
- Manage time: ~70 seconds per 5 questions.

---
## Section 1: Fundamentals (1–15)

1. The primary goal of prompt engineering is to:  
A. Reduce API latency  
B. Craft instructions to shape model behavior and outputs  
C. Replace retrieval pipelines  
D. Shrink embeddings  

2. Context engineering primarily focuses on:  
A. Hardware acceleration  
B. Providing the right supporting information at the right time  
C. Removing constraints from prompts  
D. Eliminating tool use  

3. Large Language Models fundamentally operate by:  
A. Executing symbolic logic graphs  
B. Predicting next tokens given prior tokens  
C. Parsing grammar trees deterministically  
D. Searching the open internet live by default  

4. A common cause of hallucination is:  
A. Too low temperature  
B. Missing or irrelevant grounding context  
C. Short prompts  
D. Using JSON schemas  

5. Vague prompts often produce:  
A. High determinism  
B. Unpredictable or generic outputs  
C. Guaranteed correctness  
D. Lower token counts  

6. In the prompt vs context distinction, "what you show" corresponds to:  
A. Prompt  
B. Context  
C. Decoder  
D. Tokenizer  

7. A strong initial workflow sequence is:  
A. Retrieval first → guess behavior  
B. Behavior prompt design → add relevant context  
C. Generate answers → append context later  
D. Skip retrieval entirely  

8. Seeing LLMs as "autocomplete engines" emphasizes:  
A. They reason like humans  
B. They depend on input pattern shaping  
C. They store queries permanently  
D. They internally fine-tune each call  

9. A failure mode of weak context engineering is:  
A. Precise JSON alignment  
B. Outdated or hallucinated facts  
C. Reduced temperature impact  
D. Smaller token usage  

10. Well-structured prompts assist models by:  
A. Expanding context window size physically  
B. Reducing ambiguity in expected output  
C. Increasing model training speed  
D. Disabling randomness controls  

11. Prompt engineering alone is insufficient when:  
A. You need dynamic knowledge grounding  
B. Tasks are trivial and self-contained  
C. Temperature = 0  
D. Output length is short  

12. Weak prompts often force you to:  
A. Add retrieval  
B. Iterate manually more times  
C. Lower token limits  
D. Increase top-K only  

13. A generic instruction like "Explain this" typically lacks:  
A. Output structure and audience clarity  
B. Temperature control  
C. Any tokens  
D. Model selection ability  

14. Command clarity improves:  
A. Resource metering  
B. Determinism of supply chain finance  
C. Relevance and structure of responses  
D. GPU utilization charts  

15. One advantage of explicit roles (e.g., "You are a policy analyst") is:  
A. Faster hardware  
B. Setting tone and evaluative perspective  
C. Forcing full truth  
D. Guaranteeing novelty  

---
## Section 2: Configuration (16–25)

16. Temperature controls:  
A. Context window size  
B. Randomness/creativity in token sampling  
C. Embedding dimensionality  
D. API concurrency  

17. A suitable temperature for deterministic parsing tasks:  
A. 0.0  
B. 0.8  
C. 0.9  
D. 1.0  

18. Top-K = 40 means:  
A. Only 40 tokens total allowed  
B. Sampling limited to 40 highest probability candidates  
C. 40% probability mass threshold  
D. 40 tokens are appended to context  

19. Top-P (nucleus sampling) selects:  
A. Highest probability tokens until cumulative threshold reached  
B. All tokens ranked equally  
C. Only tokens above frequency counts  
D. The longest tokens first  

20. Increasing max output tokens may increase:  
A. Latency and cost  
B. Deterministic structure always  
C. Hallucination immunity  
D. Context window capacity  

21. Balanced configuration (example) is closest to:  
A. Temp 0.2, Top-P 0.95, Top-K 30  
B. Temp 0.0, Top-P 0.5, Top-K 5  
C. Temp 0.9, Top-P 0.99, Top-K 70  
D. Temp 1.0, Top-P 0.8, Top-K 10  

22. For creative storytelling you might use:  
A. Temp 0.0  
B. Temp 0.8–0.9  
C. Temp negative  
D. Temp 0.05  

23. Setting temp = 0 with CoT helps:  
A. Generate more random sequences  
B. Consistent reasoning paths  
C. GPU scaling  
D. Larger context retrieval  

24. A conservative configuration aims to:  
A. Boost diversity heavily  
B. Reduce variance and ensure stable outputs  
C. Randomize token order  
D. Disable nucleus sampling  

25. Very high temperature risks:  
A. Monotony  
B. Increased incoherence  
C. Reduced token usage always  
D. Zero hallucinations  

---
## Section 3: Prompting Techniques (26–40)

26. Zero-shot prompting uses:  
A. No examples  
B. Exactly one example  
C. Four examples only  
D. Only chain-of-thought  

27. Few-shot prompting usually benefits from:  
A. 3–5 high-quality varied examples  
B. 30 random examples  
C. Redundant duplicates  
D. Unrelated narrative  

28. One-shot prompting is helpful when:  
A. You need broad style variation  
B. A single canonical format demonstration suffices  
C. The model rejects examples  
D. You need retrieval  

29. Role prompting influences:  
A. Output tone and framing  
B. Hardware speed  
C. Tokenization algorithm  
D. API pricing  

30. System prompting sets:  
A. Output path in GPU memory  
B. Global behavioral guidance  
C. Temperature override  
D. File system mounts  

31. Chain of Thought (CoT) is used to:  
A. Force JSON  
B. Encourage stepwise reasoning  
C. Lower latency  
D. Increase randomness  

32. Self-Consistency improves reliability by:  
A. Averaging across multiple reasoning paths  
B. Disabling token sampling  
C. Using only one forward pass  
D. Removing stepwise logic  

33. Step-Back prompting first asks:  
A. Code spec only  
B. General principle before specific application  
C. For final answer only  
D. For retrieval logs  

34. ReAct framework combines:  
A. Reasoning + tool actions/observations  
B. Random answers + temperature  
C. Roleplay + JSON  
D. Ranking + pruning  

35. Tree of Thoughts (ToT) explores:  
A. Single linear chain only  
B. Multiple candidate reasoning branches  
C. GPU memory configs  
D. Token splitting  

36. A risk of unbounded ToT is:  
A. Perfect stability  
B. Token explosion and latency increase  
C. Lower variance automatically  
D. Elimination of branching  

37. A good phrase to initiate CoT:  
A. "Skip the reasoning"  
B. "Let's think step by step"  
C. "Randomize paragraphs"  
D. "Return only final number"  

38. Prompt chaining refers to:  
A. Running multiple sequential structured steps  
B. Combining random prompts  
C. Obfuscating system messages  
D. Increasing token limit forcibly  

39. Using ReAct is especially helpful when:  
A. Internal model knowledge is enough  
B. External tool/data interaction is required  
C. You need zero context  
D. Temperature is disabled  

40. Multi-step reasoning reliability can be enhanced by:  
A. Low temperature + explicit reasoning instructions  
B. Removing structure + high temp  
C. Randomizing format  
D. Eliminating roles  

---
## Section 4: Best Practices & Pitfalls (41–55)

41. Strong prompts commonly include:  
A. Action verbs + structure + constraints  
B. Only adjectives  
C. Arbitrary disclaimers  
D. Blank context  

42. A JSON schema in a prompt provides:  
A. Output contract reducing parsing ambiguity  
B. Faster inference hardware  
C. Guaranteed factual truth  
D. Token compression algorithm  

43. Positive instructions are preferred over long negative lists because they:  
A. Guarantee novelty  
B. Increase clarity of desired behavior  
C. Reduce model size  
D. Force chain-of-thought  

44. Overloading a prompt with contradictory constraints leads to:  
A. Stable operation  
B. Confused outputs  
C. Lower cost automatically  
D. Better recall  

45. A weak prompt for analysis often lacks:  
A. Tone constraints  
B. Output sections and evaluation criteria  
C. Model name  
D. Token counter  

46. Variables in prompt templates improve:  
A. Reusability and scalability  
B. GPU caching only  
C. Grammar enforcement  
D. Binary compilation  

47. Excessive negative phrasing ("don't do X") can:  
A. Improve compliance  
B. Increase violation due to pattern anchoring  
C. Lower inference cost  
D. Force lower temperature  

48. Over-reliance on tools without reasoning steps risks:  
A. Hallucination mitigation  
B. Poor synthesis / shallow answers  
C. Eliminating latency  
D. Higher guardrail robustness  

49. A good content creation prompt includes:  
A. Topic, audience, tone, format, constraints  
B. Random inspirational phrases  
C. Only word count  
D. Internal API keys  

50. Efficient token usage involves:  
A. Deduping retrieved passages  
B. Repeating passages  
C. Inflating examples  
D. Keeping all history verbatim  

51. Adding explicit audience improves:  
A. Tone appropriateness  
B. Temperature  
C. Tokenization  
D. Static routing  

52. Strong coding prompts specify:  
A. Language, requirements, error handling, examples  
B. Only file name  
C. Generic task  
D. Broad creative style  

53. A failing cause of messy output:  
A. Clear formatting  
B. Ambiguous task description  
C. JSON schema  
D. Step labeling  

54. Excessive deadlines and micro-constraints can:  
A. Simplify  
B. Crowd out essential clarity  
C. Improve brevity  
D. Ensure reasoning quality  

55. A best practice for multi-part tasks:  
A. Run all at once with no structure  
B. Break into sequential sub-prompts (chaining)  
C. Remove formats  
D. Use placeholders only  

---
## Section 5: Testing & Evaluation (56–65)

56. A prompt testing framework tracks:  
A. Prompt version, settings, outcome quality  
B. GPU fan speed  
C. Compiler logs  
D. Operating system patch level  

57. A/B testing compares:  
A. Alternative prompt versions for performance  
B. GPU architectures  
C. Tokenizers only  
D. Latency only  

58. Key evaluation metrics include (Select all that apply):  
A. Accuracy  
B. Relevance  
C. Completeness  
D. Style alignment  

59. Consistency metric means:  
A. Output stable across repeated runs  
B. Token count is identical  
C. Always fewer tokens  
D. Zero randomness  

60. Logging retrieved context supports:  
A. Auditability and error analysis  
B. Guaranteed privacy loss  
C. Token inflation purposely  
D. Latency spikes always  

61. "Following instructions" metric checks:  
A. Format & constraint adherence  
B. Hardware alignment  
C. Token embeddings  
D. Storage usage  

62. Self-consistency evaluation involves:  
A. Multiple reasoning samples + consensus  
B. Skipping reasoning  
C. Lowering context window  
D. Removing schemas  

63. Capturing failure cases helps:  
A. Iterate targeted refinements  
B. Reduce logs  
C. Stop monitoring  
D. Add noise  

64. A rubric enhances:  
A. Systematic scoring across criteria  
B. GPU voltage control  
C. Token compression  
D. Random stream dropout  

65. The purpose of baseline prompt benchmarking is to:  
A. Establish reference performance for iteration  
B. Replace production  
C. Lower reliability  
D. Eliminate evaluation  

---
## Section 6: Advanced Techniques & Tips (66–75)

66. Context management in long chats benefits from:  
A. Periodic summarization of history  
B. Keeping everything verbatim forever  
C. Random removals  
D. Deleting system instructions  

67. Prompt chaining decomposes:  
A. Complex tasks into manageable steps  
B. JSON into prose only  
C. Temperature into tokens  
D. Tools into prompts  

68. Structured outputs (JSON) assist:  
A. Downstream automation & parsing  
B. Token inflation intentionally  
C. MoE routing directly  
D. Latency invariance  

69. Multi-modal prompting best practice:  
A. Specify clearly what to inspect in the image  
B. Ignore the visual modality  
C. Force random description  
D. Use only color names  

70. Prompt segmentation (plan → execute) improves:  
A. Clarity and error isolation  
B. Latency always  
C. GPU memory management  
D. Tokenization algorithm  

71. Hierarchical summarization helps with:  
A. Compressing large context into layered abstractions  
B. Expanding tokens  
C. Removing retrieval  
D. Destroying relevance  

72. Over-selection of context increases:  
A. Noise and dilution of key signals  
B. Precision always  
C. Determinism  
D. Model size  

73. A clear output contract reduces:  
A. Parsing ambiguity and post-processing errors  
B. Model speed  
C. Schema reuse  
D. Retrieval overhead  

74. Using voice memos for refinement can:  
A. Speed context enrichment with natural detail  
B. Decrease nuance  
C. Remove follow-up need automatically  
D. Force hallucinations  

75. A good retrieval pipeline should:  
A. Rank, dedupe, and trim irrelevant passages  
B. Always return full corpus  
C. Ignore metadata  
D. Force long chunks  

---
## Section 7: Mixture-of-Experts (MoE) (76–85)

76. MoE models activate:  
A. All experts per token  
B. A sparse subset of experts per token  
C. Only embedding layers  
D. CPU fallback networks  

77. The gating network's job is to:  
A. Route tokens to selected experts  
B. Serialize JSON  
C. Compress embeddings  
D. Handle GPU drivers  

78. A core advantage of MoE is:  
A. Bigger parameter space with limited per-token compute  
B. Fully deterministic routing  
C. Guaranteed lower hallucination  
D. No memory overhead  

79. A drawback of MoE can be:  
A. Routing instability or load imbalance  
B. Static perfect scaling  
C. Eliminated specialization  
D. No monitoring required  

80. Domain-specific upfront signals help MoE by:  
A. Steering router toward relevant experts  
B. Removing gating  
C. Increasing random drift  
D. Replacing retrieval  

81. Overly vague prompts in MoE often lead to:  
A. Optimal expert allocation  
B. Generic baseline experts triggering  
C. Stable deterministic behavior  
D. No variability  

82. Reducing temperature in MoE may reduce:  
A. Expert churn between runs  
B. Parameter count  
C. Retrieval need  
D. Tool usage  

83. Separating mixed tasks (code + legal + marketing) helps by:  
A. Preventing routing confusion  
B. Raising latency only  
C. Eliminating context need  
D. Lowering relevance  

84. Prompt ensembles (multiple variants) can mitigate:  
A. Routing variability  
B. Schema determinism  
C. Tokenization  
D. Guardrail design  

85. Expert specialization leads to:  
A. Enhanced niche performance  
B. Irrelevant domain collapse  
C. Removal of token sampling  
D. Guaranteed cost increase  

---
## Section 8: Practical Application (86–95)

86. A strong content prompt includes (Select all that apply):  
A. Audience  
B. Tone  
C. Format  
D. Constraints  

87. A robust code generation prompt includes:  
A. Language + error handling + example usage  
B. Only "Write code"  
C. Hidden constraints  
D. Random emojis  

88. Customer feedback analysis prompt should request:  
A. Sentiment breakdown and recommendations  
B. Only a poem  
C. Random sorting  
D. Obfuscated JSON  

89. For extracting structured data, include:  
A. Explicit JSON schema and null handling rules  
B. Just "extract"  
C. Reliance on temperature only  
D. Irrelevant disclaimers  

90. A product comparison prompt benefits from:  
A. Table columns defined (criteria)  
B. Vague request  
C. "Make it good" only  
D. Random examples  

91. A translation prompt improved by:  
A. Specifying audience & register  
B. Removing language names  
C. Asking for random dialect  
D. Adding misleading examples  

92. For summarization with constraints:  
A. Word/paragraph limits + key point focus  
B. Only "summarize"  
C. Provide full novel output  
D. Random tone shifts  

93. A sentiment + theme extraction prompt should:  
A. Ask for both categorical and thematic outputs  
B. Avoid structure  
C. Only output emojis  
D. Skip categories  

94. In code review prompting:  
A. Request complexity, edge cases, improvement suggestions  
B. Only say "review"  
C. Add irrelevant poem  
D. Force translation  

95. A brainstorming prompt improved by:  
A. Setting quantity, diversity criteria, and rejection filters  
B. Leaving open-ended  
C. Removing all constraints  
D. Using irrelevant persona  

---
## Section 9: Context Engineering Integration (96–105)

96. Retrieval-Augmented Generation (RAG) pairs prompting with:  
A. Dynamic context retrieval of relevant documents  
B. GPU clock control  
C. Token pruning  
D. Grammar correction  

97. Retrieval ranking improves:  
A. Relevance of selected passages  
B. Temperature scaling  
C. JSON field naming  
D. Output token limit  

98. Chunking optimization focuses on:  
A. Semantic boundaries & retrieval precision  
B. Increasing randomness  
C. Removing metadata  
D. Making larger than context window  

99. Deduplication avoids:  
A. Redundant noise diluting signal  
B. Correctness  
C. Schema generation  
D. Retrieval speed  

100. A common RAG instruction:  
A. "Answer only using provided context; cite sources"  
B. "Ignore supplied passages"  
C. "Invent sources if missing"  
D. "Drop all references"  

101. Logging which passages were used enables:  
A. Traceability and debugging  
B. Increased hallucination  
C. Latency spikes  
D. JSON corruption  

102. Over-retrieval can cause:  
A. Context flooding and distraction  
B. Guaranteed higher accuracy  
C. Perfect brevity  
D. Token immunity  

103. Context window viewed as RAM implies:  
A. Must allocate tokens judiciously  
B. Infinite retention  
C. Permanent memory  
D. Auto-expansion  

104. Temporal relevance filters help:  
A. Keep recent, discard stale info  
B. Increase token waste  
C. Inflate duplication  
D. Remove metadata  

105. Answer grounding reduces:  
A. Hallucination risk  
B. Retrieval cost always  
C. Context window size  
D. Need for instructions  

---
## Section 10: Comprehensive / Applied Scenarios (106–112)

106. For a policy Q&A bot you should:  
A. Instruct to answer only from context and cite sections  
B. Allow free speculation  
C. Encourage creative fiction  
D. Ignore irrelevant queries silently  

107. A multi-step report generation pipeline best begins with:  
A. Outline creation prompt  
B. Final polished draft  
C. Random segmentation  
D. Style injection first  

108. A weak story prompt example:  
A. "Write a 500-word sci-fi story for teens about resilience with 3 named characters"  
B. "Tell me something"  
C. "Generate structured arcs"  
D. "Plan then write"  

109. An MoE-aware redesign of a vague financial prompt should:  
A. Front-load domain tokens (e.g., "Role: Equity Analyst")  
B. Remove specificity  
C. Add unrelated domains  
D. Use only poetic phrasing  

110. A failing extraction pipeline often lacks:  
A. Clear schema + null handling rule  
B. Temperature settings  
C. Long disclaimers  
D. Creative persona  

111. A knowledge summarizer drifting off-topic likely needs:  
A. Stronger context filtering + explicit boundaries  
B. Higher temperature  
C. Random chunk mixing  
D. More vague instructions  

112. An agent repeatedly guesses missing IDs; fix by:  
A. Enforcing tool verification before response  
B. Increasing poetry  
C. Hiding context  
D. Removing guardrails  

---
## Section 11: Context Engineering Core (113–122)

113. Context engineering is critical when:  
A. Building autonomous agent workflows  
B. Asking a one-word definition  
C. Temperature = 0  
D. JSON parsing local  

114. Agent components include (Select all that apply):  
A. Model  
B. Tools  
C. Guardrails  
D. Orchestration  

115. Memory differs from knowledge because memory is:  
A. Dynamic conversational or session state  
B. Static corporate documentation  
C. Immutable facts only  
D. Code embeddings  

116. Guardrails focus on:  
A. Safety, policy, tone boundaries  
B. Lowering hardware cost  
C. Output token capping  
D. Ranking retrieval  

117. Orchestration handles:  
A. Deployment, monitoring, improvement loops  
B. Tokenization  
C. Markdown parsing  
D. PDF rendering  

118. Multi-agent splitting (e.g., search + synthesis) aids:  
A. Modularity and specialization  
B. Harder maintenance  
C. Latency only increase  
D. Eliminating documentation  

119. Writing context strategy allows:  
A. Persisting intermediate reasoning for later steps  
B. Deleting all state  
C. Replacing retrieval  
D. Blocking memory  

120. Compressing context prevents:  
A. Overload and truncation  
B. Relevance ranking  
C. Efficiency  
D. Temporal filtering  

121. Isolating context helps with:  
A. Security boundaries and tenant separation  
B. Increasing noise  
C. Unlimited sharing  
D. Removing structure  

122. "Actions carry implicit decisions" warns that:  
A. Tool outputs shift downstream state assumptions  
B. Tools have no effect  
C. Retrieval resets context  
D. Memory is static  

---
## Section 12: 6-Step Prompting Framework (123–130)

123. The first element of the 6-step framework is:  
A. Questions  
B. Command  
C. Roleplay  
D. Formatting  

124. Context should scale based on:  
A. Task complexity and stakes  
B. Always maximum tokens  
C. Random user preference  
D. Number of verbs  

125. The "Rule of Three" for context includes:  
A. Who / What / When  
B. Why / Cost / Budget  
C. Where / Mood / Color  
D. Past / Weather / Place  

126. Logic element defines:  
A. Output structure and reasoning flow  
B. Hardware driver versions  
C. API billing  
D. Persona age only  

127. Roleplay enhances:  
A. Domain credibility and tone specificity  
B. GPU frequency  
C. Pricing model  
D. Token embedding dimension  

128. Questions stage goal is to:  
A. Gather missing details for refinement  
B. Reduce accuracy  
C. Inflate token usage only  
D. Replace formatting  

129. Stopping question rounds occurs when:  
A. Model repeats or rephrases prior questions  
B. First round ends always  
C. Temperature hits 1.0  
D. Format changes  

130. A complete prompt example ends with:  
A. "Ask me N questions to tailor further"  
B. Removing context  
C. Setting random role  
D. Null command  

---
## Answer Key (Collapsible)
<details><summary><strong>Click to Reveal Answers</strong></summary>

1:B 2:B 3:B 4:B 5:B 6:B 7:B 8:B 9:B 10:B 11:A 12:B 13:A 14:C 15:B 16:B 17:A 18:B 19:A 20:A 21:A 22:B 23:B 24:B 25:B 26:A 27:A 28:B 29:A 30:B 31:B 32:A 33:B 34:A 35:B 36:B 37:B 38:A 39:B 40:A 41:A 42:A 43:B 44:B 45:B 46:A 47:B 48:B 49:A 50:A 51:A 52:A 53:B 54:B 55:B 56:A 57:A 58:A,B,C,D 59:A 60:A 61:A 62:A 63:A 64:A 65:A 66:A 67:A 68:A 69:A 70:A 71:A 72:A 73:A 74:A 75:A 76:B 77:A 78:A 79:A 80:A 81:B 82:A 83:A 84:A 85:A 86:A,B,C,D 87:A 88:A 89:A 90:A 91:A 92:A 93:A 94:A 95:A 96:A 97:A 98:A 99:A 100:A 101:A 102:A 103:A 104:A 105:A 106:A 107:A 108:B 109:A 110:A 111:A 112:A 113:A 114:A,B,C,D 115:A 116:A 117:A 118:A 119:A 120:A 121:A 122:A 123:B 124:A 125:A 126:A 127:A 128:A 129:A 130:A

</details>

---
## Scoring Guide
| Correct | Level |
|---------|-------|
| 115–130 | Distinction (Honors) |
| 100–114 | Pass – Strong Foundation |
| 85–99 | Pass – Developing (Review weak sections) |
| 70–84 | Borderline – Reinforce fundamentals |
| <70 | Not Yet Qualified – Re-study & retry |

---
## Post-Exam Reflection (Optional)
Record:
1. Lowest-performing section(s)
2. Top 3 missed concepts
3. Action plan: (a) Re-read sections, (b) Build 2 improved prompts, (c) Evaluate with rubric

---
## Study Tips Recap
- Practice iterative refinement with voice or written clarifications.
- Compare CoT vs no-CoT outputs at temperature 0.
- Create a mini RAG pipeline: ask vs grounded answer difference.
- Experiment with MoE-targeting: front-load domain vs vague; observe differences.

---
**End of Exam**
