import tkinter as tk
import sqlite3
import pandas as pd
from tkinter import PhotoImage
from tkinter import font as tkfont
from PIL import Image, ImageTk
#from database import initialize_database, insert_data_into_tables
#from second_page import second_page  # Import the second page module
#from third_page import  third_page  # Import the third page module
#from fourth_page import fourth_page  # Import the fourth page module
from datetime import datetime
import sql_functions as sq
import functions as fn
import NN11_test as nn
import svm as svm





# Initialize the database (call this at the start of your application)
#initialize_database()

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
    #cp1=cp_entry.get()
    
    for i in [0,1,2,3,4,5,6,7,8,10]:
        user_input_data[i]=int(user_input_data[i])
    user_input_data[9]=float(user_input_data[9])
    
    # Insert user input data into the database
    id_1=1
    
    #personal_info=sq.user_id_fetch(id_1)
   
    
   # producing current data and future data
    
    name,age,gender,next_year,future_output=fn.forecasting(id_1, user_input_data[2:])
    user_input_data[0]=age
    user_input_data[1]=gender

    
    
    c_judge=[0]*7
    f_judge=[0]*7
    print(user_input_data)
    print(future_output)
    c_judge[0]=svm.svm_fn(user_input_data)
    #print('svm')
    c_judge[1]=svm.nb_fn(user_input_data)
    #print('nb')
    c_judge[2]=svm.dt_fn(user_input_data)
    #print('dt')
    c_judge[3]=svm.rf_fn(user_input_data)
    #print('rf')
    c_judge[4]=svm.lr_fn(user_input_data)
    #print('lr')
    c_judge[5]=svm.knn_fn(user_input_data)
    #print('knn')
    
    f_judge[0]=svm.svm_fn(future_output)
    f_judge[1]=svm.nb_fn(future_output)
    f_judge[2]=svm.dt_fn(future_output)
    f_judge[3]=svm.rf_fn(future_output)
    f_judge[4]=svm.lr_fn(future_output)
    f_judge[5]=svm.knn_fn(future_output)
    
      
    # neural network 
    nn1=nn.diagnose(user_input_data)
    nn2=nn.diagnose(future_output)
    
    c_judge[6]=nn1.tolist()[0][0]
    f_judge[6]=nn2.tolist()[0][0]
    
    current1=any(c_judge) 
    future1=any(f_judge) 
    
    #print(current1)
    #print(future1)
    testtime=datetime.now().strftime('%m/%d/%Y')
    uid=user_input_data.copy()
    sq.test_input(id_1,testtime,uid[2], uid[3], uid[4], uid[5], uid[6], uid[7],\
                  uid[8], uid[9],uid[10], int(current1))

    
    if gender==0:
        sex_1='female'
        person_1='she'
    else:
        sex_1='male'
        person_1='he'    

# problem pointing
    subtract=[]
    for i,j in zip(user_input_data, future_output):
        subtract.append(i-j)        
    problems = []
    if subtract[3]<0:
        problems.append('resting blood pressure')
    if subtract[4]<0:
        problems.append('serum blood cholestrol')
    if subtract[7]<0:
        problems.append('maximum heart rate')
    if subtract[9]<0:
        problems.append('ST-depression depth')
    
    future_str='Potential worsened feature(s):' + '\n'
    
    if len(problems)==0:
         future_str=future_str+'Nothing'
    else:
        for k in problems:
            future_str=future_str+k+'\n'
    
 # text making    
        
    if current1 == 1: # he has heart dieases
      text1='Name:'+name+ '\n' \
            'Age:' + str(age) + '\n'\
            'Sex:'+sex_1+ '\n'+ \
             testtime + '\n'+\
      'According to our estimation,\n' + \
           person_1  + '  has a heart diesease currently. \n'+ \
           ' \n'+ \
           future_str +  ' \n' 

    if current1 == 0: # he has no heart dieases
        if future1 == 0:
            text1='Name:'+name+ '\n' \
                  'Age:' + str(age) + '\n'\
                  'Sex:'+sex_1+ '\n'+ \
                   testtime + '\n'+\
            'According to our estimation,\n' + \
            person_1 +'  may not have a heart disease. \n' +\
            'It is not likely that you have the onset of heart disease 1 year later \n'+ \
            future_str +  ' \n' 
            
                
        else: # now okay, but later expected ill
            text1='Name:'+name+ '\n' \
                  'Age:' + str(age) + '\n'\
                  'Sex:'+sex_1+ '\n'+ \
                   testtime + '\n'+\
            'According to our estimation,\n' + \
            person_1 +'  may not have a heart disease. cuurently\n ' + \
            'But, it is probable that he may have the onset of heart diease next year.\n'+ \
            '\n'+ \
            future_str  + ' \n' 
    message_label = tk.Label(text=text1, font=("Helvetica", 12))
    message_label.pack(padx=20, pady=20)
    



root = tk.Tk()
root.title("Heart Disease Application")
####

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

#user_input_data=[cp0, trestbps0, chol0, fbs0, restecg0, thalach0, exang0, oldpeak0, slope0]

# Create a label to display the result
result_label = tk.Label(first_page, text="")
result_label.grid(row=2, column=0, columnspan=2)  # Place in the main frame


root.mainloop()




