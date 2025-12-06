# build_faiss.py
"""
一条龙脚本：
1. 加载 data/ 目录中的各种文档
2. 切分文档
3. 构建 FAISS 向量库并保存到本地
"""

from rag.loader import load_documents
from rag.splitter import split_documents
from rag.vectorstore import build_vectorstore
from config import VECTOR_DB_PATH


def build_faiss_database(data_path="./data", vector_db_path=VECTOR_DB_PATH):
    """
    构建 FAISS 向量库
    参数:
        data_path: 文档目录
        vector_db_path: 向量库保存路径
    返回:
        vs: 构建完成的 FAISS 向量库对象
    """
    print("[Step 1] 加载文档...")
    docs = load_documents(data_path)

    print("[Step 2] 文本切分...")
    chunks = split_documents(docs)

    print("[Step 3] 构建 FAISS 向量库...")
    vs = build_vectorstore(chunks, vector_db_path)

    print("[Done] FAISS 向量库构建完成")
    return vs


if __name__ == "__main__":
    # 脚本模式直接执行即可
    build_faiss_database()
