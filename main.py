
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FF PANEL SUPPORT API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {
        "status": "online",
        "message": "FF PANEL SUPPORT API is running"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/api/tickets")
async def get_tickets():
    return {
        "success": True,
        "tickets": []
    }
