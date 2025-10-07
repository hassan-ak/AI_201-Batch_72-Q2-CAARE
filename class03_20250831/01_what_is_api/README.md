# Understanding APIs

## 1. What is an API?

**API** = _Application Programming Interface_  
A set of rules that lets one piece of software talk to another.

Think **“menu in a restaurant”**:

- You don’t enter the kitchen (service internals).
- You pick something from the menu (API request).
- The waiter (API) delivers the result without you worrying how it was made.

```mermaid
flowchart LR
    A[You - Client] --> B[API]
    B --> C[Service / Kitchen]
    C --> B
    B --> A
```

## 2. Everyday API Examples

| Situation        | “Kitchen” (Service)     | “Waiter” (API) | “You” (Client) |
| ---------------- | ----------------------- | -------------- | -------------- |
| Weather app      | Weather company servers | Weather API    | Your phone     |
| Ride-hailing app | Uber backend            | Booking API    | Passenger app  |
| Online payment   | PayPal / Stripe         | Payment API    | Store website  |

## 3. A Simple Public API in Action (Python)

We’ll use a public “cat fact” API — no account or API key needed.

```python
import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Random Cat Fact:", data["fact"])
else:
    print("Error:", response.status_code)
```

Here is another weather api example

```python
import requests

# Weather API endpoint for London
url = "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    current_weather = data.get("current_weather", {})
    print(f"Temperature: {current_weather.get('temperature')}°C")
    print(f"Windspeed: {current_weather.get('windspeed')} km/h")
    print(f"Weather Code: {current_weather.get('weathercode')}")
else:
    print("Error:", response.status_code)

```

## 4. OpenAI APIs — Two Main Types

### 🗨️ Chat Completions API (stateless)

- You send the _entire_ conversation each time.
- You control what memory the model sees.

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "What's the capital of France?"}
    ]
)
print(response.choices[0].message.content)
```

---

### 🧠 Responses API (stateful, tool-ready)

- Server remembers conversation history.
- Can add built-in tools like:
  - Web search
  - File retrieval
  - Code interpreter
  - Image generation

```python
from openai import OpenAI
client = OpenAI()

# First message with memory + tool
r1 = client.responses.create(
    model="gpt-4o-mini",
    input="Search the latest AI news in healthcare.",
    store=True,
    tools=[{"type": "web_search_preview"}]
)

# Follow-up without resending history
r2 = client.responses.create(
    previous_response_id=r1.id,
    input="Summarize those findings in bullet points."
)

print(r2.response.text)
```

## 5. Quick Comparison

| Feature    | Chat Completions               | Responses                  |
| ---------- | ------------------------------ | -------------------------- |
| Memory     | ❌ Send full history each time | ✅ Stored on server        |
| Tools      | Manual setup                   | One-line enable            |
| Best for   | Learning basics                | Assistants with memory     |
| Follow-ups | Resend all messages            | Use `previous_response_id` |

## 6. Which One to Start With?

- **Learning basics?** → Chat Completions
- **Quick assistant with memory?** → Responses

## 7. Next Practice

1. Try the **cat fact** API in Python.
2. Modify it for the **weather API**.
3. Make your first OpenAI API call.
