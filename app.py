from flask import Flask, request, jsonify
from langchain_community.vectorstores import FAISS
from langchain_google_genai import

app = Flask(__name__)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  

vectorStore_gemini = FAISS.load_local(
    "C:/Users/ayush/faiss_store_gemini",  
    embeddings,
    allow_dangerous_deserialization=True  
)

@app.route('/query', methods=['POST'])
def query_vector_store():
    user_input = request.json.get('query', '')  
    
    if not user_input:
        return jsonify({"error": "Query not provided"}), 400  
    
    
    result = vectorStore_gemini.similarity_search(user_input)  
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(debug=True)
