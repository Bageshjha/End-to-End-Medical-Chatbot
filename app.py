from flask import Flask, render_template, jsonify, request
from pinecone import Pinecone  
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.llms import CTransformers
from dotenv import load_dotenv
from src.prompt import *
import os
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

load_dotenv()

Pinecone_API_Key = os.environ.get("Pinecone_API_Key")

# Updated to use HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Initializing Pinecone
pc = Pinecone(api_key=Pinecone_API_Key)

index_name = "medibot"

# Check if the index exists and create it if necessary
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  
        metric='euclidean'
    )

# Loading the index
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

llm = CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_K_S.bin",
    model_type="llama",
    config={
        'max_new_tokens': 256,
        'temperature': 0.5
    }
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/") 
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"]) 
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print(response["answer"])
    return str(response["answer"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
