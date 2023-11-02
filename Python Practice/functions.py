FILEPATH = "to_dos.txt"

def get_todos(filepath=FILEPATH):
    """read the text file and return the list of to-dos"""
    with open(filepath, 'r') as file:
            to_do_list_local = file.readlines()
    return to_do_list_local


def write_todos(todos_arg, filepath=FILEPATH):
    """write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
            file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
