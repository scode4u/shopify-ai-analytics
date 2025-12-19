from fastapi import FastAPI
from agent.pipeline import run_agent

app = FastAPI()

@app.post("/ask")
def ask(payload: dict):
    return run_agent(payload["question"], payload["store_id"])
