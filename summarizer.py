import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.0-flash"

# Validate API key
if not GEMINI_API_KEY:
    print("❌ ERROR: GEMINI_API_KEY not found in .env file")
    print("📝 Please create a .env file with: GEMINI_API_KEY=your_key_here")
    sys.exit(1)

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Final Optimized Prompt (Iteration 3)
ANALYSIS_PROMPT = """Analyze this interview transcript and provide a structured candidate assessment:

1. TOPICS COVERED
   - Extract 6-8 main topics/themes discussed in the interview
   - For technical interviews: frameworks, tools, architecture patterns, coding approaches
   - For business/operations interviews: processes, KPIs, stakeholder management, strategic decisions
   - Format as a simple bulleted list
   - Example: ["AI-assisted coding", "Ionic framework", "Mobile responsiveness", "State management"]

2. PROFILE & ROLE FIT
   - Determine the best-fit role and seniority level
   - Consider: years of experience, depth of expertise, breadth of skills, communication style, confidence level
   - Format: "[Role] — [Seniority Level]" (e.g., "Full-Stack Mobile Engineer — Mid-level" or "Operations Manager — Mid-level")
   - Justification: 1-2 specific sentences explaining why this profile fits based on demonstrated skills/experience

3. CANDIDATE SUMMARY
   - Write 4-6 sentences covering:
     a) Background: Career progression, education, key roles/transitions
     b) Strengths: 2-3 key strengths demonstrated (with specific examples from the interview)
     c) Concerns: Areas that need improvement or hesitations observed
     d) Overall Impression: One concluding sentence on how well-suited they are
   - Be specific. Avoid generic praise. Reference actual content from the transcript.

IMPORTANT:
- Do not assume the role. Let the interview content guide the classification.
- Distinguish between technical confidence and soft skills (communication, clarity).
- If candidate shows hesitation or gaps, note them as concerns, not strengths.
- If the candidate's background doesn't align with typical profiles, still classify based on demonstrated capability.

Here is the transcript:

{transcript_content}

Please provide the structured analysis above."""

def read_transcript(file_path: str) -> str:
    """Read transcript from file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ ERROR: File '{file_path}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"❌ ERROR reading file: {e}")
        sys.exit(1)

def analyze_transcript(transcript_content: str) -> str:
    """Call Gemini API to analyze transcript."""
    try:
        print("🔄 Analyzing transcript with Gemini API...")
        
        model = genai.GenerativeModel(MODEL_NAME)
        prompt = ANALYSIS_PROMPT.format(transcript_content=transcript_content)
        
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                top_p=0.9,
                top_k=40,
            )
        )
        
        return response.text
    except Exception as e:
        print(f"❌ ERROR calling Gemini API: {e}")
        sys.exit(1)

def format_output(analysis: str, transcript_file: str) -> str:
    """Format the analysis output."""
    output = f"""
╔══════════════════════════════════════════════════════════════╗
║         INTERVIEW TRANSCRIPT ANALYSIS REPORT                ║
╚══════════════════════════════════════════════════════════════╝

📄 Transcript File: {transcript_file}

{'-' * 62}

{analysis}

{'-' * 62}
✅ Analysis complete!
"""
    return output

def save_output(output: str, output_file: str = None) -> None:
    """Save output to file if specified."""
    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"💾 Output saved to: {output_file}")
        except Exception as e:
            print(f"⚠️  Warning: Could not save to file: {e}")

def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("📖 USAGE:")
        print("   python summarizer.py <transcript_file> [output_file]")
        print("\n📝 EXAMPLE:")
        print("   python summarizer.py transcript.txt summary.txt")
        print("   python summarizer.py transcript.txt  (prints to console)")
        sys.exit(1)
    
    transcript_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Read transcript
    print(f"📖 Reading transcript from: {transcript_file}")
    transcript_content = read_transcript(transcript_file)
    
    # Analyze
    analysis = analyze_transcript(transcript_content)
    
    # Format output
    output = format_output(analysis, transcript_file)
    
    # Display
    print(output)
    
    # Save if requested
    if output_file:
        save_output(output, output_file)

if __name__ == "__main__":
    main()