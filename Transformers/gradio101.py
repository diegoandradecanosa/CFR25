# Solo funciona en local
import gradio as gr
from transformers import pipeline

def detect_sentiment(text):
    return "Hola"
    classifier = pipeline('sentiment-analysis')
    result = classifier(text)
    return result[0]['label']

iface = gr.Interface(fn=detect_sentiment, inputs="text", outputs="text")
iface.launch(share=True, debug=True)
