# Class 03 — Comprehensive MCQ Quiz

### Instructions

    - Select the best option (A, B, C, or D).
    - Answers with brief explanations are provided at the end — try not to peek first.

## Quiz

1. An API is best described as:

   - A) A database where data is stored
   - B) A set of rules for how software components communicate
   - C) A programming language for writing apps
   - D) A hardware device for connecting networks

2. In the “restaurant” analogy, the API is most similar to the:

   - A) Chef
   - B) Kitchen
   - C) Waiter/menu
   - D) Customer

3. Which of the following is NOT an example of an API usage from the class content?

   - A) Weather app using a weather company’s service
   - B) Online payment via PayPal/Stripe
   - C) Operating system kernel accessing drivers
   - D) Ride-hailing app booking backend

4. In the Python example using requests and catfact.ninja, which method is used to make an HTTP GET request?

   - A) requests.post
   - B) requests.get
   - C) requests.fetch
   - D) requests.call

5. In the sample Python code, what is checked to ensure the response is successful?

   - A) response.length > 0
   - B) response.is_ok
   - C) response.status_code == 200
   - D) response.status == "OK"

6. In the weather API sample, the JSON field used to print the current temperature is under:

   - A) data["weather"]["temp"]
   - B) data["temperature"]
   - C) data["current_weather"]["temperature"]
   - D) data["main"]["temp"]

7. The OpenAI Chat Completions API is described as:

   - A) Stateful with server-side memory
   - B) Stateless; you send the full conversation history each time
   - C) Only for image generation
   - D) Only for streaming audio

8. The OpenAI Responses API can:

   - A) Only return plain text
   - B) Store conversation history server-side and enable tools like web search
   - C) Run only in offline mode
   - D) Replace HTTP completely

9. For follow-up prompts using the Responses API, you typically provide:

   - A) The entire chat history again
   - B) Only the system prompt
   - C) previous_response_id
   - D) A database connection string

10. Best starting point for learning basics quickly is:

    - A) Responses API
    - B) Image generation API
    - C) Chat Completions API
    - D) Embeddings API

11. Which table pairing is correct according to the class comparison?

    - A) Chat Completions → Memory stored on server
    - B) Responses → Send full history each time
    - C) Chat Completions → Manual tools; Responses → One-line tools
    - D) Responses → No tool support

12. Programming Language vs Library vs Framework vs SDK: which mapping is correct?

    - A) Language = pre-built tools, Library = strict structure, Framework = vendor toolkit, SDK = core syntax
    - B) Language = core syntax, Library = pre-built tools, Framework = opinionated structure, SDK = vendor toolkit
    - C) Language = vendor toolkit, Library = core syntax, Framework = pre-built tools, SDK = strict rules
    - D) Language = opinionated structure, Library = vendor toolkit, Framework = core syntax, SDK = pre-built tools

13. In the house-building analogy, a Framework is like:

    - A) Bricks and cement
    - B) A hammer and drill
    - C) A pre-designed house layout
    - D) A kitchen stove

14. In the code snippet for a Library, which Python library was used to call a public API?

    - A) numpy
    - B) pandas
    - C) requests
    - D) flask

15. An SDK is best described as:

    - A) A strict set of language grammar rules
    - B) A company’s kit (code, tools, docs) to use their services
    - C) A server hardware specification
    - D) A file storage format

16. Where do you generate an OpenAI API key?

    - A) GitHub Settings
    - B) OpenAI Platform (API Keys page)
    - C) Google Cloud Console
    - D) Stripe Dashboard

17. Where do you generate a Gemini API key?

    - A) aistudio.google.com (API keys)
    - B) platform.openai.com (API keys)
    - C) console.aws.amazon.com (IAM)
    - D) developers.facebook.com (apps)

18. Security best practice for API keys is to:

    - A) Commit keys to public repos for easy access
    - B) Share keys in screenshots
    - C) Store keys in environment variables or secret managers
    - D) Hardcode keys permanently in code

19. When using higher quotas/production for Gemini, you may need to:

    - A) Disable billing
    - B) Enable billing
    - C) Fork the OpenAI repo
    - D) Use a different operating system

20. The OpenAI Agents SDK is primarily:

    - A) A low-code UI editor
    - B) A Python-first toolkit for building agentic apps with tools, handoffs, guardrails, tracing
    - C) A database engine
    - D) A GPU driver package

21. In the Agents SDK school analogy, a “handoff” is when:

    - A) The teacher grades the student
    - B) The receptionist agent delegates to a specialized agent (e.g., math teacher)
    - C) The student leaves the school
    - D) The guardrail blocks a request

22. In Agents SDK, a Tool is:

    - A) A JSON file holding configuration
    - B) A callable capability (calculator, web search, file lookup) the agent may choose to use
    - C) A debugging-only feature
    - D) The same as a Guardrail

23. The Runner in Agents SDK:

    - A) Stores API keys securely
    - B) Is a GUI to design prompts
    - C) Executes the agent loop (think → decide → act → finish) and returns the final output with trace
    - D) Is only for unit testing

24. Tracing in Agents SDK helps you:

    - A) Parallelize GPU kernels
    - B) Record decisions, tool calls, and handoffs to debug and improve workflows
    - C) Compile Python to C
    - D) Encrypt API requests end-to-end

25. The minimal “Hello World” example shows creating an Agent with:

    - A) name and instructions
    - B) database schema
    - C) CSS stylesheet
    - D) Dockerfile

26. When using Gemini via an OpenAI-compatible Chat Completions endpoint in the examples, the base_url isset to:

    - A) https://api.openai.com/v1/
    - B) https://generativelanguage.googleapis.com/v1beta/openai/
    - C) https://aistudio.google.com/api/
    - D) https://gemini.google.com/v1/chat/

27. When routing Agents SDK through Gemini’s OpenAI-compatible endpoint, the examples explicitly:

    - A) Use OpenAI Responses API with tracing enabled
    - B) Register an OpenAIChatCompletionsModel and disable tracing
    - C) Remove the model registration
    - D) Enable OpenAI-native tracing for better logs

28. In the simple and packaged app demos, the model string set for Gemini was:

    - A) gpt-4o-mini
    - B) gemini-2.5-pro
    - C) gemini-2.5-flash-lite
    - D) text-embedding-3-large

29. If you receive 401 Unauthorized from the example app, the likely fix is to:

    - A) Change Python version
    - B) Update the base_url to localhost
    - C) Provide a valid API key to AsyncOpenAI
    - D) Use a different requests timeout

30. The difference between Chat Completions and Responses APIs (as taught) includes:

    - A) Chat Completions has server memory; Responses does not
    - B) Both require resending the entire history
    - C) Responses can store history and enable built-in tools with minimal setup
    - D) Neither support tools of any kind

31. In the SDK comparison table, the OpenAI Agents SDK is characterized by:

    - A) Very high abstraction, low control
    - B) Minimal abstraction, high control, Python-first
    - C) Only for Google Cloud
    - D) No support for handoffs

32. A Guardrail in the Agents SDK is used to:

    - A) Increase GPU utilization
    - B) Validate/filter inputs/outputs for safety and policy compliance
    - C) Reduce HTTP latency
    - D) Replace the need for tools

    ***

## Answer Key with Explanations

1. B — API is a set of rules for software communication.
2. C — The waiter/menu mediates between you and the kitchen.
3. C — OS kernel/drivers weren’t covered as an example in the class content list.
4. B — requests.get was used.
5. C — The code checks for status_code == 200.
6. C — current_weather.temperature was shown in the snippet.
7. B — Chat Completions is stateless; send full history each time.
8. B — Responses can store history and enable tools like web search.
9. C — previous_response_id links the follow-up.
10. C — Start with Chat Completions for basics.
11. C — Chat Completions → manual tools; Responses → one-line enable and memory.
12. B — Language = core syntax; Library = pre-built tools; Framework = structure; SDK = vendor toolkit.
13. C — A framework is like a pre-designed house layout.
14. C — The requests library was used.
15. B — SDK is a vendor’s kit to use their services.
16. B — OpenAI Platform API Keys page.
17. A — Google AI Studio API keys page.
18. C — Use env vars/secret managers; don’t expose keys.
19. B — You may need to enable billing.
20. B — Python-first toolkit for agentic apps (tools, handoffs, guardrails, tracing).
21. B — Handoff delegates to a specialized agent.
22. B — A callable capability an agent may choose to use.
23. C — Runner executes the agent loop and returns output + trace.
24. B — Tracing records decisions, tool calls, and handoffs.
25. A — Agent created with name and instructions.
26. B — generativelanguage.googleapis.com/v1beta/openai/.
27. B — Register OpenAIChatCompletionsModel and disable tracing.
28. C — gemini-2.5-flash-lite in examples.
29. C — Provide a valid API key.
30. C — Responses can store history and offer built-in tools; Chat Completions is stateless.
31. B — Minimal abstraction, high control, Python-first.
32. B — Guardrails validate/filter for safety and policy compliance.

***

If you find any issues or want to propose additional questions, open a PR in this repository.
