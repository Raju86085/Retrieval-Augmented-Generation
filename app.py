import streamlit as st
import os
from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.core import ServiceContext, SimpleDirectoryReader, VectorStoreIndex


st.title('Retrieval-Augmented Generation')
query = "can you generate a questions from the book .do not generate all the questions based on one topic. generate from differnet topics. it should be in this template.  PART A : Generate a two mark question. i need 5 questions. do not repeat any questions. do not generate any other text other than the question. PART B Generate a sixteen mark question. i need 2 questions. they are brief questions . do not repeat any questions. do not generate any other text other than the question."
uploaded_file = st.file_uploader("Upload PDF file", type=['pdf'])

if uploaded_file:
    data_dir = "E:\\rag\\data"
    file_path = os.path.join(data_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    st.success(f"File saved to {file_path}")


llm = LlamaCpp(
    model_path="E:\\rag\\models\\mistral-7b-v0.1.Q4_0.gguf",
    n_gpu_layers=0,
    n_batch=512,
    n_ctx=2048,
    f16_kv=True,
)


embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")


import os
home = os.getcwd()
data  = home + '\data'
documents = SimpleDirectoryReader(data).load_data()


index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)


query_engine = index.as_query_engine(llm=llm)


if st.button('Generate Questions'):
    if query:
        
        response = query_engine.query(query)
        st.write('Generated Questions:')
        st.write(response.response)
        # for i, question in enumerate(response.response):
        #     st.write(f'{i+1}. {question}')
    else:
        st.warning('Please enter some text from the book.')

