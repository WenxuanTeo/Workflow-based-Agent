from agent.tools import search, analyze, summarize

def execute(step, memory):
    if step == "search_news":
        result = search()
    elif step == "analyze":
        result = analyze(memory[-1])
    elif step == "summarize":
        result = summarize(memory[-1])
    else:
        result = "unknown"

    return result
