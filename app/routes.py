# File: app/routes.py

from fastapi import APIRouter, HTTPException, Query
import requests
from app.utils import classify_number

router = APIRouter()

@router.get("/api/classify-number")
def classify_number_endpoint(number: str = Query(None, description="The number to classify")):
    """API endpoint to classify a number and fetch a fun fact."""
    try:
        # Ensure a number parameter is provided and valid
        if number is None or not number.lstrip("-").isdigit():
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
    except HTTPException as http_exc:
        raise http_exc  # Preserve 400 error for invalid input
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/health")
def health_check():
    """Health check endpoint to verify API status."""
    return {"status": "API is running"}

@router.get("/{full_path:path}")
def handle_invalid_routes(full_path: str):
    """Catch-all route to handle invalid paths and return an error response."""
    raise HTTPException(status_code=400, detail={"number": full_path, "error": True})
