import tkinter as tk
from tkinter import messagebox
import customtkinter
import json

customtkinter.set_appearance_mode("Light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("600x540")
app.title('Welcome')

def register_button(username, password):
    # Check if username already exists
    if username in users:
        messagebox.showerror("Error", "Username already exists!")
    else:
        # Add new user to the dictionary
        users[username] = password
        messagebox.showinfo("Success", "Registration successful!")

def login_button(username, password):
    if username in users and users[username] == password:
        app.destroy()  # destroy current window and creating new one
        w = customtkinter.CTk()
        w.geometry("1280x720")
        w.title('Task Organizer')
        l1 = customtkinter.CTkLabel(master=w, text=f"Hello {username}! Welcome to your Task Organizer", font=('Century Gothic', 40))
        l1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        w.mainloop()
    else:
        messagebox.showerror("Error", "Invalid username or password!")
    
# Load existing users from JSON file
try:
    with open("users.json", "r") as file:
        users = json.load(file)
except FileNotFoundError:
    users = {}

# Welcome frame
frame = customtkinter.CTkFrame(master=app, width=320, height=430)
frame.place(relx=50, rely=50, anchor=tk.CENTER)
frame.pack()

welcome = customtkinter.CTkLabel(master=frame, text="Welcome to Task Organizer", font=('Century Gothic', 20, 'bold'))
welcome.place(x=30, y=50)
# REGISTER
register = customtkinter.CTkLabel(master=frame, text="Register", font=('Century Gothic', 15))
register.place(x=50, y=80)

register_user = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
register_user.place(x=50, y=120)

register_pwd = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
register_pwd.place(x=50, y=160)

register_button_widget = customtkinter.CTkButton(master=frame, text="Register", command=lambda: register_button(register_user.get(), register_pwd.get()))
register_button_widget.place(x=90, y=200)

# LOGIN
login = customtkinter.CTkLabel(master=frame, text="Login", font=('Century Gothic', 15))
login.place(x=50, y=250)

login_user = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
login_user.place(x=50, y=290)

login_pwd = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
login_pwd.place(x=50, y=330)

login_button_widget = customtkinter.CTkButton(master=frame, text="Login", command=lambda: login_button(login_user.get(), login_pwd.get()))
login_button_widget.place(x=90, y=370)

app.mainloop()

# Save users to JSON file
with open("users.json", "w") as file:
    json.dump(users, file)