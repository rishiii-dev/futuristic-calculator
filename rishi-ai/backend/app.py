import os
from pathlib import Path
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:4b")
FRONTEND_PATH = Path(__file__).resolve().parent.parent / "frontend" / "index.html"

app = FastAPI(title="Rishi AI")


class ChatRequest(BaseModel):
    message: str


@app.get("/api/health")
async def health() -> dict[str, Any]:
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(f"{OLLAMA_BASE_URL}/api/tags")
            response.raise_for_status()
        return {"status": "ok", "ollama": True, "model": OLLAMA_MODEL}
    except Exception as exc:
        return {"status": "degraded", "ollama": False, "model": OLLAMA_MODEL, "error": str(exc)}


@app.post("/api/chat")
async def chat(request: ChatRequest) -> dict[str, str]:
    message = request.message.strip()
    if not message:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    payload = {
        "model": OLLAMA_MODEL,
        "stream": False,
        "messages": [
            {
                "role": "system",
                "content": "You are Rishi AI, a helpful private local assistant. Be concise, accurate, friendly, and practical."
            },
            {"role": "user", "content": message},
        ],
    }

    try:
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.post(f"{OLLAMA_BASE_URL}/api/chat", json=payload)
            response.raise_for_status()
            data = response.json()
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=502, detail=f"Ollama request failed: {exc}") from exc

    return {"response": data.get("message", {}).get("content", "")}


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(FRONTEND_PATH)
