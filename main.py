# File: main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

# Create FastAPI instance
app = FastAPI(title="Number Classification API", version="1.0")

# CORS Handling
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_methods=["GET"],  # Allow only GET requests
    allow_headers=["*"]  # Allow all headers
)

# Include API routes
app.include_router(router)
