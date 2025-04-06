# Instructions for Running the Single-Document Chatbot

This chatbot uses Streamlit, Langchain, Ollama, and ChromaDB to allow you to interact with a single uploaded document.

**Prerequisites:**

1.  **Python:** Ensure you have Python 3.7 or higher installed.
2.  **Ollama:** Install Ollama from [https://ollama.ai/](https://ollama.ai/).  Make sure it's running. You will also need to download a model from ollama.  The code defaults to "mistral", so run `ollama pull mistral`. If you want to use a different model, change the `model="mistral"` line in `rag_pipeline.py`.
3.  **Dependencies:** Install the required Python packages. Open a terminal or command prompt, navigate to the directory where you saved the code files (`rag_pipeline.py` and `app.py`), and run:

    ```bash
    pip install -r requirements.txt
    ```
    (Where `requirements.txt` contains the list of dependencies as provided earlier).
4.  **GPU (Recommended):** While the chatbot *can* run on a CPU, using a GPU will significantly improve performance, especially for the LLM inference. Configure Ollama to use your GPU if you have one.

**Running the Chatbot:**

1.  **Open a terminal or command prompt.**
2.  **Navigate to the directory where you saved `app.py` and `rag_pipeline.py`.**
3.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

4.  **Streamlit will open a web browser tab (usually at `http://localhost:8501`).**
5.  **In the web browser:**
    *   Upload a document (.txt, .pdf, or .docx) using the file uploader.
    *   Wait for the document to be processed (a progress spinner will be displayed).
    *   Once the document is loaded, a message will appear indicating that the system is ready.
    *   Enter your question in the text input field and press Enter.
    *   The chatbot's response will be displayed, along with the source document sections used to generate the response.
    *   You can clear the rag system by pressing the "Clear system" button, allowing you to upload a new document.
    *  If the chatbot answers outside of the scope of the document provided, try improving the prompt in `rag_pipeline.py`.

**Troubleshooting:**

*   **"ModuleNotFoundError" errors:** Double-check that you have installed all the required dependencies using `pip install -r requirements.txt`.
*   **Ollama errors:** Ensure that Ollama is running correctly and that you have downloaded the specified model (`mistral`).  Check the Ollama documentation for troubleshooting tips.
*   **Slow performance:** If the chatbot is running slowly, especially during LLM inference, consider using a GPU or a faster LLM.
*   **Unexpected answers:**  If the chatbot provides inaccurate or nonsensical answers, try refining the prompt in `rag_pipeline.py`.
*   **Large Documents Failing:** Be aware that large documents can take longer to process and may exceed available memory. Consider reducing the document size or optimizing chunking.
