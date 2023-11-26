import tkinter as tk
import sqlite3
from first_page import FirstPage


class LoginPage:


    # Create the SQLite database and user table if they don't exist
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()
    
    def __init__(self, root):
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
        self.register_button = tk.Button(root, text="Register", command=self.register)
        self.register_button.pack()
        
        # Create a label to display login status
        self.login_status = tk.Label(root, text="")
        self.login_status.pack()
        
        # Create a label to display registration status
        self.registration_status = tk.Label(root, text="")
        self.registration_status.pack()

       

    
    
    
    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        conn = sqlite3.connect("health_data.db")
        cursor = conn.cursor()
        
        # Check if the entered username and password match a record in the database
        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()
        print(user)
        
        
        if user:
            self.login_status.config(text="Login Successful")
            try:
                query="select id from users where email=?"
                cursor.execute(query,(email,))
                result=cursor.fetchone()
                print(result)
                self.id_num=int(result[0])
                self.open_first_page()
            finally:
                conn.close()
        else:
            self.login_status.config(text="Login Failed")
            conn.close()
    
    def register(self):
        try:
            conn = sqlite3.connect("health_data.db")
            cursor = conn.cursor()
            query="SELECT max(id) FROM users"
            cursor.execute(query)
            max_id=cursor.fetchone()
            max_id=max_id+1
        
        
            email = self.email_entry.get()
            password = self.password_entry.get()
            
            firstname=self.firstname_entry.get()
            lastname=self.lastname_entry.get()
            sex=self.sex_entry.get()
            dob=self.dob_entry.get()
            
           
            #conn = sqlite3.connect("health_data.db")
            #cursor = conn.cursor()
            
            # Check if the username already exists
            cursor.execute("SELECT * FROM users WHERE email=?", (email,))
            existing_user = cursor.fetchone()
            
            if existing_user:
                self.registration_status.config(text="email already exists")
            else:
                # If the username doesn't exist, insert a new user record
                cursor.execute("INSERT INTO users (id, email, password, first_name, last_name, sex, dob) VALUES (?, ?)",\
                               (max_id, email, password,firstname, lastname, sex, dob))
                conn.commit()
                self.registration_status.config(text="Registration Successful")
        finally:    
            conn.close()
            
    
    def open_first_page(self):
        self.root.destroy()  # Close the login page
        root = tk.Tk()  # Create a new root for the second page
        first_page = FirstPage(root, self.id_num)
        root.mainloop()

            
            

if __name__ == "__main__":
    # Create the tkinter window
    root = tk.Tk()
    login_page=LoginPage(root)
    root.mainloop()
