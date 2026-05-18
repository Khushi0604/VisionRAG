# VisionRAG

Advanced Multimodal Retrieval-Augmented Generation (RAG) System with OCR, Embedded Image Understanding, Real-Time Web Search, and Intelligent File Generation.

---

## Features

- Multimodal document ingestion
- PDF text extraction
- OCR support for scanned documents
- Embedded image extraction from PDFs
- Semantic chunking and embedding generation
- Vector similarity search using FAISS
- Real-time web search integration
- Intelligent response generation using Groq LLM
- Citation-aware responses
- DOCX and PDF report generation
- Streamlit frontend interface
- FastAPI backend architecture

---

## Supported File Types

- PDF
- DOCX
- CSV
- PNG
- JPG / JPEG
- Scanned PDFs

---

## Tech Stack

### Backend
- FastAPI
- Python

### Frontend
- Streamlit

### AI / ML
- Sentence Transformers
- Groq API
- EasyOCR
- Tesseract OCR

### Vector Database
- FAISS

### Document Processing
- PyMuPDF
- pdfplumber
- python-docx

### Search
- Tavily API

---

## System Architecture

User Upload
    ↓
File Extraction Layer
    ↓
OCR + Vision Analysis
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
FAISS Vector Database
    ↓
Semantic Retrieval
    ↓
Groq LLM Response Generation
    ↓
Response + Citations + File Generation

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Khushi0604/VisionRAG.git
cd VisionRAG
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

---

## Run Frontend

```bash
streamlit run frontend/streamlit_app.py
```

---

## Sample Queries

- Summarize the uploaded PDF
- Extract text from the scanned invoice
- Analyze the uploaded chart image
- Generate a report from uploaded documents
- Fetch latest AI news related to RAG systems

---

## Folder Structure

```text
VisionRAG/
│
├── app/
├── frontend/
├── uploads/
├── datasets/
├── screenshots/
├── demo_videos/
├── generated_files/
├── requirements.txt
├── README.md
├── .env.example
└── run.py
```

---

## Future Improvements

- Video understanding support
- Hybrid vector databases
- User authentication
- Multi-agent orchestration
- Cloud deployment

---

## Author

Khushi Nanwani
