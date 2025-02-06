# File: app/routes.py

from fastapi import APIRouter, HTTPException, Query
import requests
from app.utils import classify_number

router = APIRouter()

@router.get("/api/classify-number")
def classify_number_endpoint(number: str = Query(..., description="The number to classify")):
    """API endpoint to classify a number and fetch a fun fact."""
    try:
        # Validate input (must be an integer)
        if not number.lstrip("-").isdigit():
            raise HTTPException(status_code=400, detail={"number": number, "error": True})
        
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/health")
def health_check():
    """Health check endpoint to verify API status."""
    return {"status": "API is running"}
