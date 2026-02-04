from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Installation Task API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Installation Task Management API", "version": "0.1"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [
            {"id": 1, "title": "Deploy Kubernetes", "status": "pending"},
            {"id": 2, "title": "Setup Vault", "status": "pending"},
            {"id": 3, "title": "Configure Monitoring", "status": "pending"}
        ]
    }
