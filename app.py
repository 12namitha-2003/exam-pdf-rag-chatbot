import streamlit as st
from pdf_utils import extract_text_from_pdf, split_text
from rag_engine import create_vector_store, rag_chat

# Page config
st.set_page_config(page_title="Exam PDF Chatbot", layout="wide")

st.title("📚 Exam PDF Chatbot")

# Initialize session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_ready" not in st.session_state:
    st.session_state.pdf_ready = False


# -------------------------------
# PDF Upload Section
# -------------------------------
uploaded_file = st.file_uploader("Upload Study PDF", type=["pdf"])

if uploaded_file and not st.session_state.pdf_ready:

    with st.spinner("Processing PDF... Please wait"):
        text = extract_text_from_pdf(uploaded_file)
        chunks = split_text(text)
        create_vector_store(chunks)

    st.session_state.pdf_ready = True
    st.success("✅ PDF Processed Successfully! You can now ask questions.")


# -------------------------------
# Chat Section
# -------------------------------

# Display previous chat messages
for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.write(message)


# Chat input box
if st.session_state.pdf_ready:
    question = st.chat_input("Ask exam question (14-mark style)")

    if question:

        # Add user message to chat history
        st.session_state.messages.append(("user", question))

        # Generate AI response
        with st.spinner("Generating detailed exam answer..."):
            answer = rag_chat(question)

        # Add assistant response
        st.session_state.messages.append(("assistant", answer))

        # Rerun to refresh UI instantly
        st.rerun()

else:
    st.info("📄 Please upload a PDF to begin.")
