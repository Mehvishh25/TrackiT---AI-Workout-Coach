    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Explain how AI works"}]
    }]
   }'


AIzaSyB8BSwusQcrtB_RFa2T4LVZKyppWM9_IiA


AIzaSyBkGqQkHPoDx0gHNfCrEHeeagZcXHsMu-s

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["AIzaSyB8BSwusQcrtB_RFa2T4LVZKyppWM9_IiA"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)



My Project 64818