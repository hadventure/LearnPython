user_prompt = f"Please enter a todo: \n"

while True:
    user_action = input("Type add, show, edit or exit \n")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input(user_prompt)

            file = open("todos.txt", "a+")
            todos = file.readlines()
            file.close()

            todos.append(f"{todo}\n")

            file = open("todos.txt", "a+")
            file.writelines(todos)
            file.close()
        case "show" | "display":
            file = open("todos.txt", "r")
            todos = file.readlines()

            print(todos)

            file.close()
        case "edit":
            number = int(input("Enter todos number"))
            number = number - 1
            new_todo = input("Enter updated todo")
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter completed number"))
            todos.pop(number - 1)
        case "exit":
            break
        case _:
            print("Invalid input")

print("Buy")
