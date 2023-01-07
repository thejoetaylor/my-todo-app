FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):  # define a function for repetitive actions
    """ Read a text file and return the list of
    to-do items
    """
    with open(filepath, "r") as file_local:  # open file specified in filepath argument and read
        # the contents and close the file
        todos_local = file_local.readlines()  # create the list object "todos" from
        # the contents of the file that was read
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open("todos.txt", "w") as file:  # opens and closes file
        file.writelines(todos_arg)  # write the todos list to the file


if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())


def count(phrase):
    return phrase.count('.')
