user_prompt = f"Please enter a todo: \n"


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


while True:
    user_action = input("Type add, show, edit or exit \n")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = input(user_prompt)

        todos = get_todos()
        todos.append(f"{todo}\n")

        write_todos(todos_arg=todos)
    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        new_todos = []
        new_todos = [item.strip("\n") for item in todos]

        for index, todo in enumerate(new_todos):
            print(f"{index + 1}. {todo}")
    elif user_action.startswith("edit"):
        try:
            number = int(input("Enter todos number"))
            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter updated todo") + "\n"

            todos[number] = new_todo

            write_todos(todos)
        except ValueError:
            print("Command is not valid")
            user_action = input("Type add, show, edit or exit \n")
            user_action = user_action.strip()
    elif user_action.startswith("complete"):
        try:
            number = int(input("Enter completed number"))

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed"
        except IndexError:
            print("There is no item with that index")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid input")
print("Buy")
