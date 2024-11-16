import os
from os import environ
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyDIElChaei2YTjVLmAlWWuJ9XtQgdfXVDE"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
# genai.configure(api_key=environ.get("GOOGLE_API_KEY"))
pro = genai.GenerativeModel('models/gemini-pro')

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="You are a skincare expert, trying to listen to a customer's concerns and need for their skin, and recommend products to them. You are also aware of budget, quality, and reviews.",
)

history = []

print("Bot: Hello! How can I help you with your skincare needs today?")

while True:

	user_input = input("You: ")

	chat_session = model.start_chat(
		history=history
	)

	response = chat_session.send_message(user_input)
	model_response = response.text

	print(f'Bot: {model_response}')
	print()

	history.append({"role": "user", "parts": [user_input]})
	history.append({"role": "model", "parts": [model_response]})