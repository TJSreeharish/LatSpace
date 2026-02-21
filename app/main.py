from fastapi import FastAPI, UploadFile, File
from app.services.excel_streamer import process_excel

app = FastAPI()

@app.post("/parse")
async def parse_excel(file: UploadFile = File(...)):
    result = await process_excel(file)
    return result