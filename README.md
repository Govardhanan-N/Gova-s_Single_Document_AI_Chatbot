# Gova-s_Single_Document_AI_Chatbot
Check out my first RAG application !  Modelled in the need of loading documents, splitting them, creating a vector store, and using a QA chain for answering questions. It also incorporates Streamlit for the UI and uses Hugging Face embeddings and Ollama as requested.

## Introduction

This document provides a brief overview of the technical aspects of the single-document chatbot application.

## Tech Stack Choices

*   **Streamlit:** Streamlit was chosen as the UI framework due to its simplicity and ease of use. It allows for rapid prototyping and deployment of interactive web applications with minimal coding effort.
*   **Langchain:** Langchain provides the framework for building the RAG pipeline, including document loading, text splitting, embedding, vector store integration, and question answering.
*   **Ollama:** Ollama enables local execution of large language models (LLMs) like Mistral. This offers privacy, control, and avoids reliance on external API services.
*   **Mistral:** Mistral was selected as the LLM for its strong performance and open-source availability. It strikes a good balance between quality, size, and resource requirements.
*   **sentence-transformers/all-mpnet-base-v2:** This embedding model was chosen for its relatively high accuracy and manageable size. It provides semantic representations of text chunks, enabling effective retrieval of relevant information.
*   **ChromaDB:** ChromaDB serves as the vector database for storing document embeddings and performing similarity searches. Its ease of use and Python-native integration made it a suitable choice for this project.

## Response Structuring Approach

The response structuring approach relies primarily on prompt engineering. The prompt provided to the LLM explicitly instructs it to:

*   Act as a helpful assistant providing information only from the provided document.
*   Avoid using outside information.
*   Respond with "I don't know" if the answer isn't explicitly stated in the document.
*   Answer questions accurately and concisely.
*   Aim for structured output where possible (e.g., bullet points, lists, short paragraphs).

By carefully crafting the prompt, we guide the LLM to generate responses that are relevant, informative, and structured, improving the user experience.

## Challenges Faced and Solutions Implemented

*   **Hallucinations (LLM Generating Incorrect Information):**
    *   **Challenge:** LLMs are prone to generating factually incorrect or nonsensical information, especially when the context is limited.
    *   **Solution:** We addressed this by:
        *   Strongly emphasizing in the prompt that the LLM should *only* use information from the provided document.
        *   Explicitly instructing the LLM to respond with "I don't know" if the answer isn't found in the document.
*   **Retrieval Accuracy:**
    *   **Challenge:** Ensuring that the retrieval mechanism accurately identifies the most relevant sections of the document for answering a given question.
    *   **Solution:** We addressed this by:
        *   Using a high-quality embedding model (`sentence-transformers/all-mpnet-base-v2`).
        *   Experimenting with different chunk sizes and overlap values for the text splitter.
        *   Adjusting the number of documents retrieved (`k`) to optimize for precision.
*   **Document Size Limits:**
    *   **Challenge:** Larger documents can exceed memory limitations or the LLM's context window.
    *   **Solution:** We addressed this by:
        *   Using a single document approach to keep the corpus size small.
        *   Chunking large documents to create smaller, manageable pieces.
        *   Considered a single-chunk approach for very small documents to circumvent memory issues and improve accuracy.

## Future Improvements

*   Implement more advanced prompt engineering techniques, such as chain-of-thought prompting, to improve the LLM's reasoning abilities.
*   Explore the use of external knowledge sources or APIs to supplement the information in the document (with appropriate safeguards to prevent hallucinations).
*   Implement a user interface for adjusting parameters like chunk size and number of retrieved documents.
*   Add features for summarizing documents or extracting key information.
