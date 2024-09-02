"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from deep_translator import GoogleTranslator

API_KEY = "AIzaSyCkA89AIhu_F2A2ONWXUgMjSJcQaQlxy_Q"

def ai_plan(text):
    genai.configure(api_key=API_KEY)

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction="You are a personal trainer. Your learner gives information about themselves and the workout plan they want. Give them a detailed workout plan based on their needs.",
    )

    chat_session = model.start_chat(
    history=[
    ]
    )

    translated_text = translate('auto', 'en', text)

    response = chat_session.send_message(translated_text)

    translated_result = translate('auto', 'fa', response.text)

    return translated_result


def translate(source, target, text):
    translated = GoogleTranslator(source=source, target=target).translate(text)
    return translated.lower()
