import os
import subprocess
import tempfile
import uuid
import requests
import urllib.parse
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse

from app.dto.main import DownloadRequestBody
# from app.lib import download
import yt_dlp
import json


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI + uv!"}


@app.post('/download/audio')
async def download_audio(request: DownloadRequestBody):
    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        filename = f"{uuid.uuid4()}.mp3"
        output_path = os.path.join(temp_dir, filename)

        # Download the video using yt-dlp
        result = subprocess.run(
            ["yt-dlp", "-f", "bestaudio", "-o", output_path, request.link],
            capture_output=True,
            text=True
        )

        if result.returncode != 0 or not os.path.exists(output_path):
            raise HTTPException(status_code=400, detail=f"yt-dlp failed: {result.stderr.strip()}")

        # Send the file as a response
        return FileResponse(
            path=output_path,
            media_type="audio/mp3",
            filename=os.path.basename(output_path),
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post('/download/video')
async def download_video(request: DownloadRequestBody):
    
    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        filename = f"{uuid.uuid4()}.mp4"
        output_path = os.path.join(temp_dir, filename)

        # Download the video using yt-dlp
        result = subprocess.run(
            ["yt-dlp", "-f", "best", "-o", output_path, request.link],
            capture_output=True,
            text=True
        )

        if result.returncode != 0 or not os.path.exists(output_path):
            raise HTTPException(status_code=400, detail=f"yt-dlp failed: {result.stderr.strip()}")

        # Send the file as a response
        return FileResponse(
            path=output_path,
            media_type="video/mp4",
            filename=os.path.basename(output_path),
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))