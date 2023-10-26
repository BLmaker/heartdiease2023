import tkinter as tk
import sqlite3
import pandas as pd
from tkinter import PhotoImage
from tkinter import font as tkfont
from PIL import Image, ImageTk
from database import initialize_database, insert_data_into_tables
from second_page import second_page  # Import the second page module
from third_page import  third_page  # Import the third page module
from fourth_page import fourth_page  # Import the fourth page module
#from datetime import datetime

from query import export_last_row_to_csv
from NN11_test import predict_and_save_to_csv





# Initialize the database (call this at the start of your application)
initialize_database()

def switch_to_second_page():
    # Hide the first page
    first_page.pack_forget()
    
    # Create and display the second page
    second_page.pack()

def switch_to_thrid_page():
    # Hide the first page
    first_page.pack_forget()
    
    # Create and display the second page
    third_page.pack()

def switch_to_fourth_page():
    # Hide the first page
    first_page.pack_forget()
    
    # Create and display the second page
    fourth_page.pack()


def submit():
    # Get user input values from the Tkinter entry fields
    lifestyle_data = [0,0,0,0,0,0,0,0,0,0]
      
    '''
        smoke_entry.get(),
        drink_entry.get(),
        sodium_entry.get(),
        fat_entry.get(),
        act_entry.get(),
        mass_entry.get(),
        height_entry.get(),
        stress_entry.get(),
        slp_entry.get(),
        wtr_entry.get(),
        '''

    
    
    user_input_data = [
    #   age_entry.get(),
     #  sex_entry.get(),
        0,
        0,
        cp_entry.get(),
        rbp_entry.get(),
        chl_entry.get(),
        fbs_entry.get(),
        restecg_entry.get(),
        thalach_entry.get(),
        exang_entry.get(),
        oldpeak_entry.get(),
        slope_entry.get(),
    ]
    #A=cp_entry.get()
    #C.set(A)

    # Insert user input data into the database
    id_1=1
    user_input_data[0]=id_1
    #user_input_data[1]=datetime.now().strftime('%m/%d/%Y')
    #print(user_input_data)
    insert_data_into_tables(user_input_data)
    # jung hoon
    

    
    # Clear the Tkinter entry fields after submitting
    '''
    for entry in (smoke_entry, drink_entry, sodium_entry, fat_entry, act_entry, mass_entry, height_entry,
                  #stress_entry, slp_entry, wtr_entry, age_entry, sex_entry, cp_entry, rbp_entry, chl_entry,
                  stress_entry, slp_entry, wtr_entry, cp_entry, rbp_entry, chl_entry,
                  fbs_entry, restecg_entry, thalach_entry, exang_entry, oldpeak_entry, slope_entry):
    
    
        entry.delete(0, tk.END)
'''
    export_last_row_to_csv()
    predict_and_save_to_csv()

    current_state = pd.read_csv("current_state.csv")
    future_state = pd.read_csv("future_state.csv")
    row_index = 0  # Replace with the row index you want
    column_name = 'Binary_Predictions'  # Replace with the column name you want

    cell_value = current_state.at[row_index, column_name]   
    future_value = future_state.at[row_index, column_name]   
    
    
    #c.set(user_input_data)
    
    
    
    if cell_value == 1:
      second_page(root)
    if cell_value == 0:
        if future_value == 0:
            fourth_page(root)
        else:
            third_page(root)
    return(user_input_data)
    



root = tk.Tk()
root.title("Heart Disease Application")


#### global variable  maker   #####




#### global variable maker 2 #####

# Load the background image
#background_image = Image.open("g.jpg")  # Replace with the path to your image
#background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
#background_label = tk.Label(root, image=background_photo)
#background_label.place(relwidth=1, relheight=1)
#background_label.pack()

# Create a frame for your UI components (other widgets)
#ui_frame = tk.Frame(root, bg="white")  # You can set the background color for the UI components
#ui_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Add your UI components (labels, entry fields, buttons, etc.) to ui_frame
bold_font = tkfont.Font(weight="bold")

# Create frames for the two sections
first_page = tk.Frame(root)
first_page.pack(pady=10)

# Create two frames for the "Lifestyle" and "User Input Data" columns
lifestyle_frame = tk.Frame(first_page)
lifestyle_frame.grid(row=0, column=0, padx=10)  # Place in the first column with padding

User_frame = tk.Frame(first_page)
User_frame.grid(row=0, column=1, padx=10)  # Place in the second column with padding


# Lifestyle Section
'''
lifestyle_label = tk.Label(lifestyle_frame, text="Lifestyle", font = bold_font)
lifestyle_label.grid(row=0, column=0, columnspan=2)

smoke_label = tk.Label(lifestyle_frame, text="Smoking number of cigarrettes per day:")
smoke_label.grid(row=1, column=0)
smoke_entry = tk.Entry(lifestyle_frame)
smoke_entry.grid(row=1, column=1)

drink_label = tk.Label(lifestyle_frame, text="Alcohol consumption per week:")
drink_label.grid(row=2, column=0)
drink_entry = tk.Entry(lifestyle_frame)
drink_entry.grid(row=2, column=1)

sodium_label = tk.Label(lifestyle_frame, text="How much salt intake do you have per day:")
sodium_label.grid(row=3, column=0)
sodium_entry = tk.Entry(lifestyle_frame)
sodium_entry.grid(row=3, column=1)

fat_label = tk.Label(lifestyle_frame, text="Amount of saturated and trans fat intake per week:")
fat_label.grid(row=4, column=0)
fat_entry = tk.Entry(lifestyle_frame)
fat_entry.grid(row=4, column=1)

act_label = tk.Label(lifestyle_frame, text="How much do you exercise per day:")
act_label.grid(row=5, column=0)
act_entry = tk.Entry(lifestyle_frame)
act_entry.grid(row=5, column=1)

mass_label = tk.Label(lifestyle_frame, text="What is your weight:")
mass_label.grid(row=6, column=0)
mass_entry = tk.Entry(lifestyle_frame)
mass_entry.grid(row=6, column=1)

height_label = tk.Label(lifestyle_frame, text="what is your height:")
height_label.grid(row=7, column=0)
height_entry = tk.Entry(lifestyle_frame)
height_entry.grid(row=7, column=1)

stress_label = tk.Label(lifestyle_frame, text="How many times a day do you feel stressed:")
stress_label.grid(row=8, column=0)
stress_entry = tk.Entry(lifestyle_frame)
stress_entry.grid(row=8, column=1)

slp_label = tk.Label(lifestyle_frame, text="Average Sleep hours in 24hrs:")
slp_label.grid(row=9, column=0)
slp_entry = tk.Entry(lifestyle_frame)
slp_entry.grid(row=9, column=1)

wtr_label = tk.Label(lifestyle_frame, text="Your water consumption daily (litres):")
wtr_label.grid(row=10, column=0)
wtr_entry = tk.Entry(lifestyle_frame)
wtr_entry.grid(row=10, column=1)

# Sensor Reading Data Section
sensor_label = tk.Label(User_frame, text="User Input", font = bold_font)
sensor_label.grid(row=0, column=2, columnspan=2, sticky='n')

'''
# loading file

'''

age_label = tk.Label(User_frame, text="Age:")
age_label.grid(row=1, column=2)
age_entry = tk.Entry(User_frame)
age_entry.grid(row=1, column=3)


sex_label = tk.Label(User_frame, text="Sex:")
sex_label.grid(row=2, column=2)
sex_entry = tk.Entry(User_frame)
sex_entry.grid(row=2, column=3)
'''



cp_label = tk.Label(User_frame, text="[1]Chest Pain type:(1-4)")
cp_label.grid(row=3, column=2)
cp_entry = tk.Entry(User_frame)
cp_entry.grid(row=3, column=3)

#cp1=float(cp_entry)

rbp_label = tk.Label(User_frame, text="[2] Resting Blood Pressure (mm Hg):")
rbp_label.grid(row=4, column=2)
rbp_entry = tk.Entry(User_frame)
rbp_entry.grid(row=4, column=3)

#rbp1=float(rbp_entry)

chl_label = tk.Label(User_frame, text="[3] Cholestoral in mg/dl:")
chl_label.grid(row=5, column=2)
chl_entry = tk.Entry(User_frame)
chl_entry.grid(row=5, column=3)

#chl1=float(chl_entry)

fbs_label = tk.Label(User_frame, text="[4] If fasting Blood Sugar: > 120mg/L , then 1, otherwise 0")
fbs_label.grid(row=6, column=2)
fbs_entry = tk.Entry(User_frame)
fbs_entry.grid(row=6, column=3)

#fbs1=float(fbs_entry)

restecg_label = tk.Label(User_frame, text="[5] Resting Electrocardiographic Results:(0,1,2)")
restecg_label.grid(row=7, column=2)
restecg_entry = tk.Entry(User_frame)
restecg_entry.grid(row=7, column=3)

#restecg1=float(restecg_entry)

thalach_label = tk.Label(User_frame, text="[6] Maximum Heart Rate Achieved:")
thalach_label.grid(row=8, column=2)
thalach_entry = tk.Entry(User_frame)
thalach_entry.grid(row=8, column=3)


#thalach1=float(thalach_entry)

exang_label = tk.Label(User_frame, text="[7] Exercise Induced Angina (1 = Yes, 0 = No):")
exang_label.grid(row=9, column=2)
exang_entry = tk.Entry(User_frame)
exang_entry.grid(row=9, column=3)


#exang1=float(exang_entry)

oldpeak_label = tk.Label(User_frame, text="[8] ST Depression Induced by Exercise Relative to Rest:")
oldpeak_label.grid(row=10, column=2)
oldpeak_entry = tk.Entry(User_frame)
oldpeak_entry.grid(row=10, column=3)

#oldpeak1=float(oldpeak_entry)


slope_label = tk.Label(User_frame, text="[9] Slope of the Peak Exercise ST Segment:")
slope_label.grid(row=11, column=2)
slope_entry = tk.Entry(User_frame)
slope_entry.grid(row=11, column=3)




#slope1=float(slope_entry)

#print(cp_entry)


#print(input_data)
#name, dob, next_year, future_output=forecasting(dbname,input_data)



# Create a single "Submit" button that calls the submit() function
submit_button = tk.Button(first_page, text="Submit", command=submit)
submit_button.grid(row=1, column=0, columnspan=2)  # Place in the main frame


# Create a label to display the result
result_label = tk.Label(first_page, text="")
result_label.grid(row=2, column=0, columnspan=2)  # Place in the main frame


root.mainloop()




