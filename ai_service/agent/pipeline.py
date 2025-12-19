from agent.intent_classifier import classify_intent
from agent.shopifyql_builder import build_shopifyql
from agent.executor import execute_query
from agent.explainer import explain

def run_agent(question, store_id):
    intent = classify_intent(question)
    query = build_shopifyql(intent, question)
    data = execute_query(query, store_id)
    answer = explain(data, intent)

    return {
        "answer": answer,
        "confidence": "medium"
    }
