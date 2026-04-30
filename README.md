# Interview Transcript Summarizer

A Python script that analyzes interview transcripts using Google Gemini API and produces a structured candidate assessment with three sections: topics covered, role/profile fit with justification, and a 3–6 sentence candidate summary.

## How to Run

### Prerequisites
- Python 3.8+
- Google Gemini API key (free tier at https://aistudio.google.com)

### Setup

```bash
# Clone and install
git clone https://github.com/rishavkr206/interview-transcript-summarizer.git
cd interview-transcript-summarizer

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
