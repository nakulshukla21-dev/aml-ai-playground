import anthropic
import fitz  # this is pymupdf

# Open and extract text from a PDF
doc = fitz.open("document.pdf")
document_text = ""
for page in doc:
    document_text += page.get_text()

# Set up the Anthropic client
client = anthropic.Anthropic(api_key="YOUR_API_KEY_HERE")
# Send to Claude for summary
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": f"Please summarize the following document in 5 bullet points, focusing on key AML/KYC implications:\n\n{document_text[:5000]}"
        }
    ]
)

print(message.content[0].text)

