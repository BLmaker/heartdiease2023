import tkinter as tk
import sqlite3

# Create the SQLite database and user table if they don't exist
conn = sqlite3.connect("user_db.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
conn.commit()
conn.close()

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    
    # Check if the entered username and password match a record in the database
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        login_status.config(text="Login Successful")
    else:
        login_status.config(text="Login Failed")

def register():
    username = username_entry.get()
    password = password_entry.get()
    
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    
    # Check if the username already exists
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        registration_status.config(text="Username already exists")
    else:
        # If the username doesn't exist, insert a new user record
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        registration_status.config(text="Registration Successful")
    
    conn.close()

# Create the tkinter window
window = tk.Tk()
window.title("Login Application")

# Create username and password entry fields
username_label = tk.Label(window, text="Username")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password")
password_label.pack()
password_entry = tk.Entry(window, show="*")  # Show asterisks for password entry
password_entry.pack()

# Create a login button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack()

# Create a registration button
register_button = tk.Button(window, text="Register", command=register)
register_button.pack()

# Create a label to display login status
login_status = tk.Label(window, text="")
login_status.pack()

# Create a label to display registration status
registration_status = tk.Label(window, text="")
registration_status.pack()

window.mainloop()
