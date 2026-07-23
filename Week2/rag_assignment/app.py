import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ----------------------------
# LangChain Imports
# ----------------------------
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)
from langchain_classic.chains.retrieval import (
    create_retrieval_chain,
)

# =======================================================
# Streamlit Configuration
# =======================================================

st.set_page_config(
    page_title="PDF Question Answering",
    page_icon="📘",
    layout="wide",
)

st.title("📘 PDF Question Answering using LangChain + FAISS")

# =======================================================
# Tabs
# =======================================================

tab1, tab2 = st.tabs(
    [
        "📄 Create Embeddings",
        "💬 Ask Questions",
    ]
)

# =======================================================
# TAB 1
# =======================================================

with tab1:

    st.subheader("Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"],
    )

    save_folder = st.text_input(
        "Folder to save FAISS Index",
        value="faiss_index",
    )

    if st.button("Create Embeddings"):

        # Validate upload
        if uploaded_file is None:
            st.error("Please upload a PDF.")
            st.stop()

        if uploaded_file.type != "application/pdf":
            st.error("Only PDF files are allowed.")
            st.stop()

        os.makedirs(save_folder, exist_ok=True)

        # Save uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf",
        ) as temp_pdf:

            temp_pdf.write(uploaded_file.read())
            temp_path = temp_pdf.name

        # Load PDF
        with st.spinner("Reading PDF..."):

            loader = PyPDFLoader(temp_path)
            documents = loader.load()

        # Split document
        with st.spinner("Splitting into chunks..."):

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
            )

            chunks = splitter.split_documents(documents)

        # Embeddings
        with st.spinner("Generating embeddings..."):

            embeddings = OpenAIEmbeddings(
                model="text-embedding-3-small"
            )

            vectorstore = FAISS.from_documents(
                chunks,
                embeddings,
            )

        # Save FAISS locally
        vectorstore.save_local(save_folder)

        st.success("✅ PDF embedded successfully.")

        st.info(
            f"Embeddings saved in:\n\n{save_folder}"
        )

        st.code(
            f"""
{save_folder}
│
├── index.faiss
└── index.pkl
"""
        )

# =======================================================
# TAB 2
# =======================================================

with tab2:

    st.subheader("Ask Questions")

    folder = st.text_input(
        "FAISS Folder",
        value="faiss_index",
    )

    question = st.text_area(
        "Enter your question"
    )

    if st.button("Ask AI"):

        if not os.path.exists(folder):

            st.error("FAISS folder not found.")

            st.stop()

        # Load embeddings
        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )

        vectorstore = FAISS.load_local(
            folder,
            embeddings,
            allow_dangerous_deserialization=True,
        )

        retriever = vectorstore.as_retriever(
            search_kwargs={
                "k": 4
            }
        )

        # LLM
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
        )

        # Prompt
        prompt = ChatPromptTemplate.from_template(
            """
You are an intelligent assistant.

Answer ONLY from the supplied context.

If the answer is not available in the context,
reply:

"I couldn't find that information in the document."

Context:
{context}

Question:
{input}
"""
        )

        # Create document chain
        document_chain = create_stuff_documents_chain(
            llm,
            prompt,
        )

        # Create retrieval chain
        retrieval_chain = create_retrieval_chain(
            retriever,
            document_chain,
        )

        placeholder = st.empty()

        answer = ""

        with st.spinner("Thinking..."):

            for chunk in retrieval_chain.stream(
                {
                    "input": question
                }
            ):

                if "answer" in chunk:

                    answer += chunk["answer"]

                    placeholder.markdown(answer)

        # Show references
        response = retrieval_chain.invoke(
            {
                "input": question
            }
        )

        st.divider()

        st.subheader("Reference Pages")

        docs = response.get("context", [])

        pages = []

        for doc in docs:

            page = doc.metadata.get("page")

            if page is not None:

                pages.append(page + 1)

        if pages:

            pages = sorted(list(set(pages)))

            st.success(
                "Answer generated from page(s): "
                + ", ".join(map(str, pages))
            )

        else:

            st.info("No page information available.")