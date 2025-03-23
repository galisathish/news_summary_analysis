# News Sentiment Analysis

## Project Setup

### Prerequisites
Ensure you have Python installed on your system. Then, install the required dependencies using:

```sh
pip install -r requirements.txt
```

### Running the Application

1. Start the FastAPI backend:
    ```sh
    python api.py
    ```
    The API will be available at `http://127.0.0.1:8000`

2. Run the Streamlit frontend:
    ```sh
    streamlit run app.py
    ```

## Model Details

### Summarization
- News articles are scraped and summarized using BeautifulSoup.
- The first paragraph of an article is used as its summary.

### Sentiment Analysis
- Sentiment analysis is performed using TextBlob.
- The sentiment polarity determines if the article is `Positive`, `Negative`, or `Neutral`.

### Text-to-Speech (TTS)
- Google Text-to-Speech (`gTTS`) converts article titles into Hindi speech.
- The generated audio file (`output.mp3`) is available for playback.

## API Development

### Endpoint: `/news_analysis`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "company": "Tesla"
  }
  ```
- **Response Example**:
  ```json
  {
    "Company": "Tesla",
    "Articles": [
      {
        "Title": "Tesla's stock surges",
        "Summary": "Tesla stock increased by 10% today...",
        "Sentiment": "Positive",
        "Topics": ["Stock Market", "Technology"]
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
  ```

### Testing API with Postman
- Set the request type to `POST`.
- Enter `http://127.0.0.1:8000/news_analysis` as the URL.
- Add the JSON payload in the `Body`.
- Send the request and check the response.

## API Usage

### Third-Party APIs Used
1. **Google News Scraping**: Fetches news articles.
2. **TextBlob**: Performs sentiment analysis.
3. **gTTS (Google Text-to-Speech)**: Generates audio summaries.

## Assumptions & Limitations

- **Scraping Reliability**: Google News scraping may break if website structure changes.
- **Sentiment Accuracy**: TextBlob provides basic sentiment analysis but may not be highly accurate.
- **TTS Language**: Only Hindi TTS is supported.
- **Limited Articles**: Only the first 10 news articles are processed per request.

