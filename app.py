from fastapi import FastAPI, UploadFile
import shutil
from pipeline import process

app=FastAPI()

@app.post("/analyze")
async def analyze(file:UploadFile):
    input_path=f"uploads/{file.filename}"
    with open(input_path,"wb") as f:
        shutil.copyfileobj(file.file,f)
    return process(input_path)
