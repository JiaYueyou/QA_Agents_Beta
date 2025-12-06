# 将文档切分成多个 chunk 以便更好地构建向量库


from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents(docs):
    """
    输入：Document 对象列表
    输出：切分后的 Document chunk 列表
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,  # 默认设置500
        chunk_overlap=CHUNK_OVERLAP  # 默认设置50
    )

    # 自动完成切分
    chunks = splitter.split_documents(docs)
    print(f"[Splitter] Generated {len(chunks)} chunks")
    return chunks
