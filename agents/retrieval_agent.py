# Retrieval Agent: 负责查询知识库
# 使用 ReAct 智能 tool 调用能力


from langchain.agents import Tool, initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from tools.rag_tool import create_rag_tool
from config import OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME


# LLM 用于工具选择 + 思考过程
llm = ChatOpenAI(
    temperature=0,
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    model_name=MODEL_NAME
)


# 加载 RAG 工具
qa_chain = create_rag_tool()


def rag_tool_wrapper(question: str):
    """
    统一接口：输入问题，返回 answer
    同时保留 source_document 以便调试
    """
    outputs = qa_chain.invoke({"query": question})
    answer = outputs.get("result", "")
    sources = outputs.get("sources_documents", [])
    return {"answer": answer, "sources": sources}


# 定义工具列表
tools = [
    Tool(
        name="knowledge_rag",
        func=rag_tool_wrapper,
        description="用于查询公司知识库内容"
    )
]

# 初始化 ReAct Agent
retrieval_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # 经典 ReAct
    verbose=True
)


def run_retrieval(question):
    """
    输入：用户问题
    输出：RAG 查询结果
    """
    outputs = retrieval_agent.invoke({"input": question})
    answer = outputs.get("output", "")
    return answer
