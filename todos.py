user_prompt = f"Please enter a todo: \n"

while True:
    user_action = input("Type add, show, edit or exit \n")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = input(user_prompt)

        with open("todos.txt", "a+") as file:
            todos = file.readlines()

        todos.append(f"{todo}\n")

        file = open("todos.txt", "a+")
        file.writelines(todos)
        file.close()
    elif user_action.startswith("show"):
        file = open("todos.txt", "r")
        todos = file.readlines()
        file.close()

        new_todos = []
        new_todos = [item.strip("\n") for item in new_todos]

        for index, todo in enumerate(todos):
            print(f"{index}. {todo}")
    elif user_action.startswith("edit"):
        try:
            number = int(input("Enter todos number"))
            number = number - 1
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            print(todos)

            new_todo = input("Enter updated todo") + "\n"

            todos[number] = new_todo

            print(todos)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Command is not valid")
            user_action = input("Type add, show, edit or exit \n")
            user_action = user_action.strip()
    elif user_action.startswith("complete"):
        try:
            number = int(input("Enter completed number"))

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed"
        except IndexError:
            print("There is no item with that index")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid input")
print("Buy")
