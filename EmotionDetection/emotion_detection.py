# pylint: disable=import-error
"""Short Python program designed to assess emotion in customer comments"""

import requests
import json

# Defining function for user submission

def emotion_detector(text_to_analyze):
    """Run Watson emotion detection for the submitted text."""

    no_text = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if not text_to_analyze or not text_to_analyze.strip():
        return no_text

    url = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 400:
        return no_text

    parsed_response = json.loads(response.text)

    emotions = parsed_response["emotionPredictions"][0]["emotion"]

    top_emotion = max(emotions, key=emotions.get)

    result = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": top_emotion
    }

    return result
