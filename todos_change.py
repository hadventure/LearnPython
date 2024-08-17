user_prompt = "Please enter a todo: "

todos = []

while True:
    user_action = input("Type add, show or exit")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input(user_prompt)
            todos.append(todo)
        case "show" | "display":
            print(todos)
            for todo in todos:
                print(todo)
        case "exit":
            break
        case _:
            print("Invalid input")

print("Buy")
