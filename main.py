import pandas as pd
import matplotlib.pyplot as matplot
import numpy as py
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv


def clean_window():
    for widget in root.winfo_children():
        widget.destroy()


def save_user(name, password):
    # Open the CSV file in append mode to add the data
    with open("users/users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        # Write the name and password into the CSV file
        writer.writerow([name, password])


def load_user(name, password):
    with open("users/users.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name and row[1] == password:
                return True
    return False


def save_submit(name_entry, password_entry):
    name = name_entry.get()
    password = password_entry.get()

    if name and password:
        save_user(name, password)
        messagebox.showinfo("Details Saved!", "Your details have been saved successfully!")
        handle_signin_form()
    else:
        messagebox.showwarning("Invalid input!", "Please enter both name and password")


def submit_user_load(name_entry, password_entry):
    name = name_entry.get()
    password = password_entry.get()

    if load_user(name, password):
        messagebox.showinfo("Login Successful", "Welcome back!")
        # Proceed to the next window after successful login
        handle_dashboard()
    else:
        messagebox.showwarning("Invalid Login", "Incorrect username or password!")


def handle_dashboard():
    # Handle the dashboard or main screen after successful login
    dashboard = tk.Toplevel(root)
    dashboard.geometry("400x300")
    dashboard.title("Dashboard")

    label = tk.Label(dashboard, text="Welcome to the Dashboard!")
    label.pack(pady=50)

    # Add more widgets for the dashboard if needed
    dashboard.mainloop()


def handle_signup_form():
    # Clean the window before creating text boxes
    clean_window()

    # Create a frame in the middle
    frame = tk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Create and place the labels and entry fields for signup
    tk.Label(frame, text="Enter your sign up info").pack(pady=10)
    tk.Label(frame, text="Name:").pack(pady=10)
    name_entry = tk.Entry(frame)
    name_entry.pack(pady=5)

    tk.Label(frame, text="Password:").pack(pady=10)
    password_entry = tk.Entry(frame, show="*")  # Hide the password text
    password_entry.pack(pady=5)

    submit_button = tk.Button(frame, text="Submit", command=lambda: save_submit(name_entry, password_entry))
    submit_button.pack(pady=20)

    signin_button = tk.Button(frame, text="Already have an account?", command=lambda: handle_signin_form())
    signin_button.pack(pady=20)


def handle_signin_form():
    # Clean the window before showing signin form
    clean_window()

    # Create a frame in the middle
    frame = tk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Create and place the labels and entry fields for signin
    tk.Label(frame, text="Enter your sign in info").pack(pady=10)
    tk.Label(frame, text="Name:").pack(pady=10)
    name_entry = tk.Entry(frame)
    name_entry.pack(pady=5)

    tk.Label(frame, text="Password:").pack(pady=10)
    password_entry = tk.Entry(frame, show="*")  # Hide the password text
    password_entry.pack(pady=5)

    submit_button = tk.Button(frame, text="Submit", command=lambda: submit_user_load(name_entry, password_entry))
    submit_button.pack(pady=20)

    signup_button = tk.Button(frame, text="Create new account", command=lambda: handle_signup_form())
    signup_button.pack(pady=20)


def get_window_size():
    x = root.winfo_width()
    y = root.winfo_height()
    return x, y


def load_image(image_name, size):
    image = Image.open(image_name).resize(size)
    return image


def remove_image(label):
    label.config(image="")
    label.image = None


def show_image(image, duration, position):
    tk_image = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=tk_image)
    label.image = tk_image
    label.place(x=position[0], y=position[1])
    root.after(duration, remove_image, label)


root = tk.Tk()
root.title("HEC Learning Management System")
root.geometry("1024x768")

# Load HEC logo
Logo_HEC = load_image("images/HEC_Logo.png", (400, 400))

# Update the root so that the window's size gets updated correctly
root.update()

# Show the image for 4 seconds in the middle of the window
show_image(Logo_HEC, 4000, (get_window_size()[0] / 2 - 200, get_window_size()[1] / 2 - 200))

# After 4 seconds, show the sign-up form
root.after(4000, handle_signup_form)

# Starts the code/opens the window
root.mainloop()
