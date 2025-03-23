import streamlit as st
import requests

# Streamlit UI
st.title("📢 News Sentiment Analysis")

company_name = st.text_input("Enter Company Name")
display_option = st.radio("Choose Display Format", ("Normal Report", "JSON Output"))

if st.button("Get Sentiment Report"):
    if company_name:
        try:
            # API Request
            api_url = "http://127.0.0.1:8000/news_analysis"
            payload = {"company": company_name}
            response = requests.post(api_url, json=payload)
            
            if response.status_code == 200:
                report = response.json()
                
                if display_option == "JSON Output":
                    st.json(report)
                else:
                    st.markdown(f"**Sentiment Report for {company_name}**")
                    
                    if "Company Name" in report:
                        st.markdown(f"**Company Name:** {report['Company Name']}")
                    
                    if "Sentiment" in report:
                        st.markdown(f"**Overall Sentiment:** {report['Sentiment']}")
                    
                    if "Positive Articles" in report:
                        st.markdown(f"**Positive Articles:** {report['Positive Articles']}")
                    
                    if "Negative Articles" in report:
                        st.markdown(f"**Negative Articles:** {report['Negative Articles']}")
                    
                    if "Neutral Articles" in report:
                        st.markdown(f"**Neutral Articles:** {report['Neutral Articles']}")
                    
                    if "Articles" in report:
                        st.markdown("**Articles:**")
                        for article in report["Articles"]:
                            st.markdown("---")
                            if "Title" in article:
                                st.markdown(f"**Title:** {article['Title']}")
                            if "Summary" in article:
                                st.markdown(f"**Summary:** {article['Summary']}")
                            if "Sentiment" in article:
                                st.markdown(f"**Sentiment:** {article['Sentiment']}")
                            if "Topics" in article:
                                st.markdown(f"**Topics:** {', '.join(article['Topics'])}")
                    
                    if "Summary" in report:
                        st.markdown(f"**Summary:** {report['Summary']}")
                    
                # Check if an audio file was generated
                if "Audio" in report and report["Audio"] != "No audio generated":
                    st.markdown("**🔊 Sentiment Summary Audio**")
                    audio_url = report["Audio"]
                    st.audio(audio_url, format="audio/mp3")
                
            else:
                st.error("Failed to fetch sentiment report. Please try again.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a company name.")


# import streamlit as st
# import requests
# import json

# # Streamlit UI
# st.title("📢 News Sentiment Analysis")

# company_name = st.text_input("Enter Company Name")

# if st.button("Get Sentiment Report"):
#     if company_name:
#         try:
#             # API Request
#             api_url = "http://127.0.0.1:8000/news_analysis"
#             payload = {"company": company_name}
#             response = requests.post(api_url, json=payload)
            
#             if response.status_code == 200:
#                 report = response.json()

#                 # Display JSON Output
#                 st.subheader(f"Sentiment Report for {company_name}")
#                 st.json(report)  # Displaying the response in JSON format

#                 # Check if an audio file was generated
#                 if "Audio" in report and report["Audio"] != "No audio generated":
#                     st.subheader("🔊 Sentiment Summary Audio")
#                     audio_url = report["Audio"]
                    
#                     # Streamlit audio player
#                     st.audio(audio_url, format="audio/mp3")
                    
#             else:
#                 st.error("Failed to fetch sentiment report. Please try again.")

#         except Exception as e:
#             st.error(f"An error occurred: {e}")
#     else:
#         st.warning("Please enter a company name.")
