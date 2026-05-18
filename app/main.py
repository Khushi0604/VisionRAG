from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.rag_pipeline import process_uploaded_file, query_rag

app = FastAPI(title="VisionRAG")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "VisionRAG API Running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    result = await process_uploaded_file(file)
    return result

@app.post("/query")
async def query_system(query: str):
    response = query_rag(query)
    return response