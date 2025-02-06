# File: app/routes.py

from fastapi import APIRouter, HTTPException, Query
import requests
from app.utils import classify_number

router = APIRouter()

@router.get("/api/classify-number")
def classify_number_endpoint(number: str = Query(None, description="The number to classify")):
    """API endpoint to classify a number and fetch a fun fact."""
    # Ensure a number parameter is provided and valid
    if number is None or not number.lstrip("-").isdigit():
        return {"number": number, "error": True}, 400
    
    number = int(number)
    result = classify_number(number)
    
    # Fetch fun fact from Numbers API
    fun_fact_url = f"http://numbersapi.com/{number}/math"
    response = requests.get(fun_fact_url)
    
    if response.status_code == 200:
        result["fun_fact"] = response.text
    else:
        result["fun_fact"] = "Fun fact not available."
    
    return result

@router.get("/api/health")
def health_check():
    """Health check endpoint to verify API status."""
    return {"status": "API is running"}

@router.get("/{full_path:path}")
def handle_invalid_routes(full_path: str):
    """Catch-all route to handle invalid paths and return an error response."""
    return {"number": full_path, "error": True}, 400
