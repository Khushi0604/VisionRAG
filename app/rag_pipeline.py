import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.extractor import (
    extract_pdf_text,
    extract_pdf_images,
    extract_docx_text,
    extract_csv_text,
    extract_image_text
)
from app.ocr import perform_ocr
from app.vision import analyze_image
from app.embeddings import generate_embedding
from app.vector_store import store_embeddings, search_embeddings
from app.web_search import perform_web_search
from app.orchestrator import classify_query
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

UPLOAD_DIR = "uploads"

async def process_uploaded_file(file):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = ""
    image_analysis = []

    if file.filename.endswith(".pdf"):
        text = extract_pdf_text(file_path)

        images = extract_pdf_images(file_path)

        for image in images:
            ocr_text = perform_ocr(image)
            vision_text = analyze_image(image)

            image_analysis.append({
                "image": image,
                "ocr": ocr_text,
                "vision": vision_text
            })

            text += "\n" + ocr_text
            text += "\n" + vision_text

    elif file.filename.endswith(".docx"):
        text = extract_docx_text(file_path)

    elif file.filename.endswith(".csv"):
        text = extract_csv_text(file_path)

    elif file.filename.endswith((".png", ".jpg", ".jpeg")):
        text = extract_image_text(file_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    embeddings = generate_embedding(chunks)

    store_embeddings(embeddings, chunks)

    return {
        "message": "File processed successfully",
        "chunks": len(chunks),
        "image_analysis": image_analysis
    }



def query_rag(query):
    query_type = classify_query(query)

    query_embedding = generate_embedding([query])[0]

    retrieved_chunks = search_embeddings(query_embedding)

    context = "\n".join(retrieved_chunks)

    web_results = ""

    if query_type == "web_search":
        web_data = perform_web_search(query)
        web_results = str(web_data)

    final_prompt = f"""
    Answer the query using the provided context.

    Query:
    {query}

    Document Context:
    {context}

    Web Results:
    {web_results}

    Include citations wherever possible.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    return {
        "query": query,
        "response": response.choices[0].message.content,
        "citations": [
            "Uploaded Documents",
            "Web Search Results"
        ]
    }