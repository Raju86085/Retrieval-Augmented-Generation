# Retrieval-Augmented-Generation
Question Paper Generator using Retrieval-Augmented Generation
# RAG-Overview
   RAG has two main parts, retrieval and generation. In the first part, retrieval is used to fetch (chunks of) documents related to the query of interest. Generation uses those fetched chunks as added input, called context, to the answer generation model in the second part. This added context is intended to give the generator more up-to-date, hopefully better, information to base its generated answer on than just its base training data.
# LLM Model 
 LLM’s have a maximum context or sequence window length they can handle, and the generated input context for RAG needs to be short enough to fit into this sequence window. We want to fit as much relevant information into this context as possible, so getting the best “chunks” of text from the potential input documents is important. These chunks should optimally be the most relevant ones for generating the correct answer to the question posed to the RAG system.
# Proposed System 
To tackle the drawbacks of the current manual question paper generating method, the "Automated Question Paper Generation System" that has been presented makes use of RAG (Retrieval Augmented Generation) techniques. The system's automation, customization, and security capabilities are intended to completely transform the assessment generation process.
    Using Retrieval Augmented Generation (RAG) to handle activities that require a lot of information. RAG blends a text generating model with an information retrieval component. Without requiring a complete model retraining, RAG can be adjusted and its internal knowledge changed in an effective way.
Integration of RAG Technique:     
1.	Database of Questions
2.	User Interface
3.	Algorithm for Question Selection 
4.	Randomization and Variation 
5.	Output Generation
# Conclusion 
This application does a good job of demonstrating the capabilities of huge language models and how well they generalize across various documents. With LLMs' assistance, the information extraction procedure has become rather simple. Additionally, with just a basic understanding of Python and without any prior frontend experience, one can quickly create a highly contemporary-looking frontend with Streamlit. This framework is ideal for developing tiny applications and proof-of-concepts centered around a machine-learning model. The most recent function-calling technique and the question paper retrieval augmented generation (RAG) method have completely changed how we approach data extraction, information retrieval, and answer generation. These methods provide a more precise and efficient means of extracting and analyzing vast amounts of data, especially when used to question-answering systems.
