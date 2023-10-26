import tkinter as tk
import sqlite3
from tkinter import font as tkfont



def submit():
    # Get values from the lifestyle section
    carb_intake = carb_entry.get()
    cholesterol = cholesterol_entry.get()
    
    # Get values from the sensor data section
    hr = hr_entry.get()
    ecg = ecg_entry.get()
    
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    
    # Create a table to store the data if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY,
            carb_intake REAL,
            cholesterol REAL,
            hr INTEGER,
            ecg INTEGER
        )
    ''')
    
    # Insert the input data into the database
    cursor.execute("INSERT INTO user_data (carb_intake, cholesterol, hr, ecg) VALUES (?, ?, ?, ?)",
                   (carb_intake, cholesterol, hr, ecg))
    
    # Commit the changes and close the database connection
    conn.commit()
    conn.close()
    
    # For demonstration purposes, let's display a success message
    result_label.config(text="Data saved to the database")


root = tk.Tk()
root.title("User Interface")

bold_font = tkfont.Font(weight="bold")

# Create frames for the two sections
lifestyle_frame = tk.Frame(root)
lifestyle_frame.pack(pady=10)

sensor_frame = tk.Frame(root)
sensor_frame.pack(pady=10)

# Lifestyle Section
lifestyle_label = tk.Label(lifestyle_frame, text="Lifestyle", font = bold_font)
lifestyle_label.pack()

carb_label = tk.Label(lifestyle_frame, text="Carbohydrate Intake:")
carb_entry = tk.Entry(lifestyle_frame)

cholesterol_label = tk.Label(lifestyle_frame, text="Cholesterol:")
cholesterol_entry = tk.Entry(lifestyle_frame)

carb_label.pack()
carb_entry.pack()
cholesterol_label.pack()
cholesterol_entry.pack()

# Sensor Reading Data Section
sensor_label = tk.Label(sensor_frame, text="Sensor Reading Data", font = bold_font)
sensor_label.pack()

hr_label = tk.Label(sensor_frame, text="Heart Rate (HR):")
hr_entry = tk.Entry(sensor_frame)

ecg_label = tk.Label(sensor_frame, text="ECG Reading:")
ecg_entry = tk.Entry(sensor_frame)

hr_label.pack()
hr_entry.pack()
ecg_label.pack()
ecg_entry.pack()

# Create a single "Submit" button that calls the submit() function
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
