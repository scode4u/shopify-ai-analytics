def explain(data, intent):
    if intent == "sales":
        top = data[0]
        return f"Your top-selling product last week was {top['product']} with {top['total_sold']} units sold."
    return "Not enough data to generate insights."
