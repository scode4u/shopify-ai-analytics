def build_shopifyql(intent, question):
    if intent == "sales":
        return """
        SELECT product_title, SUM(quantity) as total_sold
        FROM orders
        WHERE created_at >= -7d
        GROUP BY product_title
        ORDER BY total_sold DESC
        LIMIT 5
        """
    return ""
