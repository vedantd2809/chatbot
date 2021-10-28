# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 19:48:50 2021

@author:Vedant Deshmukh 
"""
import numpy as np
import nltk
import string
import random

f = open('chatbot.txt','r',errors = 'ignore')

raw_doc=f.read()
raw_doc = raw_doc.lower()

nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

sent_tokens[:1]

word_tokens[:2]



lem = nltk.stem.WordNetLemmatizer()

def lto(tokens):
    return [lem.lemmatize(token)for token in tokens]

remove_punct_dict = dict((ord(punct), None)for punct in string.punctuation)


def lno(text):
    return lto(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


h_in = ("hello","hi","sup","hey","whatsup")
h_re = ["supp","how you doin"]

def strt(sentence):
    for word in sentence.split():
        if word.lower() in h_in:
            return random.choice(h_re)
        
        
        
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def res(user):
    robo1_response = ""
    TfidVec = TfidfVectorizer(tokenizer=lno, stop_words='english')
    Tfid = TfidVec.fit_transform(sent_tokens)
    vals = cosine_similarity(Tfid[-1],Tfid)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfid=flat[-2]
    if(req_tfid==0):
        robo1_response+'correct your grammer'
        return robo1_response
    
    else:
        robo1_response=robo1_response+sent_tokens[idx]
        return robo1_response
    
    
flag = True
print('BOT:You can start convo.')
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='exit'):
        if(user_response=='thanks' or user_response=='thank you'):
            flag==False
            print('USme kya')
        else:
            if(strt(user_response)!=None):
                print('Bot:'+strt(user_response))
            else:
                sent_tokens.append(user_response)
                word_tokens= word_tokens+nltk.word_tokenize(user_response)
                final_words=list(set(word_tokens))
                print('Bot',end="")
                print(res(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print('chal [._.]')
                
                
                
                
                
                
                
                
                
                
                
                
                