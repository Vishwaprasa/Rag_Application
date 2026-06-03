def format_docs(docs):
    return "\n\n".join([doc["text"] for doc in docs])


def truncate_text(text, max_length=1000):
    return text[:max_length]
