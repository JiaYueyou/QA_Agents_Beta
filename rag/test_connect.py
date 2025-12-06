# test_openai_api.py
"""
测试 OpenAI Embeddings API 是否可以成功连接
"""

from langchain_openai import OpenAIEmbeddings
from config import EMBEDDING_MODEL_NAME, OPENAI_API_KEY, OPENAI_BASE_URL
import os

# 2. 创建 Embeddings 对象
embeddings = OpenAIEmbeddings(
    model=EMBEDDING_MODEL_NAME,
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL
)

# 3. 测试生成向量
texts = ["这是一个测试文本", "第二条文本"]
try:
    vectors = embeddings.embed_documents(texts)
    print(f"成功生成向量，长度示例：{len(vectors[0])}")
except Exception as e:
    print(f"[Error] API 连接失败：{e}")
