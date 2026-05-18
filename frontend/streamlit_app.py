import streamlit as st
import requests

st.title("VisionRAG")
st.subheader("Advanced Multimodal RAG System")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX, CSV, Images",
    type=["pdf", "docx", "csv", "png", "jpg", "jpeg"]
)

if uploaded_file:
    files = {
        "file": uploaded_file.getvalue()
    }

    response = requests.post(
        "http://127.0.0.1:8000/upload",
        files={
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue()
            )
        }
    )

    st.success(response.json()["message"])

query = st.text_input("Ask a question")

if st.button("Generate Response"):
    response = requests.post(
        "http://127.0.0.1:8000/query",
        params={"query": query}
    )

    result = response.json()

    st.write(result["response"])

    st.subheader("Citations")

    for citation in result["citations"]:
        st.write(f"- {citation}")