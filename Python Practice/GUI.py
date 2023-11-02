import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")

window = sg.Window('To-Do App', layout=[[label, input_box, add_button]])
window.read()
window.close()
