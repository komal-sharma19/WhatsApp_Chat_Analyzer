# WhatsApp Chat Analyzer
A powerful and interactive web application built using Streamlit that allows users to analyze their WhatsApp chat history and gain detailed insights into messaging patterns, word usage, media sharing, emojis, and more.


# Features
📥 Upload and parse exported WhatsApp chat .txt files

👤 Analyze chat statistics for individual users or overall group

🧮 Message, word, media, and link count

📆 Monthly and daily chat timeline visualization

📈 User activity maps by day and month

👑 Identify the most active users in group chats

☁️ Generate word clouds of most used words

🔤 List most frequently used words

😂 Emoji analysis with pie chart and table

# Technologies Used:

Python

Streamlit

Matplotlib

Pandas

WordCloud

Emoji

URLExtract

# Project Structure

📂 whatsapp-chat-analyzer/

├── app.py                  # Main Streamlit application

├── preprocessor.py         # Chat cleaning and preprocessing

├── helper.py               # All analytical and visualization functions

├── stop_hinglish.txt       # Stopword file for word cloud filtering

├── requirements.txt        # Dependencies

└── README.md               # Project overview and instructions

# Setup Instructions

cd whatsapp-chat-analyzer

## Install dependencies:

pip install -r requirements.txt

## Run the Streamlit app:

streamlit run app.py

Upload your WhatsApp chat file

Export the chat from WhatsApp (without media)

Upload the .txt file using the sidebar in the app

#  Exporting WhatsApp Chat

Open a chat in WhatsApp

Tap on the three-dot menu > More > Export Chat

Choose without media

Transfer the .txt file to your PC and upload it in the app

# Notes:

Ensure the WhatsApp chat is in English or Hinglish for accurate word cloud and frequency analysis.

Currently supports exported chat from Android format. iOS format might need adjustments in preprocessing.
