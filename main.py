import tkinter as tk
from tkinter import messagebox

# Mock authentication function
def authenticate(username, password):
    # Check username and password against a database or API
    # Return True if authentication is successful, False otherwise
    if username == 'admin' and password == 'password':
        return True
    else:
        return False

# Function to handle login button click
def handle_login():
    username = entry_username.get()
    password = entry_password.get()

    if authenticate(username, password):
        messagebox.showinfo('Login', 'Login successful!')
        # Destroy the login window and open the main window
        login_window.destroy()
        open_main_window()
    else:
        messagebox.showerror('Login', 'Invalid username or password.')

# Function to open the main window
def open_main_window():
    main_window = tk.Tk()
    main_window.title('Main Window')
    # Add your main window widgets and functionality here
    main_window.mainloop()

# Create the login window
login_window = tk.Tk()
login_window.title('Login')

# Create username label and entry
label_username = tk.Label(login_window, text='Username')
label_username.pack()
entry_username = tk.Entry(login_window)
entry_username.pack()

# Create password label and entry
label_password = tk.Label(login_window, text='Password')
label_password.pack()
entry_password = tk.Entry(login_window, show='*')
entry_password.pack()

# Create login button
button_login = tk.Button(login_window, text='Login', command=handle_login)
button_login.pack()

# Start the login window
login_window.mainloop()

