user_prompt = "Please enter a todo: "

todos = []

while True:
    user_action = input("Type add, show, edit or exit")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input(user_prompt)
            todos.append(todo)
        case "show":
            print(todos)
            for todo in todos:
                print(todo)
        case "edit":
            number = int(input("Enter todos number"))
            number = number - 1
            new_todo = input("Enter updated todo")
            todos[number] = new_todo
        case "exit":
            break
        case _:
            print("Invalid input")

print("Buy")
