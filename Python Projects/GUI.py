import functions
import PySimpleGUI as sg

# objects & display
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todoItems', enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 10))

# executing the program
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todoItems'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo.title())
            functions.write_todos(todos)
            window['todoItems'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todoItems'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todoItems'].update(values=todos)

        case "Complete":
            todo_to_complete = values['todoItems'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todoItems'].update(values=todos)
            window['todo'].update(value='')

        case "Exit":
            break

        case 'todoItems':
            window['todo'].update(value=values['todoItems'][0])
        case sg.WIN_CLOSED:
            break

window.close()
