"""
The links below were used to aid the writing of this code

https://www.geeksforgeeks.org/python-get-first-element-of-each-sublist/
https://www.geeksforgeeks.org/python-program-to-print-lines-\
    containing-given-string-in-file/

"""

# The tasks text file is opened using the variable "tasks"
with open("tasks.txt", "r+") as tasks_file:
    tasks = tasks_file.readlines()

    # A function is defined to return the username assigned to the task
    def get_user_assigned(tasks):
        username_assigned = [tasks_list.split(",")[0].strip() for tasks_list in tasks]
        return username_assigned

    # A function is defined to return the title of the task
    def get_task_title(tasks):
        task_title = [tasks_list.split(",")[1].strip() for tasks_list in tasks]
        return task_title

    # A function is defined to return the description of the task
    def get_task_description(tasks):
        task_description = [tasks_list.split(",")[2].strip() for tasks_list in tasks]
        return task_description

    # A function is defined to return the due date of the task
    def get_task_due_date(tasks):
        task_due_date = [tasks_list.split(",")[4].strip() for tasks_list in tasks]
        return task_due_date

    # A function is defined to return the current date
    def get_current_date(tasks):
        current_date = [tasks_list.split(",")[3].strip() for tasks_list in tasks]
        return current_date

    # A function is defined to return the completion status of the task
    def get_completed(tasks):
        completed = [tasks_list.split(",")[5].strip() for tasks_list in tasks]
        return completed

    # The user text file is opened with the variable "user_password"
    with open("user.txt", "r+") as user_file:
        user_password = user_file.readlines()

        # A function is defined to return the username in the user text file
        def get_username(user_password):
            username = [
                user_pass_list.split(",")[0] for user_pass_list in user_password
            ]
            return username

        # A function is defined to return the password in the user text file
        def get_password(user_password):
            password = [
                user_pass_list.split(",")[1].strip() for user_pass_list in user_password
            ]
            return password

        # The user is asked to input their username
        username_input = str(input("Please enter your username: ").lower())

        # A while loop is used to verify if the correct username has been entered
        while username_input not in get_username(user_password):
            if username_input not in get_username(user_password):
                print("Incorrect username entered, please try again")
                username_input = str(input("Please enter your username: ").lower())
            else:
                break

        # The user is asked to input their password
        password_input = str(input("Please enter your password: ").lower())

        # A while loop is used to verify if the correct password has been entered
        while password_input not in get_password(user_password):
            if password_input not in get_password(user_password):
                print("Incorrect password entered, please try again")
                password_input = str(input("Please enter your password: ").lower())
            else:
                print("Login successful!")

        # An if-else is used to verify if the user is an admin or not
        # An admin is displayed a different menu to non-admins
        while True:
            if username_input != "admin":
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

                # If the user is not an admin, they are unable to register new users
                if menu == "r":
                    print("You are not authorised to register new users")
                    print(
                        "Please use an admin login to complete this \
                          task"
                    )

                # Selecting "a" adds a new task to the tasks text file
                # The user is asked to input each required field
                # The inputted text is then written to the tasks text file
                elif menu == "a":
                    username_assigned_input = str(
                        input(
                            "Please enter the username of the person \
                                assigned to the task: "
                        )
                    ).lower()
                    task_title_input = str(
                        input("Please enter the title of the task: ")
                    ).lower()
                    task_description_input = str(
                        input(
                            "Please enter a short description of the \
                              task: "
                        )
                    ).lower()
                    task_due_date_input = str(
                        input(
                            "Please enter the task due date in the \
                                following format DD/MM/YYYY: "
                        )
                    )
                    current_date_input = str(
                        input(
                            "Please enter the current date in the \
                                following format DD/MM/YYYY: "
                        )
                    )
                    completed_input = str(
                        input(
                            "Is this task complete? Answer 'Yes' or \
                              'No': "
                        )
                    ).lower()
                    new_task = (
                        "\n"
                        + username_assigned_input
                        + ","
                        + task_title_input
                        + ","
                        + task_description_input
                        + ","
                        + task_due_date_input
                        + ","
                        + current_date_input
                        + ","
                        + "No"
                    )
                    tasks_file.write(new_task)
                    print("New task added")
                    break

                # Selecting "va" displays all tasks in the task text file
                # The tasks are printed in a user-friendly style
                elif menu == "va":
                    for task_title in get_task_title(tasks):
                        print("---------------------------")
                        print("Task:" + " " + get_task_title(tasks)[0])
                        break
                    for username_assigned in get_user_assigned(tasks):
                        print("Assigned to: " + " " + get_user_assigned(tasks)[0])
                        break
                    for current_date in get_current_date(tasks):
                        print("Date assigned: " + " " + get_current_date(tasks)[0])
                        break
                    for task_due_date in get_task_due_date(tasks):
                        print("Due date: " + " " + get_task_due_date(tasks)[0])
                        break
                    for completed in get_completed(tasks):
                        print("Task complete?" + " " + get_completed(tasks)[0])
                        break
                    for task_description in get_task_description(tasks):
                        print(
                            "Task description: "
                            + "\n"
                            + " "
                            + get_task_description(tasks)[0]
                        )
                        print("---------------------------")
                        break

                    for task_title in get_task_title(tasks):
                        print("---------------------------")
                        print("Task:" + " " + get_task_title(tasks)[1])
                        break
                    for username_assigned in get_user_assigned(tasks):
                        print("Assigned to: " + " " + get_user_assigned(tasks)[1])
                        break
                    for current_date in get_current_date(tasks):
                        print("Date assigned: " + " " + get_current_date(tasks)[1])
                        break
                    for task_due_date in get_task_due_date(tasks):
                        print("Due date: " + " " + get_task_due_date(tasks)[1])
                        break
                    for completed in get_completed(tasks):
                        print("Task complete?" + " " + get_completed(tasks)[1])
                        break
                    for task_description in get_task_description(tasks):
                        print(
                            "Task description: "
                            + "\n"
                            + " "
                            + get_task_description(tasks)[1]
                        )
                        print("---------------------------")
                        break

                # Selecting "vm" displays tasks assigned to the user
                # The tasks are printed in a user-friendly style
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

                # Selecting "e" exits the program
                elif menu == "e":
                    print("Goodbye!!!")
                    exit()

                # An error message is displayed if an incorrect input is entered
                else:
                    print(
                        "You have entered an invalid input. \
                          Please try again"
                    )

            # The user is shown a specific menu if they are an admin
            # An admin receives an extra menu option titled "s - statistics"
            # An admin is able to register new users to the tasks text file
            elif username_input == "admin":
                admin_menu = input(
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
                    + "s - statistics"
                    + "\n"
                    + "e - exit: "
                ).lower()

                # Selecting "r" registers new users to the tasks text file
                if admin_menu == "r":
                    new_username = str(
                        input(
                            "Please enter the new username:\
                                              "
                        )
                    ).lower()
                    new_password = str(
                        input(
                            "Please enter the new password:\
                                              "
                        )
                    ).lower()
                    new_password_confirm = str(
                        input("Please re-enter the new password: ")
                    ).lower()
                    while new_password != new_password_confirm:
                        print(
                            "The passwords entered do not match, \
                              please try again!"
                        )
                        new_password_confirm = str(
                            input("Please re-enter the new password: ")
                        ).lower()
                        break
                    while new_password == new_password_confirm:
                        registered_user = (
                            "\n" + new_username + "," + " " + new_password_confirm
                        )
                        user_file.write(registered_user)
                        print(
                            "Please exit the program to confirm \
                              registration"
                        )
                        break

                elif admin_menu == "a":
                    username_assigned_input = str(
                        input(
                            "Please enter the username of the person \
                                assigned to the task: "
                        )
                    ).lower()
                    task_title_input = str(
                        input("Please enter the title of the task: ")
                    ).lower()
                    task_description_input = str(
                        input(
                            "Please enter a short description of the \
                              task: "
                        )
                    ).lower()
                    task_due_date_input = str(
                        input(
                            "Please enter the task due date in the \
                                following format DD/MM/YYYY: "
                        )
                    )
                    current_date_input = str(
                        input(
                            "Please enter the current date in the \
                                following format DD/MM/YYYY: "
                        )
                    )
                    completed_input = str(
                        input(
                            "Is this task complete? Answer 'Yes' \
                              or 'No': "
                        )
                    ).lower()
                    new_task = (
                        "\n"
                        + username_assigned_input
                        + ","
                        + task_title_input
                        + ","
                        + task_description_input
                        + ","
                        + task_due_date_input
                        + ","
                        + current_date_input
                        + ","
                        + "No"
                    )
                    tasks_file.write(new_task)
                    print("New task added")
                    break

                elif admin_menu == "va":
                    for task_title in get_task_title(tasks):
                        print("---------------------------")
                        print("Task:" + " " + get_task_title(tasks)[0])
                        break
                    for username_assigned in get_user_assigned(tasks):
                        print("Assigned to: " + " " + get_user_assigned(tasks)[0])
                        break
                    for current_date in get_current_date(tasks):
                        print("Date assigned: " + " " + get_current_date(tasks)[0])
                        break
                    for task_due_date in get_task_due_date(tasks):
                        print("Due date: " + " " + get_task_due_date(tasks)[0])
                        break
                    for completed in get_completed(tasks):
                        print("Task complete?" + " " + get_completed(tasks)[0])
                        break
                    for task_description in get_task_description(tasks):
                        print(
                            "Task description: "
                            + "\n"
                            + " "
                            + get_task_description(tasks)[0]
                        )
                        print("---------------------------")
                        break

                    for task_title in get_task_title(tasks):
                        print("---------------------------")
                        print("Task:" + " " + get_task_title(tasks)[1])
                        break
                    for username_assigned in get_user_assigned(tasks):
                        print("Assigned to: " + " " + get_user_assigned(tasks)[1])
                        break
                    for current_date in get_current_date(tasks):
                        print("Date assigned: " + " " + get_current_date(tasks)[1])
                        break
                    for task_due_date in get_task_due_date(tasks):
                        print("Due date: " + " " + get_task_due_date(tasks)[1])
                        break
                    for completed in get_completed(tasks):
                        print("Task complete?" + " " + get_completed(tasks)[1])
                        break
                    for task_description in get_task_description(tasks):
                        print(
                            "Task description: "
                            + "\n"
                            + " "
                            + get_task_description(tasks)[1]
                        )
                        print("---------------------------")
                        break

                elif admin_menu == "vm":
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
                elif admin_menu == "s":
                    print("Total number of users: " + str(len(user_password)))
                    print("Total number of tasks: " + str(len(tasks)))

                elif admin_menu == "e":
                    print("Goodbye!!!")
                    exit()

                else:
                    print(
                        "You have entered an invalid input. \
                          Please try again"
                    )
