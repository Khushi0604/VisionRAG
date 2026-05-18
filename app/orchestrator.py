def classify_query(query):
    query = query.lower()

    if "latest" in query or "current" in query:
        return "web_search"

    elif "report" in query or "generate" in query:
        return "file_generation"

    else:
        return "rag"