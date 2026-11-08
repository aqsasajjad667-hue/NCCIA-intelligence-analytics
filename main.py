import os
import json
from datetime import datetime
from google import genai
from google.genai import types

# Initialize Gemini Client using environment variable
gemini_client = genai.Client()

def extract_nccia_data(raw_text: str) -> dict:
    """Extracts structured metrics using Gemini API."""
    prompt = f"""
    Analyze the following official text/press release from NCCIA Pakistan 
    and extract daily intelligence metrics.
    
    If any metric is missing, set its value strictly to "Not Reported".

    Extract metrics:
    - Raids
    - Arrests
    - FIRs
    - Complaints
    - Cases Registered
    - Financial Recoveries
    - Cities Breakdown
    - Cybercrime Trends

    Text:
    {raw_text}
    """

    response = gemini_client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )
    )
    return json.loads(response.text)

if __name__ == "__main__":
    print(f"--- Running NCCIA Intelligence Agent [{datetime.now().strftime('%Y-%m-%d')}] ---")
    sample_raw_text = "NCCIA press update: Operations ongoing in Lahore and Karachi."
    extracted = extract_nccia_data(sample_raw_text)
    print("Extracted Data:", json.dumps(extracted, indent=2))
    sample_raw_text = "NCCIA press update: Operations ongoing in Lahore and Karachi."
    extracted = extract_nccia_data(sample_raw_text)
    print("Extracted Data:", json.dumps(extracted, indent=2))
    
