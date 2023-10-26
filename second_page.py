import tkinter as tk
import pandas as pd
#from query import name1, age1
def second_page(root):
    # Create a new frame for the second page
    #print(name1)
    
    second_page_frame = tk.Frame(root)
    second_page_frame.pack(pady=10)
    
    ### subtracted
    problems = []
    if query.subtract[3]<0:
        problems.append('resting blood pressure')
    if query.subtract[4]<0:
        problems.append('serum blood cholestrol')
    if query.subtract[7]<0:
        problems.append('maximum heart rate')
    if query.subtract[9]<0:
        problems.append('ST-depression depth')
        
    ####
    
    
    
    if query.sex1==0:
        sex_1='female'
        person_1='she'
    else:
        sex_1='male'
        person_1='he'
    #future_str=''.join(map(str,query.future_row))
    future_str=query.future_row

    # Create a label to display the message
    today1=pd.to_datetime('today').strftime("%Y-%m-%d")
    text1='Name:'+query.name1+ '\n' \
          'Age:' + str(query.age1) + '\n'\
          'Sex:'+sex_1+ '\n'+ \
           today1 + '\n'+\
    'According to our estimation,\n' + \
         person_1  + '  has a heart diesease currently. \n'+ \
         'The forecasted features after 1 year are \n'+ \
         future_str +  ' \n' 
         
    if len(problems)==0:
        print('Nothing')
    else:
        print('Potential worsened feature(s) after 1 year:' + '\n')
        for k in problems:
            print(k+'\n')
             
    
    message_label = tk.Label(second_page_frame, text=text1, font=("Helvetica", 12))
    message_label.pack(padx=20, pady=20)
