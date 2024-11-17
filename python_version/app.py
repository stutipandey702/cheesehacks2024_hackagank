import PySimpleGUI as sg

# Path to the Poppins font file (replace with your actual path)
font_path = "/path/to/Poppins-Regular.ttf"

# Layout with purply-pink mauve color and cute Poppins font
layout = [
    [sg.Text("Hello! I'm your Skincare Helper!", font=(font_path, 20), text_color='white', background_color='#D1A1C7')],
    [sg.Text("Let's find the perfect product for you", font=(font_path, 15), text_color='white', background_color='#D1A1C7')],
    
    [sg.Text("What is your skin type?", font=(font_path, 12), text_color='white', background_color='#D1A1C7')],
    [sg.Combo(['Oily', 'Dry', 'Combination', 'Sensitive'], key='-SKIN_TYPE-', font=(font_path, 12), background_color='#D1A1C7', text_color='white')],
    
    [sg.Text("What is your main skincare concern?", font=(font_path, 12), text_color='white', background_color='#D1A1C7')],
    [sg.Combo(['Acne', 'Wrinkles', 'Hyperpigmentation', 'Dryness'], key='-CONCERN-', font=(font_path, 12), background_color='#D1A1C7', text_color='white')],
    
    [sg.Text("What's your budget?", font=(font_path, 12), text_color='white', background_color='#D1A1C7')],
    [sg.Combo(['Under $20', '$20 - $50', '$50 - $100', 'Above $100'], key='-BUDGET-', font=(font_path, 12), background_color='#D1A1C7', text_color='white')],
    
    [sg.Button('Get Recommendations', font=(font_path, 12), size=(20, 2), button_color=('white', '#D1A1C7'))]
]

# Create the window with purply-pink mauve background and white text
window = sg.Window('Skincare Helper', layout, size=(400, 400), background_color='#D1A1C7')

# Create an event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Get Recommendations':
        skin_type = values['-SKIN_TYPE-']
        concern = values['-CONCERN-']
        budget = values['-BUDGET-']
        
        sg.popup(f"Skin Type: {skin_type}\nConcern: {concern}\nBudget: {budget}")


window.close()
