import os
from google.generativeai import Client

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Initialize the Google Gemini API client
api_key = os.getenv('GOOGLE_API_KEY')
client = Client(api_key=api_key)

def analyze_transcript(transcript):
    """
    Analyze the interview transcript and return a summary.
    
    Parameters:
    transcript (str): The interview transcript to analyze.
    
    Returns:
    str: The summary of the transcript.
    """
    try:
        # Call the Google Gemini API for summarization
        response = client.summarize(transcript)
        return response['summary']
    except Exception as e:
        print(f'Error during API call: {e}')  # Proper error handling

if __name__ == '__main__':
    # Example usage
    transcript = "Your interview transcript here."
    summary = analyze_transcript(transcript)
    print(summary)