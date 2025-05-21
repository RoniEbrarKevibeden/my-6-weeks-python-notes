# FUNCTIONS - BASICS

# 01 - Basic Functions
def say_hello():
    print("Hello, Roni")

def greet():
    print("Welcome, future cybersecurity expert!")

# Function with parameter
def greet_person(name):
    print(f"Hello, {name}")

# Calling functions
say_hello()
greet()
greet_person("Alice")
greet_person("Roni")

# FUNCTIONS WITH RETURN

# 02 - Return Values

def add(x, y):
    return x + y

def multiply(a, b):
    return a * b

sum_result = add(3, 5)
product_result = multiply(4, 6)

print("Sum:", sum_result)
print("Product:", product_result)

# DEFAULT PARAMETERS

# 03 - Default Parameters

def greet_with_default(name="Guest"):
    print(f"Hello, {name}")

greet_with_default("Roni")
greet_with_default()

def welcome(name="friend"):
    return f"Welcome, {name}"

print(welcome("Alice"))
print(welcome())

# FUNCTIONS WITH CONDITIONS (IF STATEMENTS)

def check_age(age):
    if age >= 18:
        return "You can vote."
    else:
        return "You are too young to vote."

print(check_age(20))
print(check_age(15))

def check_price(price):
    if price >= 100:
        return "You can buy this T-shirt."
    else:
        return "You can't buy it, unfortunately..."

print(check_price(300))
print(check_price(25))

# COMBINED FUNCTION INPUT/OUTPUT

def greet_input(name):
    return f"Hello, {name}!"

def check_age_input(age):
    if age >= 18:
        return "You can vote."
    else:
        return "You are too young to vote."

# Get input from user
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(greet_input(user_name))
print(check_age_input(user_age))

# FUNCTION TO DISPLAY USER INFO

def show_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

show_info("Roni", 20)
