from transformers import pipeline
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from youtube_transcript_api import YouTubeTranscriptApi
import re

# Load abstractive summarizer
abstractive_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extractive_summary(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

def get_transcript_text(video_url):
    video_id_match = re.search(r"v=([\w-]+)", video_url)
    if not video_id_match:
        return None
    video_id = video_id_match.group(1)

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([item['text'] for item in transcript])
        return full_text
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def summarize_text(video_url):
    text = get_transcript_text(video_url)
    if not text:
        return "Transcript not available or too short to summarize.", ""

    # Generate summaries
    abstractive = abstractive_summarizer(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
    extractive = extractive_summary(text)

    # Hybrid combined summary
    combined_summary = f"{abstractive} {extractive}"

    return combined_summary, text
