def write_file():
    with open("greeting.txt", "w") as file:
        file.write("Hello World")
    
    print("File written successfully")


write_file()