import tkinter as tk
from tkinter import scrolledtext
import tkinter.font
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
    print("reached model start chat")
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
    window.title("AI Chatbot")
    window.geometry("800x500")
    window.configure(bg="#ffe6f3")

    title_label = tk.Label(window, text="AI Skincare Chatbot", bg="#ffe6f3", fg="#a10067")
    title_label.grid(column=0, row=0, columnspan=2, pady=10)

    
    # Chat display
    chat_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled', height=20)
    chat_display.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
    chat_display['state'] = 'normal'
    chat_display.insert(tk.END, f"Bot: Hello, I am your skincare expert, here to help you with any concerns or questions you have about skincare. I can tell you about specific products, their benefits, pricing, and other concerns! Ask away!")
    chat_display['state'] = 'disabled'
    chat_display.yview(tk.END)
    
    # User input
    #user_input = tk.Entry(window, width=40)
    #user_input.grid(column=0, row=1, padx=10, pady=10)
    user_input = tk.Entry(window, width=40, bg="#ffe6f3", fg="#4b0042", relief="flat", highlightthickness=2, highlightbackground="#a10067")
    user_input.grid(column=0, row=2, padx=10, pady=10)

    def send_message():
        message = user_input.get().strip()
        if message:
            # Display user message
            chat_display['state'] = 'normal'
            chat_display.insert(tk.END, f"You: {message}\n\n")
            chat_display['state'] = 'disabled'
            chat_display.yview(tk.END)
            #print("Sent message " + message)

            # Get chatbot response
            response = chatbot_response(message)
            #new_response = custom_formating(response);
            chat_display['state'] = 'normal'
            chat_display.insert(tk.END, f"{response}\n\n")
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
