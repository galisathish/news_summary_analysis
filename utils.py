import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS


def extract_news(company):
    """
    Scrapes Google News for articles related to the company.
    """
    search_url = f"https://www.google.com/search?q={company}+news&tbm=nws"
    headers = {"User-Agent": "Chrome/91.0.4472.124 Safari/537.36"}
    
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    for item in soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd"):
        title = item.text
        parent = item.find_parent("a")
        link = "https://www.google.com" + parent["href"] if parent else "No URL found"
        
        summary, topics = extract_summary_and_topics(link)
        
        articles.append({"Title": title, "Summary": summary, "Topics": topics, "URL": link})
        
        if len(articles) >= 10:
            break
    
    return articles

def extract_summary_and_topics(url):
    """
    Extracts summary and topics from the given news URL.
    """
    try:
        response = requests.get(url, headers={"User-Agent": "Chrome/91.0.4472.124 Safari/537.36"})
        soup = BeautifulSoup(response.text, "html.parser")
        
        paragraphs = soup.find_all("p")
        summary = " ".join([para.text for para in paragraphs[:1]]) if paragraphs else "Summary unavailable"
        
        topics = [meta["content"] for meta in soup.find_all("meta", attrs={"name": "keywords"})]
        topics = topics[0].split(",") if topics else ["Topics unavailable"]
        
        return summary, topics
    except Exception as e:
        return "Error fetching summary", ["Error fetching topics"]

def analyze_sentiment(text):
    """
    Performs sentiment analysis on the given text.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

def generate_tts(text, lang="hi"):
    """
    Converts text to Hindi speech using gTTS.
    """
    if not text:
        return "No audio generated"
    
    tts = gTTS(text, lang=lang)
    file_path = "output.mp3"
    tts.save(file_path)
    
    return file_path
