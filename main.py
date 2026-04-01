from fastapi import FastAPI, UploadFile, File
from ecgtizer import ECGtizer
import pandas as pd
import shutil
import os

app = FastAPI()

@app.post("/digitize")
async def digitize_ecg(file: UploadFile = File(...)):
    # 1. Save the uploaded image locally
    with open("temp_ecg.png", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # 2. Run the AI Digitizer
    # We use 'fragmented' for 3x4 and 6x2 layouts
    digitizer = ECGtizer("temp_ecg.png", extraction_method="fragmented")
    
    # 3. Format the data into a list of numbers
    results = {}
    for lead_name, lead_data in digitizer.extracted_lead.items():
        results[lead_name] = lead_data.tolist()
    
    return {"status": "success", "data": results}
