import tkinter as tk
from tkinter import messagebox
import csv

def login():
    email = email_entry.get()
    password = password_entry.get()

    with open('document.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == email and row[1] == password:
                open_second_interface()
                return
    messagebox.showerror("Error", "Invalid email or password")

def open_second_interface():
    root.destroy()  # Close the login window
    second_window = tk.Tk()
    second_window.title("Second Interface")
    second_window.geometry("400x200")

    # Add your interface elements here for the second interface

    second_window.mainloop()

root = tk.Tk()
root.title("Login Page")

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()

# email1@example.com,password1
# email2@example.com,password2
