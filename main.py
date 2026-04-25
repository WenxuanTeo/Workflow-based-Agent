from agent.planner import plan
from agent.executor import execute
from agent.workflow import run_workflow
from agent.memory import Memory


def main():
    query = "分析股价走势"

    steps = plan(query)

    memory = Memory()

    results = run_workflow(steps, execute, memory)

    print("最终结果：", results[-1])


if __name__ == "__main__":
    main()
