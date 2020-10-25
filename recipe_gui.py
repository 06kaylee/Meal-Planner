import PySimpleGUI as sg 
import recipe

layout = [
    [sg.MLine(size=(80,20), key='OUTPUT')],
    [sg.Button('Randomly Select 5 Meals'), sg.Button('Hit Up Walmart'), sg.Button('Exit')]
]

window = sg.Window('Meal Planner', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Randomly Select 5 Meals':
        recipes = recipe.main();
        output_str = ""
        for recipe in recipes:
            title, ingredients = recipe[1], recipe[3]
            output_str += f"{title}: {ingredients}\n\n"
        window['OUTPUT'].update(output_str)

window.close()