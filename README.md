# 🎯 Interview Transcript Analyzer

A sophisticated Python application that leverages Google Gemini API to automatically analyze interview transcripts and generate structured candidate assessments. Perfect for recruiters, hiring managers, and interview teams.

---

## ✨ Features

- **🔍 Automatic Topic Extraction**: Identifies 6-8 main themes discussed in the interview
- **👤 Role Classification**: Determines candidate role and seniority level with reasoning
- **📊 Structured Assessment**: Generates 4-6 sentence candidate summaries covering background, strengths, concerns, and overall fit
- **🎯 Generalization**: Handles both technical and business/operations interviews seamlessly
- **🔒 Secure API Management**: Environment variables protect sensitive credentials
- **⚡ Fast & Reliable**: Uses Google Gemini 2.0 Flash for quick inference
- **📝 Detailed Output**: Professionally formatted analysis reports

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key (free tier available)
- Windows, macOS, or Linux

### 1️⃣ Get Your API Key

1. Visit [Google AI Studio](https://aistudio.google.com)
2. Sign in with your Google account
3. Click **"Get API key"** → **"Create API key in new project"**
4. Copy your API key

### 2️⃣ Clone & Setup

```bash
# Clone repository
git clone https://github.com/rishavkr206/interview-transcript-summarizer.git
cd interview-transcript-summarizer

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
