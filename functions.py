
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ read a text file and return the list of             #doc string for code documentation
    to-do items"""
    with open(filepath, 'r') as file_local:     #open() call which is builtin in python interpreter (.exe written in C language)
        todos_local = file_local.readlines()       #todos in this line is local variable    # with as context manager, no need to close file
    return todos_local

#print(help(get_todos))
def write_todos(todos_arg, filepath=FILEPATH ):
    """write a tobedone items list in the test file"""
    with open(filepath, 'w') as file_local:     #open() call which is builtin in python interpreter (.exe written in C language)
        file_local.writelines(todos_arg)   #todos in this line is local variable    # with as context manager, no need to close file
#print("name is =", __name__)
if __name__ == "__main__":    #__name__ wil be main if run independently and will be the actual file name if it is run from origin function from where it is called
    print("Hello")
    print(get_todos())
