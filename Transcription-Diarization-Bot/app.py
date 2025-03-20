from fastapi import FastAPI, UploadFile, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import whisper
from pyannote.audio import Pipeline
import torch
import os
import requests
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
#uvicorn app:app --reload
# API Configuration
GEMINI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxx"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

# Templates Directory
templates = Jinja2Templates(directory="templates")

# Load Models
whisper_model = whisper.load_model("base")
pipeline_path = "diarization_model/pipeline.pkl"
pipeline = torch.load(pipeline_path)
pipeline.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))

# Upload Directory
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@app.get("/transcribe", response_class=HTMLResponse)
async def transcribe_page(request: Request):
    return templates.TemplateResponse("transcribe.html", {"request": request})


@app.get("/diarize", response_class=HTMLResponse)
async def diarize_page(request: Request):
    return templates.TemplateResponse("diarize.html", {"request": request})


@app.get("/chatnote", response_class=HTMLResponse)
async def chatnote_page(request: Request):
    return templates.TemplateResponse("chatnote.html", {"request": request})

@app.get("/index", response_class=HTMLResponse)
async def transcribe_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/explore", response_class=HTMLResponse)
async def transcribe_page(request: Request):
    return templates.TemplateResponse("explore.html", {"request": request})

@app.post("/transcribe")
async def transcribe_audio(audio: UploadFile, request: Request):
    try:
        filepath = os.path.join(UPLOAD_FOLDER, audio.filename)
        with open(filepath, "wb") as buffer:
            buffer.write(audio.file.read())

        # Transcription
        transcription_result = whisper_model.transcribe(filepath)
        transcription_text = transcription_result['text']

        return templates.TemplateResponse(
            "transcribe.html",
            {"request": request, "transcription": transcription_text},
        )
    except Exception as e:
        return HTMLResponse(content=f"<h1>Error:</h1> <pre>{str(e)}</pre>")


@app.post("/diarize")
async def diarize_audio(audio: UploadFile, request: Request):
    try:
        filepath = os.path.join(UPLOAD_FOLDER, audio.filename)
        with open(filepath, "wb") as buffer:
            buffer.write(audio.file.read())

        # Diarization and Transcription
        diarization_result = pipeline(filepath)
        transcription_result = whisper_model.transcribe(filepath)
        transcription_text = transcription_result['text']

        diarized_transcription = align_transcription(diarization_result, transcription_text)

        return templates.TemplateResponse(
            "diarize.html",
            {"request": request, "transcription_and_diarization": diarized_transcription},
        )
    except Exception as e:
        return HTMLResponse(content=f"<h1>Error:</h1> <pre>{str(e)}</pre>")


@app.post("/generate_chatnote")
async def generate_chatnote(audio: UploadFile, request: Request):
    try:
        filepath = os.path.join(UPLOAD_FOLDER, audio.filename)
        with open(filepath, "wb") as buffer:
            buffer.write(audio.file.read())

        # Diarization and Transcription
        diarization_result = pipeline(filepath)
        transcription_result = whisper_model.transcribe(filepath)
        transcription_text = transcription_result['text']

        diarized_transcription = align_transcription(diarization_result, transcription_text)

        # Gemini API Request
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f"""
                            You are a medical assistant AI. Below is a transcribed and diarized conversation.
                            Format the key medical information into structured SOAP notes. Use the following sections:\n
                            Chief Complaint: \n
                            HPI: \n
                            ROS: \n
                            PE: \n
                            Medications: \n
                            Past Medical History: \n
                            Social History: \n
                            Assessment: \n
                            Plan: \n

                            Conversation:\n
                            {diarized_transcription}
                            """
                        }
                    ]
                }
            ]
        }

        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            chatnote_result = response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "[No result from Gemini]")
        else:
            chatnote_result = f"[Error: {response.status_code}] {response.json().get('error', {}).get('message', 'Unknown error')}"

        return templates.TemplateResponse(
            "chatnote.html",
            {"request": request, "chatnote": chatnote_result},
        )
    except Exception as e:
        return HTMLResponse(content=f"<h1>Error:</h1> <pre>{str(e)}</pre>")


def align_transcription(diarization_result, transcription_text):
    output = []
    segments = transcription_text.split(". ")
    for segment, (start, end) in zip(segments, diarization_result.itersegments()):
        output.append(f"[{start:.2f}s - {end:.2f}s] {segment.strip()}")
    return "\n".join(output)
