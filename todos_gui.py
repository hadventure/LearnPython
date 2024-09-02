import functions
import FreeSimpleGUI as sg

sg.theme("System Default 1")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")

window = sg.Window("App", layout=[label, input_box, add_button])
window.read()
window.close()
