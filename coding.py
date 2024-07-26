#get key api from https://aistudio.google.com/app/apikey
#pip install google-generativeai
import os
import google.generativeai as genai


def ask_gemini(qu):
  genai.configure(api_key=os.environ["your_key_api"])

  # Create the model
  # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
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
  )

  chat_session = model.start_chat(
    history=[
    ]
  )

  response = chat_session.send_message(qu)
  return response.text
print(ask_gemini('gave me random names'))
