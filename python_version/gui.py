import tkinter as tk
from tkinter import scrolledtext
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


# Placeholder chatbot function
def chatbot_response(ui):
    user_input = ui

    chat_session = model.start_chat(
        history=history
    )
    #print("reached model start chat")
    response = chat_session.send_message(user_input)
    model_response = response.text

    #print(f'Bot: {model_response}')
    print()
    to_return = "Bot: " + model_response
    #print(to_return)

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})
    
    return to_return

    

# GUI Application
def main():
    # Initialize window
    window = tk.Tk()
    window.title("Skincare Chatbot")
    window.geometry("600x500")
    
    # Chat display
    chat_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled', height=20)
    chat_display.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
    
    # User input
    user_input = tk.Entry(window, width=40)
    user_input.grid(column=0, row=1, padx=10, pady=10)

    def send_message():
        message = user_input.get().strip()
        if message:
            # Display user message
            chat_display['state'] = 'normal'
            chat_display.insert(tk.END, f"You: {message}\n")
            chat_display['state'] = 'disabled'
            chat_display.yview(tk.END)
            #print("Sent message " + message)

            # Get chatbot response
            response = chatbot_response(message)
            chat_display['state'] = 'normal'
            chat_display.insert(tk.END, f"{response}\n")
            chat_display['state'] = 'disabled'
            chat_display.yview(tk.END)
            
            # Clear input
            user_input.delete(0, tk.END)
    
    # Send button
    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.grid(column=1, row=1, padx=10, pady=10)
    
    # Run the application
    window.mainloop()

if __name__ == "__main__":
    main()
