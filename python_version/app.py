# hello_psg.py

import PySimpleGUI as sg

layout = [
    [sg.Text("Hello! I'm your Skincare Helper!", font=('Poppins', 20))],
    [sg.Text("Let's find the perfect product for you", font=('Poppins', 15))],

    [sg.Text("What is your skin type?", font=('Poppins', 12))],
    [sg.Combo(['Oily', 'Dry', 'Combination', 'Sensitive'], key='-SKIN_TYPE-', font=('Poppins', 12))],
    
    [sg.Text("What is your main skincare concern?", font=('Poppins', 12))],
    [sg.Combo(['Acne', 'Wrinkles', 'Hyperpigmentation', 'Dryness'], key='-CONCERN-', font=('Poppins', 12))],
    
    [sg.Text("What's your budget?", font=('Poppins', 12))],
    [sg.Combo(['Under $20', '$20 - $50', '$50 - $100', 'Above $100'], key='-BUDGET-', font=('Poppins', 12))],
    
    [sg.Button('Get Recommendations', font=('Poppins', 12), size=(20, 2))]
]

# Create the window
window = sg.Window('Skincare Helper', layout, size=(400,400))

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
