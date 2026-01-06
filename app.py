import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

#load lstm model
model=load_model('next_word_lstm.h5')

#load tokenizer
with open('tokenizer.pickle','rb') as handle:
    tokenizer=pickle.load(handle)

#function to predict next word
def predict_next_word(model,tokenizer,text,max_sequence_len):
    sequence=tokenizer.texts_to_sequences([text])[0]
    sequence=pad_sequences([sequence],maxlen=max_sequence_len-1,padding='pre')
    predicted_probs=model.predict(sequence,verbose=0)
    predicted_index=np.argmax(predicted_probs,axis=-1)[0]
    
    for word, index in tokenizer.word_index.items():
        if index==predicted_index:
            return word
    return None

#streamlit app
st.title("Next Word Prediction using LSTM & Early Stopping")
input_text=st.text_input("Enter a sequence of words:", 'to be or not to be')
if st.button("Predict Next Word"):
    max_sequence_len=model.input_shape[1]+1 #+1 for the next word
    next_word=predict_next_word(model,tokenizer,input_text,max_sequence_len)
    st.write(f"Predicted Next Word: **{next_word}**")