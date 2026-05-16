import streamlit as st
import anthropic
import fitz
from dotenv import load_dotenv
import os

load_dotenv()

st.title("AML Document Summarizer")
st.write("Upload a regulatory document (PDF) and get a concise AML/KYC summary.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text from PDF
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    document_text = ""
    for page in doc:
        document_text += page.get_text()

    st.info("Document uploaded successfully. Click below to summarize.")

    if st.button("Summarize"):
        with st.spinner("Analyzing document..."):
          ##  client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
            client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
            message = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": f"Summarize the following AML/KYC regulatory document in 5 bullet points, focusing on key compliance implications:\n\n{document_text[:5000]}"
                    }
                ]
            )

        st.subheader("Summary")
        st.write(message.content[0].text)