# login.py
def login(username, password):
    # 假设用户名为admin，密码为1234
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Invalid credentials"
