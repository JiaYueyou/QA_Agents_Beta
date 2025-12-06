# Validation Agent: 负责审查回答是否有幻觉或逻辑错误


from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME

llm = ChatOpenAI(
    temperature=0,
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    model_name=MODEL_NAME
)


def validate_answer(answer, sources):
    """
    answer: Reasoning Agent 生成的最终回答
    sources: Retrieval Agent 提供的知识库内容
    """
    prompt = f"""你是 Validation Agent。

请检查以下回答是否存在：
- 无依据内容
- 逻辑错误
- 幻觉内容（hallucination）
- 与来源不一致的地方

回答：
{answer}

来源：
{sources}

如果没有任何问题，你必须只输出：VALID
否则逐条给出问题列表。
"""
    return llm.predict(prompt)