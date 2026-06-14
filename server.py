from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Detector de emociones")

@app.route('/emotionDetector')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotionDetector")
def emote_detector():
    texto = request.args.get('textToAnalyze')
    respuesta = emotion_detector(texto)
    if respuesta['dominant_emotion'] is None:
        return "No se ha reconocido ninguna emoción! "
    return( respuesta, 200)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
