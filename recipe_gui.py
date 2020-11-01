import PySimpleGUI as sg 
import recipe

layout = [
    [sg.Text("First select whether you want takeout or not. Then click on one of the buttons below it.")],
    [sg.Text("Takeout?"), sg.Checkbox("Yes", key="YES"), sg.Checkbox("No", key="NO")],
    [sg.Button('Randomly Select 5 Meals'), sg.Button('Hit Up Walmart'), sg.Button('Exit')],
    [sg.Text('1. '), sg.In(key = 1)],
    [sg.Text('2. '), sg.In(key = 2)],
    [sg.Text('3. '), sg.In(key = 3)],
    [sg.Text('4. '), sg.In(key = 4)],
    [sg.Text('5. '), sg.In(key = 5)] 
]

window = sg.Window('Meal Planner', layout, size = (750, 350))

takeout = False

while True:
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Randomly Select 5 Meals':
        if values['YES']:
            takeout = True
        recipes = recipe.main(takeout)
        output_list = []
        for recipe in recipes:
            #output_str = ""
            if recipe == "Takeout":
                title = recipe
            else:
                title, ingredients = recipe[1], recipe[3]
            output_list.append(title)
        for index in range(1, 6):
            window[index].update(output_list[index - 1])
        
       


