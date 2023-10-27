import tkinter as tk

class SecondPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Second Page")

        # Add the content of your second page here

if __name__ == "__main__":
    root = tk.Tk()
    second_page = SecondPage(root)
    root.mainloop()