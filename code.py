# Define functions for each number from 0 to 9
def zero():
    return 0
def one():
    return 1
def two():
    return 2
def three():
    return 3
def four():
    return 4
def five():
    return 5
def six():
    return 6
def seven():
    return 7
def eight():
    return 8
def nine():
    return 9

# Define functions for each mathematical operation
def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def times(a, b):
    return a * b
def divided(a, b):
    return a // b

# User class to store user information
class User:
    def __init__(self, name, role, email, password):
        self.name = name
        self.role = role
        self.email = email
        self.password = password

# Store all users in a list
users = []

# Sign up function for both master and student
def sign_up():
    name = input("Enter your name: ")
    role = input("Enter your role (master or student): ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    users.append(User(name, role, email, password))
    print("Sign up successful.")

# Login function for both master and student
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    for user in users:
        if user.email == email and user.password == password:
            print("Login successful.")
            if user.role == "master":
                master_actions(user)
            elif user.role == "student":
                student_actions(user)
            return
    print("Login failed. Invalid email or password.")

# Logout function for both master and student
def logout():
    print("Logout successful.")

# Actions for master
def master_actions(user):
    while True:
        print("What do you want to do?")
        print("1. Ask a student")
        print("2. Logout")
        option = int(input("Enter your choice: "))
        if option == 1:
            ask_student(user)
        elif option == 2:
            logout()
            break

# Ask a student function
def ask_student(user):
    calculation = input("Enter your calculation: ")
    result = eval(calculation)
    print("Result:", result)

# Actions for student
def student_actions(user):
    while True:
        print("What do you want to do?")
        print("1. View activity log")
        print("2. Logout")
        option = int(input("Enter your choice: "))
        if option == 1:
            view_activity_log(user)
        elif option == 2:
            logout()
            break

# View activity log function for student
def view_activity_log(user):
    print("Activity log for student", user.name)
    # Code to retrieve activity log from database

# Main function
def main():
    while True:
        print("What do you")
