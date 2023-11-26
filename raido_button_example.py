import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Integer Input App")

# Integer variable to store the radio button value
selected_value = tk.IntVar()

def submit():
    # Function to handle the submission of the radio button value and input fields
    print(f"Selected Value: {selected_value.get()}")
    print(f"Input Field 1: {entry1.get()}")
    print(f"Input Field 2: {entry2.get()}")

# Frame to contain radio buttons
radio_frame = tk.Frame(root)
radio_frame.pack()

# Radio buttons
tk.Radiobutton(radio_frame, text="0", variable=selected_value, value=0).pack(side=tk.LEFT)
tk.Radiobutton(radio_frame, text="1", variable=selected_value, value=1).pack(side=tk.LEFT)
tk.Radiobutton(radio_frame, text="2", variable=selected_value, value=2).pack(side=tk.LEFT)

# Input fields
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Run the application
root.mainloop()
