from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app 
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response 
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response 
    anger = response['anger'] 
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with the sentiment label and score 
    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger, disgust, fear, joy, sadness, dominant_emotion)
   

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
    

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:8000
    '''
    app.run(host="0.0.0.0", port=5000)
