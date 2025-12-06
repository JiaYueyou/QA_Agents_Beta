# 主调度器：依次调用 Intake → Retrieval → Reasoning → Validation → Output

from agents.intake_agent import intake_decision
from agents.retrieval_agent import run_retrieval
from agents.reasoning_agent import run_reasoning
from agents.validation_agent import validate_answer
from agents.output_agent import optimize_output


def multi_agent_answer(question):
    """
    多 Agent 协作流程核心逻辑
    """
    print("\n[1] Intake Agent 判断用户问题类型...")
    decision = intake_decision(question)

    # 若需要检索，则调用 Retrieval Agent
    context = ""
    if decision == "use_rag":
        print("[2] Retrieval Agent 检索知识库中...")
        context = run_retrieval(question)

    # Reasoning Agent 合成最终回答
    print("[3] Reasoning Agent 推理中...")
    answer = run_reasoning(context, question)

    # 校验答案
    print("[4] Validation Agent 校验中...")
    validation = validate_answer(answer, context)

    # 若不通过，加入警告
    if validation != "VALID":
        answer += f"\n\n[校验提示]\n{validation}"

    # 最后优化输出
    print("[5] Output Agent 输出中...")
    return optimize_output(answer)


# REPL 模式
if __name__ == "__main__":
    while True:
        q = input("\n请输入你的问题：")
        print("\n=== 最终回答 ===")
        print(multi_agent_answer(q))
