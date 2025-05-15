# Define a user account dictionary
account = {
    "username": "Roni",
    "password": "1234",
    "is_admin": False
}

# Display user info
print("Username:", account["username"])
print("Is Admin:", account["is_admin"])

# Update account info
account["password"] = "roni_secure_2025"
account["email"] = "roni@cybermail.com"
del account["is_admin"]

# Print updated account
print("\nUpdated account info:")
for key in account:
    print(f"{key}: {account[key]}")