# AML Document Summarizer

An AI-powered tool that summarizes AML/KYC regulatory documents using the Claude API.

## What it does
Paste in any FATF recommendation, FinCEN advisory, or AML/KYC regulatory document and get a concise 5-point summary of the key compliance implications — in seconds.

## Why it matters
AML/KYC compliance teams deal with dense, lengthy regulatory documents. This tool demonstrates how LLMs can accelerate regulatory review and support compliance workflows in financial institutions.

## Tech stack
- Python
- Anthropic Claude API (claude-sonnet-4-6)
- PyMuPDF for PDF extraction
- python-dotenv for secure key management

## How to run
1. Clone the repo
2. Install dependencies: `pip install anthropic pymupdf python-dotenv`
3. Create a `.env` file with your Anthropic API key: `ANTHROPIC_API_KEY=your-key-here`
4. Add your PDF document as `document.pdf`
5. Run: `python summarize.py`

## Sample output
Tested on FATF Recommendations (October 2025 update) — extracted key AML/KYC implications including risk-based approach, CDD requirements, beneficial ownership transparency, sanctions compliance, and STR obligations.
