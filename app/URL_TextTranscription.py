from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse
import os
import ntpath
import re
import librosa    
import soundfile as sf
from pydub import AudioSegment
import moviepy.editor as mp 
import PyPDF2 as pdf
import textract

from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Load the modern punctuation model
punctuation_tokenizer = AutoTokenizer.from_pretrained("oliverguhr/fullstop-punctuation-multilang-large")
punctuation_model = AutoModelForTokenClassification.from_pretrained("oliverguhr/fullstop-punctuation-multilang-large")
punctuate = pipeline("token-classification", model=punctuation_model, tokenizer=punctuation_tokenizer, aggregation_strategy="simple")

def restore_punctuation(text):
    results = punctuate(text)
    punctuated = ""
    last_idx = 0
    for item in results:
        word = item['word']
        label = item['entity_group']
        if label == "O":
            punctuated += word + " "
        else:
            punctuated = punctuated.strip() + get_punctuation_symbol(label) + " "
    return punctuated.strip()

def get_punctuation_symbol(label):
    return {
        "PERIOD": ".",
        "COMMA": ",",
        "QUESTION": "?",
        "EXCLAMATION": "!",
    }.get(label, "")


def URL_Text_Transcription(video_url):
    url_data = urllib.parse.urlparse(video_url)
    query = urllib.parse.parse_qs(url_data.query)
    video = query["v"][0]
    print(video)
    video_url = "https://youtu.be/" + str(video[:11])
    print(video_url)

    p_path = os.getcwd()
    dir_name = "Results/" + str(video_url[-11:])
    path = os.path.join(p_path, dir_name)
    if not os.path.isdir(path):
        os.mkdir(path)

    transcript_list = YouTubeTranscriptApi.get_transcript(video)
    transcript_text = ""
    for i in transcript_list:
     if i['text'] == "[Music]":
        continue
     transcript_text += i['text'] + " "

    print("Raw transcript:")
    print(transcript_text)
    print("Word count:", len(transcript_text.strip().split()))


    arr_words, arr_timing = [], []
    transcript_text = ""

    transcription_with_timestamps_fpath = os.path.join(path, "transcription_with_timestamps.txt")
    with open(transcription_with_timestamps_fpath, 'w') as f:
        for i in transcript_list:
            if i['text'] == "[Music]":
                continue
            f.write(f"{i['start']} - {i['text']}\n")
            transcript_text += i['text'] + " "
            for word in i['text'].split():
                arr_words.append(word.lower())
                arr_timing.append(int(i['start']))

    transcription_text_fpath = os.path.join(path, "transcription_text.txt")
    with open(transcription_text_fpath, 'w') as f:
        f.write(transcript_text)

    # Modern punctuation restoration
    punctuated_text = restore_punctuation(transcript_text)

    transcription_punctuated_fpath = os.path.join(path, "transcription_punctuated.txt")
    with open(transcription_punctuated_fpath, 'w') as f:
        f.write(punctuated_text)

    return [transcription_text_fpath, transcription_punctuated_fpath], arr_words, arr_timing, video, video_url


def extract_text_from_url(url):
    if "youtube.com" in url or "youtu.be" in url:
        paths, words, times, video_id, video_url = URL_Text_Transcription(url)
        with open(paths[1], 'r') as f:
            return f.read()
    else:
        return "Unsupported URL or file format."
