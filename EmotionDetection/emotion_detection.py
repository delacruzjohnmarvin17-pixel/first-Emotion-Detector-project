"""Analyzes the emotion of text using IBM Watson NLP API."""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Analyzes emotion of provided text using IBM Watson NLP API.

    Args:
      text_to_analyize (str): Text to analyze for emotion

    Returns:
     The json of emotions with scores and dominant emotion
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)

        # Check if response was successful (200)
        if response.status_code == 200:
            formatted_response = json.loads(response.text)
            emotions = formatted_response["emotionPredictions"][0]["emotion"]
            dominant_emotion = max(emotions, key=emotions.get)
            return {
                "anger": emotions["anger"],
                "disgust": emotions["disgust"],
                "fear": emotions["fear"],
                "joy": emotions["joy"],
                "sadness": emotions["sadness"],
                "dominant_emotion": dominant_emotion,
            }
        elif response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }
        return {
            "message": f"Failed to process request status_code{response.status_code}"
        }
    except requests.exceptions.RequestException as e:
        # Handle network errors, timesouts, etc
        return {"message": f"Request failed: {e}"}
    except (KeyError, json.JSONDecodeError) as e:
        # Handle bad response of missing keys
        return {"message": f"Parsing error: {e}"}
