# Reasoning Agent: 负责将检索内容 + 用户问题进行逻辑整合


from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME

llm = ChatOpenAI(
    temperature=0,
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    model_name=MODEL_NAME
)


def run_reasoning(context, question):
    """
    context: Retrieval Agent 的原始检索结果
    question: 用户问题
    """
    prompt = f"""
你是 Reasoning Agent，要根据检索内容进行逻辑推理和整合。

检索内容如下（可能为空）：
{context}

用户问题：
{question}

请生成最终的综合推理回复。
如果你不能完全确定答案，请明确指出“不确定”部分。
"""
    return llm.predict(prompt)
