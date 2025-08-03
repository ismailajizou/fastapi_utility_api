from pydantic import BaseModel


class DownloadRequestBody(BaseModel):
    link: str