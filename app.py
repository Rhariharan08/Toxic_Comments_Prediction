import streamlit as st
import pickle 
import numpy as np 
import transformers
import tensorflow
from keras import *


def encode(data, tokenizer, max_length=150):
    encoded_data = tokenizer.batch_encode_plus(
        data,
        max_length=max_length,
        padding='max_length',
        truncation=True,
        return_tensors='tf'
    )
    return encoded_data['input_ids'], encoded_data['attention_mask']
    
def load_tokenizer():
    tokenizer_load = pickle.load(open("bert_tokenizer.pkt", "rb"))
    return tokenizer_load

def load_model():
    model_load = pickle.load(open("toxicity_model.pkt", "rb"))
    return model_load

def toxicity_prediction(text):
    tokenizer = load_tokenizer()
    comment_ids,comment_mask  = encode([text], tokenizer)
    nb_model = load_model()
    prediction = nb_model.predict(comment)
    prediction = prediction[0][0]
    if prediction > 0.73:
    	return"Toxic"  
    return "Non-Toxic"

st.header("Toxicity Detection App")

st.subheader("Input your text")

text_input = st.text_input("Enter your text")

if text_input is not None:
    if st.button("Analyse"):
        result = toxicity_prediction(text_input)
        st.subheader("Result:")
        st.info("The result is "+ result + ".")
