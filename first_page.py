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



class FirstPage:

    # Initialize the database (call this at the start of your application)
    #initialize_database()
    
    def __init__(self, root,id_num):
        self.id_num=id_num
        root.title("Heart Disease Application")
        conn = sqlite3.connect("health_data.db")
        cursor = conn.cursor()
        
        selected_value=tk.IntVar() ###
        
        query2='select first_name, last_name, dob, sex from users  where id='+str(self.id_num)
        try:
            result=cursor.fetchall()#과거의 병력
            cursor.execute(query2)
            info=cursor.fetchall() #개인정보
        finally: 
            conn.close()

        name=info[0][0]+" "+info[0][1]
        dob=info[0][2]
        sex=info[0][3]
        if sex==1:
            gender='Male'
        else:
            gender='Female'
        
        
        bold_font = tkfont.Font(weight="bold")
    
        # Create frames for the two sections
        first_page = tk.Frame(root)
        first_page.pack(pady=10)
    
        

        User_frame = tk.Frame(first_page)
        User_frame.grid(row=0, column=1, padx=10)  # Place in the second column with padding
    
    
    
        # loading file
    
         
        self.name_label=tk.Label(User_frame, text='Name:'+name, justify='center', font=bold_font)
        self.name_label.grid(row=0, column=1)
        self.dob_label=tk.Label(User_frame, text='Date of Birth:'+dob,justify='center', font=bold_font)
        self.dob_label.grid(row=0, column=2)
        self.sex_label=tk.Label(User_frame, text='Gender:'+gender,justify='center', font=bold_font)
        self.sex_label.grid(row=0, column=3)
        
        
        self.sex_label=tk.Label(User_frame, text='Enter Your Features',justify='center', font=bold_font)
        self.sex_label.grid(row=1, column=2)
        
            
        self.cp_label = tk.Label(User_frame, text="[1]Chest Pain type:(1-4)")     
        self.cp_label.grid(row=3, column=1)
        '''
        self.cp_entry = tk.Entry(User_frame)
        self.cp_entry.grid(row=3, column=3)
'''
        self.cp_value = tk.IntVar()
        cp_options = [1, 2, 3, 4]
        juarte=["typical angina", "atypical angina", "non-anginal pain", "asymptomatic" ]
        for index, option in enumerate(cp_options):
            cp_radio = tk.Radiobutton(User_frame, text=juarte[index], variable=self.cp_value, value=option)
            cp_radio.grid(row=3, column= 2 + index)
            #root.grid_columnconfigure(4, minsize=20)


   

        #cp1=float(cp_entry)
    
        self.rbp_label = tk.Label(User_frame, text="[2] Resting Blood Pressure (mm Hg):")
        self.rbp_label.grid(row=4, column=1)
        self.rbp_entry = tk.Entry(User_frame)
        self.rbp_entry.grid(row=4, column=2)
    
        #rbp1=float(rbp_entry)
    
        self.chl_label = tk.Label(User_frame, text="[3] Cholestoral in mg/dl:")
        self.chl_label.grid(row=5, column=1)
        self.chl_entry = tk.Entry(User_frame)
        self.chl_entry.grid(row=5, column=2)
    
        #chl1=float(chl_entry)
        
    
        self.fbs_label = tk.Label(User_frame, text="[4] If fasting Blood Sugar: ")
        self.fbs_label.grid(row=6, column=1)
        '''
        self.fbs_entry = tk.Entry(User_frame)
        self.fbs_entry.grid(row=6, column=3)
        '''
        self.fbs_value = tk.IntVar()
        cp_options = [0, 1]
        juarte=["less than 120mmol/L", "otherwise" ]
        for index, option in enumerate(cp_options):
            fbs_radio = tk.Radiobutton(User_frame, text=juarte[index], variable=self.fbs_value, value=option)
            fbs_radio.grid(row=6, column=2 + index)
       
    

    
        #fbs1=float(fbs_entry)
    
        self.restecg_label = tk.Label(User_frame, text="[5] Resting Electrocardiographic Results:(0,1,2)")
        self.restecg_label.grid(row=7, column=1)
        '''
        self.restecg_entry = tk.Entry(User_frame)
        self.restecg_entry.grid(row=7, column=3)
        '''
        self.restecg_value = tk.IntVar()
        cp_options = [0, 1, 2]
        juarte=["normal", "ST-T abnormality", "exeeding Estes' Criteria"]
        for index, option in enumerate(cp_options):
            restecg_radio = tk.Radiobutton(User_frame, text=juarte[index], variable=self.restecg_value, value=option)
            restecg_radio.grid(row=7, column=2 + index)

        
    
        #restecg1=float(restecg_entry)
    
        self.thalach_label = tk.Label(User_frame, text="[6] Maximum Heart Rate Achieved:")
        self.thalach_label.grid(row=8, column=1)
        self.thalach_entry = tk.Entry(User_frame)
        self.thalach_entry.grid(row=8, column=2)
    
    
        #thalach1=float(thalach_entry)
    
        self.exang_label = tk.Label(User_frame, text="[7] Exercise Induced Angina :")
        self.exang_label.grid(row=9, column=1)
        
        '''
        self.exang_entry = tk.Entry(User_frame)
        self.exang_entry.grid(row=9, column=3)
    '''
        self.exang_value = tk.IntVar()
        cp_options = [0, 1]
        juarte=["No", "Yes"]
        for index, option in enumerate(cp_options):
            exang_radio = tk.Radiobutton(User_frame, text=juarte[index], variable=self.exang_value, value=option)
            exang_radio.grid(row=9, column=2 + index)
    
        #exang1=float(exang_entry)
    
        self.oldpeak_label = tk.Label(User_frame, text="[8] ST Depression Induced by Exercise Relative to Rest:")
        self.oldpeak_label.grid(row=10, column=1)
        self.oldpeak_entry = tk.Entry(User_frame)
        self.oldpeak_entry.grid(row=10, column=2)
    
        #oldpeak1=float(oldpeak_entry)
    
    
        self.slope_label = tk.Label(User_frame, text="[9] Slope of the Peak Exercise ST Segment:")
        self.slope_label.grid(row=11, column=1)
        
        '''
        self.slope_entry = tk.Entry(User_frame)
        self.slope_entry.grid(row=11, column=3)
        '''
        self.slope_value = tk.IntVar()
        cp_options = [1, 2, 3]
        juarte=["upsloping", "flat", "downsloping"]
        for index, option in enumerate(cp_options):
            slope_radio = tk.Radiobutton(User_frame, text=juarte[index], variable=self.slope_value, value=option)
            slope_radio.grid(row=11, column=2 + index)
    
        
      
        

    
    
        #slope1=float(slope_entry)
    
        #print(cp_entry)
    
    
        #print(input_data)
        #name, dob, next_year, future_output=forecasting(dbname,input_data)
    
    
    
        # Create a single "Submit" button that calls the submit() function
        self.submit_button = tk.Button(first_page, text="Submit", command=self.submit)
        self.submit_button.grid(row=1, column=0, columnspan=2)  # Place in the main frame
    
        #user_input_data=[cp0, trestbps0, chol0, fbs0, restecg0, thalach0, exang0, oldpeak0, slope0]
    
        # Create a label to display the result
        self.result_label = tk.Label(first_page, text="")
        self.result_label.grid(row=2, column=0, columnspan=2)  # Place in the main frame
        
    
    
    def submit(self):
        
        user_input_data = [
        #   age_entry.get(),
         #  sex_entry.get(),
            
            self.id_num, # new adding
            0,
            self.cp_value.get(),
            self.rbp_entry.get(),
            self.chl_entry.get(),
            self.fbs_value.get(),        
            self.restecg_value.get(), 
            self.thalach_entry.get(),
            self.exang_value.get(),
            self.oldpeak_entry.get(),
            self.slope_value.get(),
            
        ]
        
        
        #cp1=cp_entry.get()
        
        for i in [0, 1,2,3,4,5,6,7,8,10]: #0
            if isinstance(user_input_data[i], str)==True:
                user_input_data[i]=int(user_input_data[i])
        user_input_data[9]=float(user_input_data[9])
        
        print(user_input_data)
        
        # Insert user input data into the database
        id_1=self.id_num # new adding
        
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
                'today is'+testtime + '\n'+\
          'According to our estimation,\n' + \
               person_1  + '  has a heart diesease currently. \n'+ \
               ' \n'+ \
               future_str +  ' \n' 
    
        if current1 == 0: # he has no heart dieases
            if future1 == 0:
                text1='Name:'+name+ '\n' \
                      'Age:' + str(age) + '\n'\
                      'Sex:'+sex_1+ '\n'+ \
                      'today is' +testtime + '\n'+\
                'According to our estimation,\n' + \
                person_1 +'  may not have a heart disease. \n' +\
                'It is not likely that you have the onset of heart disease 1 year later \n'+ \
                future_str +  ' \n' 
                
                    
            else: # now okay, but later expected ill
                text1='Name:'+name+ '\n' \
                      'Age:' + str(age) + '\n'\
                      'Sex:'+sex_1+ '\n'+ \
                      'today is '+testtime + '\n'+\
                'According to our estimation,\n' + \
                person_1 +'  may not have a heart disease. cuurently\n ' + \
                'But, it is probable that he may have the onset of heart diease next year.\n'+ \
                '\n'+ \
                future_str  + ' \n' 
        message_label = tk.Label(text=text1, font=("Helvetica", 12))
        message_label.pack(padx=20, pady=20)
        self.log_button = tk.Button(first_page, text="logout", command=self.logout)
        self.log_button.grid(row=11, column=0, columnspan=2)  # Place in the main frame

    def logout(self):
        '''
        self.root.destroy()  # Close the current window
        root = tk.Tk()  # Create a new root for the login page
        login_page = MyApp(root)
        root.mainloop()
       '''

if __name__=="__main__":   


    root = tk.Tk()
    first_page=FirstPage(root)    
    root.mainloop()




