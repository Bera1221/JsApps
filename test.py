import tkinter as tk
from tkinter import messagebox

# Function to validate login credentials
def login():
    username = entry_username.get()
    password = entry_password.get()

    # For simplicity, we'll just check if both fields are filled and assume 'admin' as correct credentials
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Creating main window
root = tk.Tk()
root.title("Login Interface")

# Set window size
root.geometry("300x200")

# Username Label and Entry
label_username = tk.Label(root, text="Username")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password Label and Entry
label_password = tk.Label(root, text="Password")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Run the application
root.mainloop()