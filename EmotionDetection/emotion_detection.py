import requests, json

def emotion_detector(text_to_analyse): 
    """
    Function to detect emotions from a given text:
    Return raw text

    """
    # URL of the sentiment analysis service 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the expected format 
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Custom header specifying the model ID for the sentiment analysis service 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API 
    response = requests.post(url, json=myobj, headers=header)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Parsing the JSON response from the API 
        formatted_response = json.loads(response.text)

        # Extracting sentiment label and score from the response 
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        anger_score = emotions['anger'] 
        disgust_score = emotions['disgust'] 
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        dominant_emotion = max(emotions, key=emotions.get)
    # If the response status code is 400, set scores to None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    else:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
     
    # Return text from emotion detector
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }

