import tkinter as tk
from tkinter import messagebox
import json
import re


def login_window():
    """Initialize the main window"""
    # Main window settings
    main_window = tk.Tk()
    main_window.title("Login")
    main_window.resizable(width=0, height=0)

    # Main window contents items
    login_prompt = tk.Label(main_window, text="""Please enter your username and password to login:""")
    username_label = tk.Label(main_window, text="Username:")
    username_entry = tk.Entry(main_window, bg="white", width=20, borderwidth=2)
    password_label = tk.Label(main_window, text="Password:")
    password_entry = tk.Entry(main_window, bg="white", width=20, borderwidth=2, show="*")
    show_password_button = tk.Button(main_window, text="Show", width=4, relief="raised")
    sign_in_button = tk.Button(main_window, text="Sign In", width=10, relief="raised")
    sign_up_button = tk.Button(main_window, text="Sign Up", width=10, relief="raised")

    # Main window contents placement
    login_prompt.grid(row=0, column=0, columnspan=4, pady=5)
    username_label.grid(row=1, column=1)
    username_entry.grid(row=1, column=2, padx=10, pady=5)
    password_label.grid(row=2, column=1)
    password_entry.grid(row=2, column=2, padx=10, pady=5)
    show_password_button.grid(row=2, column=3, padx=5)
    sign_in_button.grid(row=3, column=2, padx=10, pady=5)
    sign_up_button.grid(row=3, column=1, padx=25, pady=5)

    # Show/Hide password button
    show_password_button.bind('<ButtonPress-1>', lambda event: password_entry.config(show=""))
    show_password_button.bind('<ButtonRelease-1>', lambda event: password_entry.config(show="*"))

    # Sign In Button --> check_credentials function  /  Sign Up Button --> sign_up_window function
    sign_in_button.bind('<ButtonRelease-1>', lambda event: check_credentials(username_entry.get(),
                                                                             password_entry.get(),
                                                                             main_window))

    sign_up_button.bind('<ButtonRelease-1>', lambda event: sign_up_window(main_window))

    main_window.mainloop()


def check_credentials(username, password, main_window):
    with open('user_logs.txt', 'r') as user_logs:
        user_info = json.load(user_logs)
        for user in user_info:
            if user['username'] == username:
                if user['password'] == password:
                    tk.messagebox.showinfo(title="Welcome", message="Log in successful!")
                    main_window.destroy()
                    break
        else:
            tk.messagebox.showerror(title="Error", message="Incorrect username or password.")


def sign_up_window(main_window):
    # Window settings
    register_window = tk.Toplevel(main_window)
    register_window.title("Sign Up")
    register_window.resizable(width=0, height=0)
    register_window.focus()
    register_window.grab_set()

    # Contents
    signup_prompt = tk.Label(register_window, text="Please enter the following information:", padx=10, pady=10)
    new_email_label = tk.Label(register_window, text="Email:")
    new_email_entry = tk.Entry(register_window, bg="white", width=20, borderwidth=2)
    new_username_label = tk.Label(register_window, text="Username:")
    new_username_entry = tk.Entry(register_window, bg="white", width=20, borderwidth=2)
    new_password_label = tk.Label(register_window, text="Password:")
    new_password_entry = tk.Entry(register_window, bg="white", width=20, borderwidth=2, show="*")
    reenter_new_password_label = tk.Label(register_window, text="Re-enter password:")
    reenter_new_password_entry = tk.Entry(register_window, bg="white", width=20, borderwidth=2, show="*")
    new_sign_up_button = tk.Button(register_window, text="Sign Up", width=10, relief="raised")

    # Contents placement
    signup_prompt.grid(row=0, column=1, columnspan=2)
    new_email_label.grid(row=1, column=1)
    new_email_entry.grid(row=1, column=2, padx=10, pady=5)
    new_username_label.grid(row=2, column=1)
    new_username_entry.grid(row=2, column=2, padx=10, pady=5)
    new_password_label.grid(row=3, column=1)
    new_password_entry.grid(row=3, column=2, padx=10, pady=5)
    reenter_new_password_label.grid(row=4, column=1)
    reenter_new_password_entry.grid(row=4, column=2, padx=10, pady=5)
    new_sign_up_button.grid(row=5, column=0, columnspan=3, padx=25, pady=5)

    # New Sign Up Button --> check_new_credentials function
    new_sign_up_button.bind('<ButtonRelease-1>', lambda event: check_new_credentials(new_email_entry.get(),
                                                                                     new_username_entry.get(),
                                                                                     new_password_entry.get(),
                                                                                     reenter_new_password_entry.get(),
                                                                                     register_window))


def check_new_credentials(new_email, new_username, new_password, reenter_new_password, register_window):
    new_email.lower()
    new_username.lower()

    regex_email = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '~', '~',
                     "'", '"', ':', ';', '{', '[', '}', ']', '|', '\\', '<', ',', '>', '.', '?', '/']
    password_error_msg = """Invalid password.
                                \nPasswords must contain between 6 and 20 characters
and must use at least three of the four available character
types: lowercase letters, uppercase letters, numbers, and symbols."""

    # Password conditions
    if not any(char.isdigit() for char in new_password) or not any(char.isupper() for char in new_password) or not any(
            char.islower() for char in new_password) or not any(char in special_chars for char in new_password):
        tk.messagebox.showerror(title="Error", message=password_error_msg)
    else:
        if (re.search(regex_email, new_email)) and 3 <= len(new_username) <= 20 and 6 <= len(new_password) <= 20:
            if new_password != reenter_new_password:
                tk.messagebox.showerror(title="Error", message=""""Passwords do not match.
Please try again.""")
            else:
                with open('user_logs.txt', 'r') as user_logs:
                    user_info = json.load(user_logs)
                    for user in user_info:
                        # Username is taken
                        if user["username"] == new_username:
                            tk.messagebox.showerror(title="Error", message="Username is already taken.")
                        # Email is taken
                        elif user["email"] == new_email:
                            tk.messagebox.showerror(title="Error", message="That email is already in use.")
                        # Write new file
                        else:
                            with open('user_logs.txt', 'w') as updated_user_logs:
                                new_user = {"email": new_email, "username": new_username, "password": new_password}
                                updated_user_info = user_info.copy()
                                updated_user_info.append(new_user)
                                json.dump(updated_user_info, updated_user_logs)
                                tk.messagebox.showinfo(title="Success", message="Signed up successfully!")
                                updated_user_logs.close()
                                register_window.destroy()
                                break
        elif not (re.search(regex_email, new_email)):
            tk.messagebox.showerror(title="Error", message="Invalid email address.")
        elif not 3 <= len(new_username) <= 20:
            tk.messagebox.showerror(title="Error", message="""Invalid username.
                                    \nUsernames must contain between 3 and 20 characters.""")
        else:
            tk.messagebox.showerror(title="Error", message=password_error_msg)


login_window()
