 AML Document Summarizer

An AI-powered tool that summarizes AML/KYC regulatory documents using the Claude API.

## Live Demo
[Try it here](https://bit.ly/aml-summarizer)

## What it does
Upload any FATF recommendation, FinCEN advisory, or AML/KYC regulatory document (PDF) and get a concise 5-point summary of the key compliance implications — in seconds.

## Why it matters
AML/KYC compliance teams deal with dense, lengthy regulatory documents. This tool demonstrates how LLMs can accelerate regulatory review and support compliance workflows in financial institutions.

## Tech stack
- Python
- Anthropic Claude API (claude-sonnet-4-6)
- Streamlit (web interface + cloud deployment)
- PyMuPDF for PDF extraction
- python-dotenv for secure key management

## How to run locally
1. Clone the repo
2. Install dependencies: `pip install anthropic pymupdf python-dotenv streamlit`
3. Create a `.env` file with your Anthropic API key: `ANTHROPIC_API_KEY=your-key-here`
4. Run: `streamlit run app.py`

## Sample output
Tested on FATF Recommendations (October 2025 update) — extracted key AML/KYC implications including risk-based approach, CDD requirements, beneficial ownership transparency, sanctions compliance, and STR obligations.
