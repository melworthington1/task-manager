# The datetime module is imported to display the current date
# The date string is manipulated to match the dates displayed in the tasks text file
from datetime import datetime

date_today = datetime.today()
date_formatted = date_today.strftime("%d %b %Y")

# The tasks text file is opened using the variable "tasks_file"
# The tasks file is then read with the "tasks" variable
with open("tasks.txt", "r+") as tasks_file:
    tasks = tasks_file.readlines()

# The user text file is opened with the variable "user_password"
# The user file is then read with the "user_password" variable
with open("user.txt", "r+") as user_file:
    user_password = user_file.readlines()
    login_dict = {}
    for login in user_password:
        username, password = login.split(",")
        username = username.strip()
        password = password.strip()
        login_dict[username] = password


# A function is defined to read and manipulate each line into a list
def get_task():
    with open("tasks.txt", "r+") as tasks_file:
        tasks = tasks_file.readlines()
        tasks_list = [tasks_list.strip().split(",") for tasks_list in tasks]
        return tasks_list


# User is asked to enter their username
username_input = str(input("Please enter your username: ").lower())

# A while loop is used to validate if the username inputted exists within the program/user text file
while username_input not in login_dict.keys():
    if username_input not in login_dict.keys():
        print("User does not exist")
        username_input = str(input("Please enter your username: ").lower())
    else:
        break

# User is asked to enter their password
password_input = str(input("Please enter your password: ").lower())

# An if-elif is used to validate if the password entered is correct
# The if-elif also validates if the password entered matches the username
if password_input not in login_dict.values():
    print("Incorrect password entered")
    password_input = str(input("Please enter your password: ").lower())
elif username_input in login_dict.keys() and password_input == login_dict[username]:
    print(f"Welcome {username}")

while True:
    menu = input(
        "Select one of the following options:"
        + "\n"
        + "r - register a user"
        + "\n"
        + "a - add task"
        + "\n"
        + "va - view all tasks"
        + "\n"
        + "vm - view my tasks"
        + "\n"
        + "e - exit: "
    ).lower()

    if menu == "r":
        if username_input != "admin":
            print("You are not authorised to register new users")
            print("Please use an admin login to complete this task")
        elif username_input == "admin":
            with open("user.txt", "r+") as user_file:
                user_password = user_file.readlines()
                new_username = str(input("Please enter the new username: ")).lower()
                new_password = str(input("Please enter the new password: ")).lower()
                new_password_confirm = str(
                    input("Please re-enter the new password: ")
                ).lower()
                if new_password != new_password_confirm:
                    print("The passwords entered do not match, please try again!")
                    new_password_confirm = str(
                        input("Please re-enter the new password: ")
                    ).lower()
                    break
                elif new_password == new_password_confirm:
                    registered_user = (
                        "\n" + new_username + "," + " " + new_password_confirm
                    )
                    user_file.write(registered_user)
                    print("New user registered")
                    pass

    elif menu == "a":
        with open("tasks.txt", "r+") as tasks_file:
            tasks = tasks_file.readlines()
            username_assigned_input = str(
                input("Please enter the username of the person assigned to the task: ")
            ).lower()
            task_title_input = str(
                input("Please enter the title of the task: ")
            ).lower()
            task_description_input = str(
                input("Please enter a short description of the task: ")
            ).lower()
            task_due_date_input = str(
                input(
                    "Please enter the task due date in the following format DD/MM/YYYY: "
                )
            )

            # The inputted due date is formatted to match the task file date format
            due_date_format = datetime.strptime(task_due_date_input, "%d/%m/%Y")
            due_date_formatted = datetime.strftime(due_date_format, "%d %b %Y")

            new_task = (
                "\n"
                + username_assigned_input
                + ","
                + " "
                + task_title_input
                + ","
                + " "
                + task_description_input
                + ","
                + " "
                + due_date_formatted
                + ","
                + " "
                + date_formatted
                + ","
                + " "
                + "No"
            )

            # The new task is written to the task file
            tasks_file.write(new_task)
            print("New task added")
            pass

    elif menu == "va":
        index = 0
        print("------------------")
        if index < len(get_task()):
            for index, task_field in enumerate(get_task()):
                if index == 0:
                    print(
                        f"Task: {task_field[1]}\nAssigned to: {task_field[0]}\nDate assigned: {task_field[4]}\nDue date: {task_field[3]}\nTask complete?: {task_field[5]}\nTask description:\n{task_field[2]}"
                    )
                    print("------------------")
                else:
                    index = index + 1
                    print(
                        f"Task: {task_field[1]}\nAssigned to: {task_field[0]}\nDate assigned: {task_field[4]}\nDue date: {task_field[3]}\nTask complete?: {task_field[5]}\nTask description:\n{task_field[2]}"
                    )
                    print("------------------")

    elif menu == "vm":
        try:
            user_check = []
            idx = 0

            for task in tasks:
                if username_input in task:
                    user_check.insert(idx, task)
                    idx += 1
            if len(user_check) == 0:
                print(
                    "User does not have any tasks \
                                  assigned!"
                )
            else:
                user_found = len(user_check)
                print("Your assigned tasks: ")
                for i in range(user_found):
                    personal_tasks = user_check[i].split(",")
                    print("---------------------------")
                    print(
                        "Task: "
                        + personal_tasks[1]
                        + "\n"
                        + "Date assigned: "
                        + personal_tasks[3]
                        + "\n"
                        + "Due date: "
                        + personal_tasks[4]
                        + "\n"
                        + "Task complete?: "
                        + personal_tasks[5]
                        + "\n"
                        + "Task description: "
                        + personal_tasks[2]
                    )
                    print("---------------------------")
                print()
        except:
            print("User has no tasks assigned!")

    # Selecting "s" displays the total users and tasks
    elif menu == "s":
        if username_input != "admin":
            print("This option is for admins only!")
        elif username_input == "admin":
            print("Total number of users: " + str(len(user_password)))
            print("Total number of tasks: " + str(len(tasks)))

    # Selecting "e" exits the program
    elif menu == "e":
        print("Goodbye!!!")
        exit()

    # An error message is displayed if an incorrect input is entered
    else:
        print("You have entered an invalid input. Please try again")
