from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from ai_service import generate_summary
from email_service import send_email

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...), email: str = Form(...)):

    try:
        df = pd.read_csv(file.file)

        summary = generate_summary(df)

        send_email(email, summary)

        return {"message": "Summary sent successfully"}

    except Exception as e:
        print("ERROR OCCURRED:", e)
        return {"error": str(e)}