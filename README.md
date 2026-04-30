# Interview Transcript Summarizer

A Python script that analyzes interview transcripts using Google Gemini API and produces a structured candidate assessment with three sections: topics covered, role/profile fit with justification, and a 4–6 sentence candidate summary.

## How to Run

### Prerequisites
- Python 3.8+
- Google Gemini API key (free tier at https://aistudio.google.com)

### Setup

```bash
# Clone and install
git clone https://github.com/rishavkr206/interview-transcript-summarizer.git
cd interview-transcript-summarizer

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### API Key Setup

Create a `.env` file in the project root (use `.env.example` as reference):

```bash
cp .env.example .env
```

Open `.env` and add your key:
```
GEMINI_API_KEY=your_actual_key_here
```

**Never commit this file.** It is already listed in `.gitignore`.

### Running the Script

```bash
# Print output to console
python summarizer.py transcript.txt

# Save output to a file
python summarizer.py transcript.txt output_summary.txt
```

### Example

```bash
python summarizer.py sample_transcript_assignment_1.txt
```

---

## LLM Provider & Model

- **Provider:** Google AI Studio (Gemini)
- **Model:** `gemini-2.0-flash`
- **Why:** Free tier with 1,500 requests/day and a 1M token context window — more than sufficient for long interview transcripts.

---

## Reflection

### What Surprised Me

**1. Small wording changes in the prompt had outsized effects.**
Adding a single format example like `"[Role] — [Seniority Level]"` was enough to make the model consistently produce structured role classifications instead of free-form descriptions. I expected to need much more explicit instruction — the model is more sensitive to examples than to lengthy explanations.

**2. Generalization across interview types was harder than expected.**
A prompt tuned for a technical interview would produce completely wrong topic categories for a business/operations interview. Transcript 1 needed frameworks, tools, and architecture patterns; Transcript 2 needed KPIs, vendor processes, and stakeholder dynamics. Getting both right with a single prompt required deliberate branching logic and multiple test iterations.

**3. The model sometimes reframes candidate weaknesses as neutral observations.**
Without an explicit instruction like "if the candidate shows hesitation, note it as a concern — not a strength," the model tended to soften or omit gaps. Adding the IMPORTANT block to the prompt was the single biggest quality improvement between Iteration 2 and 3.

### What I'd Improve With More Time

**1. Multi-step prompting.**
Break the task into stages: (a) extract raw facts, (b) classify role based on those facts, (c) write the summary using the classification. The current single-prompt approach works well but gives the model too much to juggle at once, which occasionally causes role classification to drift.

**2. Few-shot examples in the prompt.**
Include one complete example transcript + expected output to anchor the model's understanding of what "good" looks like. This would reduce variance across different transcript styles.

**3. Output validation and re-prompting.**
Parse the model's response and check that all three sections are present and correctly formatted. If any section is missing or malformed, automatically re-prompt with a correction instruction rather than returning a broken output.

**4. Confidence scoring.**
Add a fourth output field where the model rates its own confidence in the role classification (e.g., High/Medium/Low) and explains why. Useful for cases where the transcript is very short or the candidate's background is ambiguous.

### Limitations of the Final Prompt

**1. Hallucination risk on thin transcripts.**
If the transcript is under 500 words or the candidate gives very short answers, the model may invent concerns or strengths not actually evidenced in the text. The instruction to "reference actual content" helps but does not fully prevent this.

**2. Short transcript degradation.**
Very brief interviews lack enough signal for accurate seniority classification. The model defaults to generic mid-level classifications when evidence is sparse.

**3. Language and accent bias.**
The interviewer in Transcript 2 flagged the candidate's use of Hindi jargon as a concern. The model correctly picked this up because it was stated explicitly. However, the model cannot independently assess communication quality from text — it relies on the interviewer explicitly noting it.

**4. Single API call, no retry on partial output.**
If the model returns an incomplete response (rare but possible), the script surfaces the raw partial output with no fallback. A production version would validate and retry.

**5. Free tier rate limits.**
Gemini's free tier caps at 15 requests/minute. Long transcripts or back-to-back calls can hit this ceiling quickly. The script does not currently implement retry logic with exponential backoff.

### Time Spent
Approximately 3 hours:
- 30 min: Understanding the task, setting up Gemini API
- 1 hour: Prompt design and iteration (V1 → V3) tested against both transcripts
- 1 hour: Script development, error handling, CLI argument support
- 30 min: Documentation, README, and final cleanup
