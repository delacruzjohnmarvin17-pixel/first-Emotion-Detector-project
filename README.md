# Emotion Detection Web App

## 📌 Project Name
Final Project - Emotion Detection System

## 📖 Description
This project is a simple web-based Emotion Detection application built using Flask and IBM Watson NLP API.

It analyzes user input text and detects emotions such as:
- Anger
- Disgust
- Fear
- Joy
- Sadness

The system also identifies the dominant emotion from the input text.

---

## ⚙️ How It Works
1. User enters a text input in the web interface.
2. The Flask backend sends the text to the Watson Emotion API.
3. The API returns emotion scores.
4. The system processes the response and extracts:
   - Emotion scores
   - Dominant emotion
5. The result is displayed on the web page.

---

## 🚀 Features
- Emotion analysis using AI (IBM Watson NLP)
- Displays emotion scores
- Highlights dominant emotion
- Simple Flask web interface

---

## 🛠️ Technologies Used
- Python 3.11
- Flask
- IBM Watson NLP API
- HTML, JavaScript

---

## 📂 Project Structure
final_project/oaqjp-final-project-emb-ai
└── EmotionDetection/
    ├── __pycache__/
    │   ├── __init__.py
    │   └── emotion_detection.py
    │
    ├── static/
    │   └── mywebscript.js
    │
    ├── templates/
    │   └── index.html
    │
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── server.py
    └── test_emotion_detection.py
