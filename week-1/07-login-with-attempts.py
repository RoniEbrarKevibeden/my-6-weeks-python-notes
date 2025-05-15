# Define account information
account = {
    "username": "Roni",
    "password": "roni_secure_2025",
    "is_admin": False
}

# Allow the user 3 login attempts
attempts = 3

while attempts > 0:
    input_username = input("Enter your username: ").strip()
    input_password = input("Enter your password: ").strip()

    if input_username == account["username"] and input_password == account["password"]:
        print("Login successful!")
        if account["is_admin"]:
            print("Welcome, Admin!")
        else:
            print("Welcome, User!")
        break
    else:
        attempts -= 1
        print("Wrong username or password.")
        print(f"Remaining attempts: {attempts}")

if attempts == 0:
    print("Too many failed attempts. Access denied.")
