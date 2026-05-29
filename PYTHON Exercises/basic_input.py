def greet_user():
    name = input("Enter your name: ").strip()

    if name == "":
        print("Name cannot be empty")
    else:
        print(f"Hello, {name}!")


greet_user()