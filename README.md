# News-research-tool
A Streamlit-based research assistant that lets users fetch, embed, and query news articles or web pages using LangChain, FAISS vector search, and Google Generative AI embeddings. This tool is designed to help researchers, students, and professionals quickly extract insights and answer questions from multiple online sources.

🚀 Features
🔗 URL Loader – Extracts text content from online news/articles.
🧩 Text Splitting – Uses RecursiveCharacterTextSplitter for efficient chunking.
🧠 Semantic Search – FAISS-powered vector store for fast similarity search.
🤖 Google GenAI Embeddings – High-quality embeddings for contextual search.
❓ Question Answering – Ask natural language questions about ingested news sources.
🎨 Streamlit UI – Simple, interactive, and user-friendly interface.

🛠️ Tech Stack
Python 3.11+
Streamlit – Interactive front-end
LangChain – Chains for retrieval and Q&A
FAISS – Vector database for semantic search
Google Generative AI – Embeddings & LLM integration
dotenv – Environment variable management

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows


Install dependencies:

pip install -r requirements.txt


Set up your environment variables in a .env file:

GOOGLE_API_KEY=your_google_genai_api_key

▶️ Usage

Run the Streamlit app:
streamlit run main.py


Steps:
->Enter one or more URLs of news sources.
->The tool scrapes and embeds the articles.
->Ask any question about the ingested news.
->Get concise answers with sources.

📁 Project Structure
📂 news-research-tool
│── main.py                 # Streamlit app entry point
│── requirements.txt        # Dependencies
│── .env                    # API keys (not to be shared)
│── vectorstore.pkl         # Saved FAISS index (generated at runtime)
│── README.md               # Project documentation

🔮 Future Improvements
🌍 Multi-language support
📊 Visual summaries (charts & graphs)
📱 Deploy on Streamlit Cloud / Hugging Face Spaces
📝 Export research notes as PDF/Docx


🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.
