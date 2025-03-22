import streamlit as st
import requests
import json

# Streamlit UI
st.title("📢 News Sentiment Analysis")

company_name = st.text_input("Enter Company Name")

if st.button("Get Sentiment Report"):
    if company_name:
        try:
            # API Request
            api_url = "http://127.0.0.1:8000/news_analysis"
            payload = {"company": company_name}
            response = requests.post(api_url, json=payload)
            
            if response.status_code == 200:
                report = response.json()

                # Display JSON Output
                st.subheader(f"Sentiment Report for {company_name}")
                st.json(report)  # Displaying the response in JSON format

                # Check if an audio file was generated
                if "Audio" in report and report["Audio"] != "No audio generated":
                    st.subheader("🔊 Sentiment Summary Audio")
                    audio_url = report["Audio"]
                    
                    # Streamlit audio player
                    st.audio(audio_url, format="audio/mp3")
                    
            else:
                st.error("Failed to fetch sentiment report. Please try again.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a company name.")
