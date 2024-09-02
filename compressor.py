import FreeSimpleGUI as sg
from zip_creator import make_archive

sg.theme("System Default 1")

label_src = sg.Text("Select files to compress")
input_src = sg.Input()
button_src = sg.FilesBrowse("Choose", key="files")

label_dest = sg.Text("Select destination folder")
input_dest = sg.Input()
button_dest = sg.FolderBrowse("Choose", key="folder")

button_compress = sg.Button("Compress")

output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Compressor", layout=[
    [label_src, input_src, button_src],
    [label_dest, input_dest, button_dest],
    [button_compress, output_label]
])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update("Compression completed.")

window.read()
window.close()
