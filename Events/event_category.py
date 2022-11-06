import random 
import json 
import pickle 
import numpy as np 
import os
    
import nltk 
from nltk.stem import WordNetLemmatizer
lemmatizer = nltk.stem.WordNetLemmatizer()

from tensorflow.keras.models import load_model

lemmatizer = nltk.stem.WordNetLemmatizer()
intents = json.loads(open('Events\events.json').read())


kk = open('Events\words.pkl','rb')
words = pickle.load(kk)
kk.close()


kp = open('Events\classes.pkl','rb')
classes = pickle.load(kp)
kp.close()
model = load_model('Events\eventbot.h5')  

def clean_up_sentence(sen):
    sentence_words =  nltk.tokenize.casual_tokenize(sen)
    sentence_words = [lemmatizer.lemmatize(word)for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w: 
                bag[i] = 1

    return np.array(bag)


def predict_class(sentence): 
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]

    EROOR_THRESHOLD =   0.25 
    result = [[i,r]for i,r in enumerate(res) if r>   EROOR_THRESHOLD]

    result.sort(key = lambda x : x[1],reverse = True)
    return_list = []
    for r in result:
        return_list.append({'intent':classes[r[0]],'probability': str(r[1])} )
    return return_list

def get_response(intents_list,intents_json): 
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents: 
        if i['tag'] == tag: 
            result = random.choice(i['responses'])
            break 
    return result 

print("The Bot is running, Less Go!!!!")

def mm(message):
    while True: 
        ints = predict_class(message)

        res = get_response(ints,intents)
        return res















