'''
import tkinter as tk
from first_page import FirstPage
from login import LoginPage

class MyApp:
    def __init__(self, root):
        self.root = root
        self.show_login()

    def show_login(self):
        self.login_page = LoginPage(self.root)
        # Add logic to display the login page

    def show_first_page(self):
        self.first_page = FirstPage(self.root)
        # Add logic to display the first page

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
'''