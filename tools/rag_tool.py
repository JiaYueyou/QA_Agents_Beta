# 用于构建一个可以被 Agent 调用的 RAG 工具
# 该处使用了 LangChain 的 RetrievalQA 链来实现 RAG 功能


from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from rag.vectorstore import load_vectorstore
from config import OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME


def create_rag_tool():
    """返回一个 QA Chain 作为 RAG 工具，供 Agent 使用"""
    llm = ChatOpenAI(
        temperature=0,
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_BASE_URL,
        model_name=MODEL_NAME
    )

    # 加载向量数据库
    vectorstore = load_vectorstore()

    # 转换成可检索对象
    retriever = vectorstore.as_retriever()

    # 构建 RetrievalQA 链（LCEL兼容）
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True  # 返回引用来源
    )

    return qa_chain
