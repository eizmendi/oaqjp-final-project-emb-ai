from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def RunSentimentAnalysis():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if input is provided
    if not text_to_analyze:
        return jsonify({"error": "No input text provided. Please try again!"}), 400

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the response contains the required data
    if not response or 'dominant_emotion' not in response:
        return jsonify({"error": "Failed to analyze emotions. Please try again!"}), 500

    # Extract scores and dominant emotion
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Construct the formatted text response
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, "
        f"'joy': {joy_score} and 'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    # Return a JSON response with the extracted emotion scores
    return response_text

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)