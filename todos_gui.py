import functions
import FreeSimpleGUI as sg

sg.theme("System Default 1")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 12))

# keeps the window open
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()
