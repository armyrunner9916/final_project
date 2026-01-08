"""Flask server for Emotion Detection application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_endpoint():
    """Run emotion detection and return formatted output."""
    text_to_analyze = request.args.get("textToAnalyze")

    if request.method == "POST":
        text_to_analyze = request.form.get("textToAnalyze", text_to_analyze)

    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again.", 400

    result = emotion_detector(text_to_analyze)

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
