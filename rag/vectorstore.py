# 向量数据库的构建与加载（FAISS）

import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from config import VECTOR_DB_PATH, OPENAI_API_KEY, OPENAI_BASE_URL, EMBEDDING_MODEL_NAME


def build_vectorstore(chunks, vector_db_path="vectorstore/faiss_index"):
    """
    将切分好的文档 chunks 构建为 FAISS 向量数据库，并保存到本地指定路径。

    参数：
    - chunks: list[Document] 已切分的文档块
    - vector_db_path: str 向量库保存路径，默认 'vectorstore/faiss_index'

    返回：
    - vs: FAISS 向量库对象
    """
    # 1. 创建 Embeddings 对象
    embeddings = OpenAIEmbeddings(
        model=EMBEDDING_MODEL_NAME,  # 使用配置的嵌入模型
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_BASE_URL
    )

    # 2. 构建 FAISS 向量库
    vs = FAISS.from_documents(chunks, embeddings)

    # 3. 确保保存目录存在
    os.makedirs(vector_db_path, exist_ok=True)

    # 4. 保存向量库到本地
    vs.save_local(vector_db_path)
    print(f"[VectorStore] 向量库已保存到：{vector_db_path}")

    return vs


def load_vectorstore():
    """加载已经存在的 FAISS 向量数据库"""
    embeddings = OpenAIEmbeddings(
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_BASE_URL
    )
    return FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True  # 允许从本地加载
    )
