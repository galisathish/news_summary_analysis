Here's a README.md for your GitHub repository, including sections and placeholders for images.

📢 News Sentiment Analysis

This project is a news sentiment analysis tool that scrapes Google News for articles related to a company, analyzes sentiment, extracts key topics, and generates a Hindi text-to-speech summary. It includes a FastAPI backend and a Streamlit frontend.

🚀 Features

✅ News Scraping – Fetches latest news articles from Google News

✅ Sentiment Analysis – Classifies headlines as Positive, Negative, or Neutral

✅ Topic Extraction – Identifies key discussion topics

✅ Hindi Audio Summary – Converts headlines into speech using gTTS

✅ Interactive UI – Simple and user-friendly Streamlit interface



🏗️ Project Structure

├── app.py            # Streamlit UI  
├── api.py            # FastAPI backend  
├── utils.py          # Helper functions (news scraping, sentiment analysis, TTS)  
├── requirements.txt  # Dependencies  
├── README.md         # Documentation  
└── assets/           # Images for documentation  


📥 Installation

 Install Dependencies

pip install -r requirements.txt

🖥️ Execution

1️⃣ Start the Backend (FastAPI Server)

uvicorn api:app --reload

✅ Runs on http://127.0.0.1:8000

🔗 Check API Docs: http://127.0.0.1:8000/docs

2️⃣ Start the Frontend (Streamlit App)

streamlit run app.py

✅ Runs on http://localhost:8501



🎮 How to Use

1️⃣ Enter a company name in the text box

2️⃣ Click "Get Sentiment Report"

3️⃣ View extracted news articles, sentiment distribution, and key topics

4️⃣ Listen to the Hindi audio summary of the news

🌐 API Endpoints

Method	Endpoint	Description

POST	/news_analysis	Fetch news and analyze sentiment


📩 Request Example:json

{
  "company": "Tesla"
}
📤 Response Example:

{

  "Company": "Tesla",
  
  "Articles": [
  
    {
    
      "Title": "Tesla launches new model...",
      
      "Summary": "Tesla has released...",
      
      "Sentiment": "Positive",
      
      "Topics": ["Electric Cars", "Tesla", "Technology"]
    
    }
  
  ],
  
  "Comparative Sentiment Score": {
  
    "Sentiment Distribution": {
    
      "Positive": 5,
      
      "Negative": 3,
      
      "Neutral": 2
    
    }
  
  },
  
  "Audio": "output.mp3"

}


🛠️ Technologies Used

Python (FastAPI, Streamlit)

BeautifulSoup (Web Scraping)

TextBlob (Sentiment Analysis)

gTTS (Text-to-Speech)

Requests (API Handling)


📌 Notes

⚠️ Google News scraping might be restricted; ensure your IP is not blocked.

⚠️ Sentiment Analysis relies on TextBlob, which may have limitations in accuracy.

