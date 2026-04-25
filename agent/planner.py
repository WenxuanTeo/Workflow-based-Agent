def plan(query):
    if "股价" in query:
        return ["search_news", "analyze", "summarize"]
    return ["search", "summarize"]
