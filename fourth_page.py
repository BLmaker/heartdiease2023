import tkinter as tk
import query
import pandas as pd
def fourth_page(root):
    # Create a new frame for the second page
    second_page_frame = tk.Frame(root)
    second_page_frame.pack(pady=10)

    # Create a label to display the message
    #text2='According to our estimation, you may not have a heart disease'
    #print(query.sex1)
    if query.sex1==0:
        sex_1='female'
        person_1='she'
    else:
        sex_1='male'
        person_1='he'
    
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
    print(problems)
    

    #future_str=''.join(map(str,query.future_row))
    future_str=query.future_row
    today1=pd.to_datetime('today').strftime("%Y-%m-%d")
    text2='Name:'+query.name1+ '\n' \
          'Age:' + str(query.age1) + '\n'\
          'Sex:'+sex_1+ '\n'+ \
           today1 + '\n'+\
    'According to our estimation,\n' + \
    person_1 +'  may not have a heart disease. \n' + \
    'the forecasted features after 1 year are \n'+ \
    future_str +'\n'
    if len(problems)==0:
         text2=text2+'Nothing'
    else:
        text2=text2+'Potential worsened feature(s):' + '\n'
        for k in problems:
            text2=text2+k+'\n'
    
    message_label = tk.Label(second_page_frame, text=text2, font=("Times New Roman ", 12))
    message_label.pack(padx=20, pady=20)
