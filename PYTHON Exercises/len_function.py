def get_length(text):
    if not isinstance(text, str):
        return "Invalid input"

    return len(text)


text = "Hello World"

result = get_length(text)
print("Length:", result)