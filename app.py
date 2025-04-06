import streamlit as st
from rag_pipeline import load_documents, load_qa_chain

st.set_page_config(page_title="Single-Document Chat", layout="centered")
st.title("My Own Single-Document Chat with Ollama + Mistral")

if "qa_chain" not in st.session_state:
    st.info("Initializing system...")
    st.session_state.qa_chain = load_qa_chain()

    uploaded_file = st.file_uploader("Upload a document (.txt, .pdf, .docx)", type=["txt", "pdf", "docx"])
    if uploaded_file:
        try:
            with st.spinner("Loading document..."):
                documents = load_documents(uploaded_file.name) # Pass filename to load_documents
                st.session_state.document_content = documents[0].page_content #store the entire document
                st.success("Document loaded! Ask your questions.")
        except Exception as e:
            st.error(f"Error loading document: {e}")
    else:
        st.warning("Please upload a document to begin.")
elif st.button("Clear System"):
    del st.session_state["qa_chain"]
    del st.session_state["document_content"] #remove document conent
    st.rerun()

if "qa_chain" in st.session_state and "document_content" in st.session_state:
    query = st.text_input("Ask a question about the document:")
    if query:
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.qa_chain.run(context=st.session_state.document_content, question=query)
                st.write(response)

            except Exception as e:
                st.error(f"Error processing query: {e}")