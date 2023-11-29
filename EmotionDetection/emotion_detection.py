import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        emotion_score = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        highest_score = max(emotion_score)
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        highest_score = None
    
    dict_emotion = {'anger': anger_score,
     'disgust': disgust_score, 
     'fear': fear_score, 
     'joy': joy_score, 
     'sadness': sadness_score}
    
    def get_name_emotion(highest_score):
        if highest_score != None:
            for x, y in dict_emotion.items():
                if y == highest_score:
                    return x
        return highest_score

    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': get_name_emotion(highest_score)
            }
    