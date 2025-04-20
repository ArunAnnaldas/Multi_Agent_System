# 🤖 Agentic AI – Multi-Agent System (LangChain + OpenAI)

This project demonstrates a modular **multi-agent AI system** built using [LangChain](https://www.langchain.com/) and OpenAI's GPT models. It showcases how agents can collaborate toward a shared goal by simulating the behavior of a Planner, a Coder, and a Critic — just like a real-world development team.

---

## 🧩 Agent Roles

| Agent          | Description |
|----------------|-------------|
| 🧠 **Planner Agent** | Breaks down the user request into implementation steps |
| 💻 **Coder Agent**   | Generates Python code based on the Planner's steps |
| 🧐 **Critic Agent**  | Reviews the code and suggests improvements |

---

## 🎯 Use Case Example

**Input Prompt:**

Write a function to check if a number is prime



**System Output:**
1. Planner provides coding steps
2. Coder generates code
3. Critic reviews and suggests changes (in Module 3B: Reflexive loop)

---

## 🛠 Tech Stack

- Python 3.9+
- [LangChain](https://docs.langchain.com)
- [OpenAI GPT-3.5 Turbo](https://platform.openai.com)
- Callback tracking via `get_openai_callback`

---


---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install langchain openai


2. Set Your OpenAI API Key

export OPENAI_API_KEY="your-key-here"


3. Run the Program

python main.py

