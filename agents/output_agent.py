# Output Agent: 负责将回答格式化，变成专业企业风格

from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME

llm = ChatOpenAI(
    temperature=0,
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    model_name=MODEL_NAME
)


def optimize_output(answer):
    """
    对最终答案做格式化美化
    """
    prompt = f"""
你是 Output Agent，请将以下内容整理为：清晰、专业、有结构、企业可直接展示的回答。

内容：
{answer}
"""
    return llm.predict(prompt)
