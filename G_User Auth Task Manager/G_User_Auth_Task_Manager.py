# Initialize an empty dictionary to store users and their tasks
user_database = {}
user_tasks = {}

# Utility functions for formatted outputs
def print_separator():
    print("=" * 50)

def print_header(title):
    print_separator()
    print(f"{title.center(50)}")
    print_separator()

# Step 2: Register a new user
def register_user():
    print_header("REGISTER NEW USER")
    username = input("Enter a username: ")
    if username in user_database:
        print("❌ Username already exists. Please choose another.")
        return
    password = input("Enter a password (at least 6 characters): ")
    if len(password) < 6:
        print("❌ Password must be at least 6 characters long!")
        return
    user_database[username] = {
        "password": password,
        "details": {"name": "", "address": "", "phone": "", "dob": ""}
    }
    print("✅ Registration successful!")

# Step 3: Log in an existing user
def login_user():
    print_header("USER LOGIN")
    username = input("Enter your username: ")
    if username not in user_database:
        print("❌ Username not found. Please register first.")
        return None
    password = input("Enter your password: ")
    if user_database[username]["password"] == password:
        print(f"✅ Welcome back, {username}!")
        user_dashboard(username)
    else:
        print("❌ Incorrect password! Please try again.")

# Step 4: Dashboard after successful login
def user_dashboard(username):
    while True:
        print_header(f"DASHBOARD - {username}")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Change Password")
        print("4. Manage Tasks")
        print("5. Logout")
        print_separator()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(username)
        elif choice == "2":
            update_profile(username)
        elif choice == "3":
            change_password(username)
        elif choice == "4":
            manage_tasks(username)
        elif choice == "5":
            print(f"Goodbye, {username}!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

# Step 5: View user profile
def view_profile(username):
    print_header("PROFILE")
    details = user_database[username]["details"]
    print(f"Username: {username}")
    print(f"Name: {details['name']}")
    print(f"Address: {details['address']}")
    print(f"Phone: {details['phone']}")
    print(f"Date of Birth: {details['dob']}")
    print_separator()

# Additional Feature: Update profile details
def update_profile(username):
    print_header("UPDATE PROFILE")
    name = input("Enter your full name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    user_database[username]["details"] = {
        "name": name,
        "address": address,
        "phone": phone,
        "dob": dob
    }
    print("✅ Profile updated successfully!")

# Step 6: Change password
def change_password(username):
    print_header("CHANGE PASSWORD")
    old_password = input("Enter your current password: ")
    if user_database[username]["password"] != old_password:
        print("❌ Incorrect current password! Password not changed.")
        return
    new_password = input("Enter a new password (at least 6 characters): ")
    if len(new_password) < 6:
        print("❌ Password must be at least 6 characters long!")
        return
    user_database[username]["password"] = new_password
    print("✅ Password updated successfully!")

# Step 8 (Task 2): Manage tasks for the logged-in user
def manage_tasks(username):
    if username not in user_tasks:
        user_tasks[username] = []

    while True:
        print_header("TASK MANAGEMENT")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Go Back")
        print_separator()
        choice = input("Enter your choice: ")

        if choice == "1":
            print_header("YOUR TASKS")
            tasks = user_tasks[username]
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks found.")
        elif choice == "2":
            task = input("Enter a new task: ")
            user_tasks[username].append(task)
            print("✅ Task added successfully!")
        elif choice == "3":
            print_header("UPDATE TASK")
            tasks = user_tasks[username]
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_index = int(input("Enter the task number to update: ")) - 1
                if 0 <= task_index < len(tasks):
                    new_task = input("Enter the updated task: ")
                    user_tasks[username][task_index] = new_task
                    print("✅ Task updated successfully!")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "4":
            print_header("DELETE TASK")
            tasks = user_tasks[username]
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"✅ Task '{removed_task}' deleted successfully!")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice! Please try again.")

# Step 7: Main program loop
def main():
    while True:
        print_header("USER AUTHENTICATION & TASK MANAGEMENT")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print_separator()
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
