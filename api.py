from fastapi import FastAPI
from pydantic import BaseModel
from utils import extract_news, analyze_sentiment, generate_tts

app = FastAPI()

class NewsRequest(BaseModel):
    company: str

@app.post("/news_analysis")
def news_analysis(request: NewsRequest):
    """
    Fetches news, analyzes sentiment, and returns JSON.
    """
    articles = extract_news(request.company)
    
    report = {"Company": request.company, "Articles": []}

    for article in articles:
        sentiment = analyze_sentiment(article["Title"])
        topics = article.get("Topics", ["Unknown"])  # Extract topics from article
        
        report["Articles"].append({
            "Title": article["Title"],
            "Summary": article["Summary"],
            "Sentiment": sentiment,
            "Topics": topics
        })

    # Sentiment Summary
    positive_count = sum(1 for art in report["Articles"] if art["Sentiment"] == "Positive")
    negative_count = sum(1 for art in report["Articles"] if art["Sentiment"] == "Negative")
    neutral_count = sum(1 for art in report["Articles"] if art["Sentiment"] == "Neutral")

    report["Comparative Sentiment Score"] = {
        "Sentiment Distribution": {
            "Positive": positive_count,
            "Negative": negative_count,
            "Neutral": neutral_count
        }
    }

    # Generate Hindi TTS
    summary_text = " ".join(art["Title"] for art in report["Articles"])
    audio_file = generate_tts(summary_text) if summary_text else "No audio generated"
    report["Audio"] = audio_file
    
    return report

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)
