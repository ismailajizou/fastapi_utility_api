from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

from app.lib import download

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI + uv!"}


@app.post('/download')
def download_file(link: str, format: str):
    if format not in ["mp4", "mp3"]:
        return JSONResponse(content={"message": "Invalid format"}, status_code=400)

    result = download.download(link, f"public/output.{format}")

    mimetype = "video/mp4" if format == "mp4" else "audio/mpeg"
    if result:
        return FileResponse(f"public/output.{format}", media_type=mimetype)

    return JSONResponse(content={"message": "Download failed"}, status_code=500)
