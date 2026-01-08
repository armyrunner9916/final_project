# pylint: disable=import-error
"""Short Python program designed to assess emotion in customer comments"""

from flask import Flask, request
import requests
import json

app = Flask(__name__)
app.json.sort_keys = False

# Defining function for user submission
@app.route("/ask")
def emotion_detector():
    """Run Watson emotion detection for the submitted text."""

    text_to_analyze = request.args.get("text")
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

if __name__ == "__main__":
    app.run()
