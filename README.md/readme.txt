# AI-Powered Shopify Analytics Agent

## Overview
This project implements an AI-powered analytics service for Shopify stores that allows users to ask natural-language business questions (sales, inventory, customers). The system interprets the question, generates ShopifyQL, executes analytics queries, and returns insights in simple, business-friendly language.

The core focus is on **agentic reasoning, ShopifyQL generation, and API design**.

---

## Architecture

Client / API Consumer  
→ **Rails API Gateway (design-only)**  
→ **Python AI Service (FastAPI, implemented)**  
→ Shopify Analytics (mocked)

> Note: For the scope of this assignment, the Rails API is represented at the design level, while the Python AI agent is fully implemented and runnable.

---

## Implemented Components

### Python AI Service (FastAPI)
- Exposes a `/ask` endpoint
- Accepts natural language questions and store context
- Implements an agentic workflow:
  1. Intent classification (sales / inventory / customers)
  2. ShopifyQL query generation
  3. Query execution (mocked Shopify Analytics API)
  4. Business-friendly explanation of results

### Agent Design
- **Intent Understanding:** Identifies required data domain
- **Planning:** Chooses relevant Shopify tables and metrics
- **ShopifyQL Generation:** Produces syntactically valid queries
- **Execution:** Simulates Shopify Analytics responses
- **Explanation:** Converts metrics into clear business insights

---

## Example API Request

POST `/ask`

```json
{
  "store_id": "demo.myshopify.com",
  "question": "What were my top selling products last week?"
}
