# Intake Agent: 决定用户的请求属于哪种类型
# 职责是任务分解（适配复杂问题）


from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME

# 使用 deterministic LLM 确保输出是固定的关键词
llm = ChatOpenAI(
    temperature=0,
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    model_name=MODEL_NAME
)


def intake_decision(question):
    """
    输入：用户问题
    输出：use_rag / reason / chitchat
    """
    prompt = f"""
你是 Intake Agent，请判断用户需求：

 - 若需要查询知识库 → 输出 use_rag
 - 若需要推理分析 → 输出 reason
 - 若为闲聊 → 输出 chitchat

 注意！！！只输出上述关键词，不要输出其他任何内容。
 用户问题：{question}
"""
    return llm.predict(prompt).strip()
