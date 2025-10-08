# **Assignment 5 — Chainlit “Agent+Tools” (Packaged App)**

## 🎯 **Objective**

Create an interactive **AI Chatbot** using the **OpenAI Agents SDK** and **Chainlit**.
The chatbot must have streaming responses, use at least one tool, and save the entire chat history.
You must also ensure a fully customized UI and a proper packaged Python project structure.

---

## 🧠 **Learning Outcomes**

By completing this assignment, you will learn to:

- Build a Chainlit-based chatbot that integrates with the OpenAI Agents SDK.
- Use environment variables safely with `.env`.
- Stream model responses in real time.
- Organize projects using a **packaged app** layout.
- Customize the Chainlit UI (theme, logo, and layout).
- Add and use tools within the chatbot.
- Save chat histories automatically in structured JSON format.

---

## 🏗️ **Assignment Requirements**

1. **Develop a chatbot** using **Chainlit** and the **OpenAI Agents SDK**.
2. Use a **packaged app structure** (`src/` layout).
3. Define a **script in `pyproject.toml`** so that the chatbot can be started with:

   ```
   uv run chatbot
   ```

4. Use a `.env` file for environment variables and commit only `.env.example`.
5. Keep **agent logic** and **Chainlit code** in **separate packages**.
6. The chatbot’s **responses must be streamed** in real time.
7. When the chat ends, **save the chat history** as a JSON file in a `runs/` folder.
8. **Fully customize the Chainlit UI** — theme, colors, logos, sidebar, etc.
9. Add **starter templates** for different chat modes (e.g., greeting, math demo).
10. The chatbot must include and use **at least one tool** (e.g., a calculator or similar).

---

## 📦 **Expected Project Structure**

```
chainlit-agent-assignment/
├─ pyproject.toml
├─ README.md
├─ .gitignore
├─ .env.example
├─ runs/
├─ src/
│  ├─ agent_core/
│  └─ chat_ui/
└─ scripts/
```

---

## 🔐 **Security Rules**

- **Do not hardcode any API keys** or secrets.
- All keys must be stored in a `.env` file.
- The `.env.example` file should only show variable names (no values).
- The real `.env` file must be **ignored via `.gitignore`**.
- Before submitting, double-check your repository to ensure no secrets are exposed.

---

## 🧾 **Submission Instructions**

1. Push your complete assignment to **GitHub** as a public repository.
2. The **README.md** file must include:

   - A short **description** of your chatbot.
   - **Steps** to set up and run your project.
   - A **browser screenshot** showing your chatbot running in Chainlit.

3. Submit the **GitHub repository URL** as your official submission.

---

## ⚠️ **Important Notes**

- **Do not copy or reuse code** from previous classrooms or assignments.
  All submissions will be checked for originality.
- **Those who fail to submit this assignment** will be **removed from the Google Classroom**.
- **Students who complete this assignment** must **present their project in class**.
- Your presentation should include:

  - A short walkthrough of your chatbot.
  - A demo showing streaming and tool usage.
  - A brief explanation of your code organization and UI customization.

---

## ✅ **Grading Rubric (100%)**

| Criteria               | Description                                                   | Weight |
| ---------------------- | ------------------------------------------------------------- | ------ |
| **Project Structure**  | Proper packaged app layout with separate agent and UI modules | 20%    |
| **Functional Chatbot** | Runs successfully with `uv run chatbot`                       | 25%    |
| **Streaming Output**   | Responses stream in real time                                 | 15%    |
| **Tool Integration**   | Working tool used in chat                                     | 10%    |
| **History Storage**    | Chat transcript saved in JSON                                 | 10%    |
| **UI Customization**   | Non-default design, colors, and logo                          | 10%    |
| **Secrets Management** | `.env` used correctly, no keys leaked                         | 5%     |
| **Documentation**      | README includes setup guide + screenshot                      | 5%     |

**Total: 100%**

---

## 💡 **Additional Tips**

- Test your chatbot thoroughly before submission.
- Ensure the streamed messages appear gradually in the browser.
- Confirm that every chat session generates a new JSON file in `runs/`.
- Double-check your `.gitignore` to prevent committing sensitive files.
- Use clear commit messages and maintain a professional Git history.

---
