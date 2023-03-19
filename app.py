from fastapi import FastAPI
from pydantic import BaseModel
import tiktoken

app = FastAPI()
enc = tiktoken.get_encoding("cl100k_base")

class EncodeRequest(BaseModel):
    text: str

class DecodeRequest(BaseModel):
    encoded_text: list

@app.post('/encode')
async def encode(request: EncodeRequest):
    encoded_text = enc.encode(request.text)
    return {"encoded_text": encoded_text}

@app.post('/decode')
async def decode(request: DecodeRequest):
    decoded_text = enc.decode(request.encoded_text)
    return {"decoded_text": decoded_text}

