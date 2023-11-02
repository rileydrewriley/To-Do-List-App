# To-Do list
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_to_do = input("would you like to add, show, edit, complete or exit: ")
    user_to_do = user_to_do.strip()

    if 'add' in user_to_do:
        to_do = user_to_do[4:]
        to_do = to_do.title()

        to_do_list = functions.get_todos()

        to_do_list.append(to_do + '\n')

        functions.write_todos(to_do_list, 'to_dos.txt')

    elif 'show' in user_to_do:
        to_do_list = functions.get_todos()

        new_to_do_list = [item.strip("\n") for item in to_do_list]

        for index, item in enumerate(new_to_do_list):
            row = f"{index + 1} - {item}"
            print(row)

    elif 'edit' in user_to_do:
        user_edit = input("Would you like to remove or replace a to-do? ")
        user_edit.strip()
        if 'remove' in user_edit:
            to_do_list = functions.get_todos()
            remove_request = input("What number to-do would you like to remove? ")
            remove_to_do = int(remove_request) - 1
            to_do_list.pop(remove_to_do)

            functions.write_todos('to_dos.txt', to_do_list)

            message = f"{remove_request} was removed."
            print(message)


        if 'replace' in user_edit:
            to_do_list = functions.get_todos()

            replace_to_do = int(input("What number to-do would you like to replace? ")) - 1
            new_to_do = input("What to-do would you like to add instead? ")
            new_to_do = new_to_do.title()
            to_do_list[replace_to_do] = new_to_do + '\n'

            functions.write_todos('to_dos.txt', to_do_list)
    elif 'complete' in user_to_do:
        try:
            complete_to_do = input("What to-do have you completed?: ")
            complete_to_do = complete_to_do.title()
            to_do_list.remove(complete_to_do)
        except NameError:
            print("There is no item with that number! Try again!")
    elif 'exit' in user_to_do:
        break


print("Bye!")

