def classify_intent(question: str):
    q = question.lower()
    if "inventory" in q or "stock" in q:
        return "inventory"
    if "sell" in q or "sales" in q:
        return "sales"
    if "customer" in q:
        return "customers"
    return "unknown"
