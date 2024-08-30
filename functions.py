def get_todos(filepath="todos.txt"):
    """
    Read a text file and return the list of.
    """
    with open(filepath, "a+") as file_local:
        file_local.seek(0)
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """
    Read a text file and return the list of.
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


