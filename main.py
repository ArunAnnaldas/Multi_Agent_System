from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks import get_openai_callback


llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo",
	openai_api_key="")

# Step 1: Planner Agent
def planner_agent(task):
    messages = [
        SystemMessage(content="You are a senior software architect. Your job is to break down coding tasks into implementation steps."),
        HumanMessage(content=f"Task: {task}")
    ]
    response = llm(messages).content
    return response

# Step 2: Coder Agent
def coder_agent(instruction):
    messages = [
        SystemMessage(content="You are an expert Python developer. Write clean and readable Python code based on the instructions."),
        HumanMessage(content=instruction)
    ]
    response = llm(messages).content
    return response

# Step 3: Critic Agent
def critic_agent(code):
    messages = [
        SystemMessage(content="You are a code reviewer. Review the following Python function for correctness and suggest improvements."),
        HumanMessage(content=f"Code:\n{code}")
    ]
    response = llm(messages).content
    return response

# 🔁 Orchestration (Coordinator)
def run_multi_agent_system(user_request):
    print("📌 User Request:", user_request)
    
    print("\n🔧 Step 1: Planning the task...")
    plan = planner_agent(user_request)
    print(plan)

    print("\n💻 Step 2: Generating code...")
    code = coder_agent(plan)
    print(code)

    print("\n🧐 Step 3: Reviewing code...")
    review = critic_agent(code)
    print(review)

# 🔍 Try it
if __name__ == "__main__":
    user_prompt = "Write a function to check if a number is prime"
    with get_openai_callback() as cb:
        run_multi_agent_system(user_prompt)
        print("\n📊 Token Usage Summary:")
        print(cb)