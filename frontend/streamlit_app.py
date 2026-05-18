import streamlit as st
import requests

st.set_page_config(page_title="VisionRAG", layout="wide")

st.title("VisionRAG")
st.subheader("Advanced Multimodal RAG System")

if "uploaded" not in st.session_state:
    st.session_state.uploaded = False

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX, CSV, Images",
    type=["pdf", "docx", "csv", "png", "jpg", "jpeg"]
)

if uploaded_file is not None and not st.session_state.uploaded:

    with st.spinner("Uploading and processing file..."):

        response = requests.post(
            "http://127.0.0.1:8000/upload",
            files={
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }
        )

    if response.status_code == 200:

        st.session_state.uploaded = True

        data = response.json()

        st.success("File processed successfully!")

        st.write("### Processing Details")
        st.json(data)

    else:
        st.error(f"Upload failed: {response.text}")

query = st.text_input("Ask a question")

if st.button("Generate Response"):

    with st.spinner("Generating response..."):

        response = requests.post(
            "http://127.0.0.1:8000/query",
            params={"query": query}
        )

    if response.status_code == 200:

        result = response.json()

        st.write("## Response")
        st.write(result["response"])

        st.write("## Citations")

        for citation in result["citations"]:
            st.write(f"- {citation}")

    else:
        st.error(f"Query failed: {response.text}")