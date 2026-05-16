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
        client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

        with st.spinner("Checking document relevance..."):
            relevance_check = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=10,
                messages=[
                    {
                        "role": "user",
                        "content": (
                            "Does the following document relate to AML (Anti-Money Laundering), "
                            "KYC (Know Your Customer), financial compliance, or related regulatory topics? "
                            "Reply with only 'yes' or 'no'.\n\n"
                            f"{document_text[:2000]}"
                        )
                    }
                ]
            )

        is_aml_related = relevance_check.content[0].text.strip().lower().startswith("yes")

        if not is_aml_related:
            st.error(
                "This document doesn't appear to be AML/KYC related. "
                "Please upload a regulatory document covering topics such as Anti-Money Laundering, "
                "Know Your Customer, or financial compliance."
            )
        else:
            with st.spinner("Analyzing document..."):
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