import tkinter as tk
from tkinter import messagebox
from second import SecondPage  # Import the SecondPage class from second.py

class LoginPage1:
    def __init__(self, root):
        '''
        self.root = root
        self.root.title("Login Page")

        self.label = tk.Label(root, text="Username:")
        self.label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.label = tk.Label(root, text="Password:")
        self.label.pack()

        self.password_entry = tk.Entry(root, show="*")  # Use show="*" to hide the password
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()
        '''
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("700x350")
        
        # Create username and password entry fields
        self.email_label = tk.Label(root, text="email address")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()
        
        self.password_label = tk.Label(root, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")  # Show asterisks for password entry
        self.password_entry.pack()
        
        
        self.firstname_label = tk.Label(root, text="first name")
        self.firstname_label.pack()
        self.firstname_entry = tk.Entry(root)  # Show asterisks for password entry
        self.firstname_entry.pack()
        
        
        self.lastname_label = tk.Label(root, text="last name")
        self.lastname_label.pack()
        self.lastname_entry = tk.Entry(root)  # Show asterisks for password entry
        self.lastname_entry.pack()
        
        self.dob_label = tk.Label(root, text="dob month/day/year")
        self.dob_label.pack()
        self.dob_entry = tk.Entry(root)  # Show asterisks for password entry
        self.dob_entry.pack()
        
        
        self.sex_label = tk.Label(root, text="female:0, mail:1")
        self.sex_label.pack()
        self.sex_entry = tk.Entry(root)  # Show asterisks for password entry
        self.sex_entry.pack()
        
        
        # Create a login button
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()
        
        # Create a registration button
        self.register_button = tk.Button(root, text="Register", command=self.login)
        self.register_button.pack()
        
        # Create a label to display login status
        self.login_status = tk.Label(root, text="")
        self.login_status.pack()
        
        # Create a label to display registration status
        self.registration_status = tk.Label(root, text="")
        self.registration_status.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Add your login validation logic here
        if username == "your_username" and password == "your_password":
            self.open_second_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_second_page(self):
        self.root.destroy()  # Close the login page
        root = tk.Tk()  # Create a new root for the second page
        second_page = SecondPage(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage1(root)
    root.mainloop()