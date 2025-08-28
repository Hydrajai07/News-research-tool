import os
import streamlit as st
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
import asyncio

load_dotenv()

st.title("News Research Tool")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url = st.sidebar.button("Process URL")
vector_store_path = "faiss_index"

main_placeholder = st.empty()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Function to get or create an event loop to avoid embedding error
def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()

if process_url:
    # Set the event loop before any async-related calls
    get_or_create_eventloop()

    # Loading data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading Started...")
    data = loader.load()

    # Splitting data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n', '\n\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitting Started...")
    docs = text_splitter.split_documents(data)

    # Creating embeddings and saving as a FAISS index
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding vector started building ...")
    time.sleep(2)

    # Save FAISS index using the correct method
    vectorstore.save_local(vector_store_path)
    main_placeholder.success("Vectorstore saved successfully!")

# Load the vector store if it exists
loaded_vectorstore = None
if os.path.exists(vector_store_path):
    with st.spinner("Loading vector store..."):
        # Set event loop for the loading process as well
        get_or_create_eventloop()
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        loaded_vectorstore = FAISS.load_local(
            vector_store_path,
            embeddings,
            allow_dangerous_deserialization=True
        )
    st.sidebar.success("Vector store loaded!")
else:
    st.sidebar.warning("Vector store not found. Please process URLs first.")

query = st.text_input("Question:")
if query and loaded_vectorstore:
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=loaded_vectorstore.as_retriever())
    result = chain.invoke({"question": query})

    st.header("Answer")
    st.write(result["answer"])

    sources = result.get("sources", "")
    if sources:
        st.subheader("Sources")
        st.markdown(sources)