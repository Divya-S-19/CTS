def validate_login(user, pwd):
    if user == "" or pwd == "":
        return "Username or Password cannot be empty"

    if user == "admin":
        if pwd == "pass123":
            return "Login Successful"
        else:
            return "Invalid Password"
    else:
        return "Invalid Username"


user = "admin"
pwd = "pass123"

result = validate_login(user, pwd)
print(result)