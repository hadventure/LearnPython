import FreeSimpleGUI as sg

sg.theme("System Default 1")

label_src = sg.Text("Select files to compress")
input_src = sg.Input()
button_src = sg.FilesBrowse("Choose")

label_dest = sg.Text("Select destination folder")
input_dest = sg.Input()
button_dest = sg.FolderBrowse("Choose")

button_compress = sg.Button("Compress")

window = sg.Window("Compressor", layout=[
    [label_src, input_src, button_src],
    [label_dest, input_dest, button_dest],
    [button_compress]
])

window.read()
window.close()
