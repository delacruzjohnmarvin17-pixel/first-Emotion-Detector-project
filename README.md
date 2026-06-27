# Repository for final project
# Emotion Detector Web Application

## Overview

This project is an AI-powered **Emotion Detection Web Application** developed using **IBM Watson NLP** and **Flask**. It analyzes text entered by the user and predicts the emotions expressed in the text, displaying both the individual emotion scores and the dominant emotion.

This project was completed as part of the **IBM Developer Skills Network Final Project**.

---

## Original Project Repository

This project is based on the IBM Developer Skills Network starter project:

https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai

---

## Project Objectives

The project fulfills the following requirements:

* Clone the original project repository.
* Develop an emotion detection application using IBM Watson NLP.
* Format the prediction results into a user-friendly output.
* Package the application as a reusable Python module.
* Create and execute unit tests.
* Deploy the application using the Flask web framework.
* Implement proper error handling.
* Perform static code analysis using Pylint.

---

## Technologies Used

* Python 3
* Flask
* IBM Watson NLP
* Requests
* HTML
* CSS
* JavaScript
* Pylint
* Unit Testing

---

## Features

* Detects emotions from user text.
* Displays emotion scores for:

  * Anger
  * Disgust
  * Fear
  * Joy
  * Sadness
* Identifies the dominant emotion.
* Handles invalid or empty user input.
* Provides a simple and responsive web interface.

---

## Project Structure

```
EmotionDetection/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── static/
├── templates/
├── server.py
├── test_emotion_detection.py
├── README.md
├── LICENSE
└── requirements.txt
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/delacruzjohnmarvin17-pixel/first-Emotion-Detector-project.git
```

Move into the project directory.

```bash
cd first-Emotion-Detector-project
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server.

```bash
python server.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Sample Output

**Input**

```
I am very happy today!
```

**Output**

```
anger: 0.01
disgust: 0.02
fear: 0.01
joy: 0.95
sadness: 0.01

Dominant Emotion: joy
```

---

## Running Unit Tests

```bash
python test_emotion_detection.py
```

---

## Static Code Analysis

```bash
pylint EmotionDetection
```

---

## Error Handling

The application handles:

* Empty user input
* Invalid API responses
* Network connection errors
* Unexpected exceptions

---

## Learning Outcomes

Through this project, I learned how to:

* Integrate IBM Watson NLP services.
* Build a Flask web application.
* Package Python modules.
* Write unit tests.
* Perform static code analysis.
* Implement proper error handling.
* Deploy an AI-powered web application.

---

## Author

**John Marvin D. Dela Cruz**

Master of Arts in Education major in Mathematics

Philippines

---

## License

This project is intended for educational purposes as part of the IBM Developer Skills Network course.
