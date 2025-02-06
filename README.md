**Custom Chatbot Using Langchain, FAISS, and Google Gemini AI**  

**1. Data Extraction**  
- Extracts text data from a webpage using `UnstructuredURLLoader`.  
- Splits extracted text into smaller chunks using `CharacterTextSplitter` for efficient processing.  

**2. Creating Vector Embeddings**  
- Uses **GoogleGenerativeAIEmbeddings** to convert text chunks into numerical vectors.  
- These embeddings enable similarity searches based on user queries.  

**3. Storing Data in FAISS Vector Store**  
- Stores the generated embeddings in **FAISS (Facebook AI Similarity Search)** for efficient retrieval.  
- Saves the FAISS index locally to avoid recomputing embeddings repeatedly.  

**4. Flask API Integration**  
- Implements a **Flask RESTful API** to handle user queries.  
- Receives queries via a `/query` endpoint, retrieves relevant results, and returns responses.  

**5. Query Processing & Similarity Search**  
- When a user submits a query, the chatbot performs a **similarity search** in the FAISS vector store.  
- Returns the most relevant response based on stored knowledge.  

**6. Technology Stack Used**  
- **Langchain** – Handles document loading and text processing.  
- **Google Gemini AI** – Generates vector embeddings.  
- **FAISS** – Stores and retrieves embeddings for similarity searches.  
- **Flask** – Provides a RESTful API for interaction.  

**Outcome**: A fast, efficient chatbot capable of retrieving relevant information using **vector search** and **AI-powered embeddings**.
