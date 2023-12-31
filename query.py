import sqlite3
import csv
from normalization import normalizing
from functions import do_regression, merge_table, forecasting
import pandas as pd
import math
from sklearn.linear_model import LinearRegression
import sql_functions as sl
from datetime import datetime
import first_page as fp

#from first_page import get_entry

'''
def export_last_row_to_csv(
    database_name="health_data.db",
    table_name="user_input",
    csv_file_name="last_row.csv",
    
    
    output_future_file='future_state.csv',
    future_file_name='future_row.csv',
    
    
    column_headers=[
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", 
        "exang", "oldpeak", "slope"
    ]
):
    # Connect to the SQLite database
    # Connect to the SQLite database

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    # Construct the SQL query to retrieve the last row with columns explicitly selected
    query = f"SELECT {', '.join(column_headers)} FROM {table_name} ORDER BY id DESC LIMIT 1"

    
    # Execute the query
    cursor.execute(query)
    
    # Fetch the result (last row)
    last_row = cursor.fetchone()
    
    last_row=fp.input_user_data
    
    id1=1
    #last_row=last_row[2:]
    print(f'last_row{last_row}')
    for i in range(len(last_row)):
        last_row[i]=float(last_row[i])   
    #print(last_row)
    id1=int(id1)
    name1, age1, sex1, year1, fore1=forecasting(id1,last_row)
    
     

    #last_row[0]=age1
    #last_row[1]=sex1
    
    future_row1=fore1
    ###
    
    ###
    
    future_row2='['
    for i in range(len(future_row1)):
        if i<10:
            comma=','
        else:
            comma=']'
        future_row2+=str(future_row1[i])+comma
    
    # delete
    
    future_row=tuple(future_row1)
    last_row=tuple(last_row)
    
    future_row_data=list(future_row)
    last_row_data=list(last_row)
    
    # to last row, add age and sex
    
    last_row_data=[age1, sex1]+last_row_data
    
    
    last_row = normalizing(last_row_data)
    future_row = normalizing(future_row_data)
    

    for i in range(11):
        if future_row[i]>1:
            future_row[i]=1    

    # Close the database connection

    #conn.close()
    subtracted=[]
    for i,j in zip(last_row_data, future_row_data):
        subtracted.append(i-j)
    
    

    if last_row:
        # Write data to the CSV file
        with open(csv_file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(column_headers)  # Write the header row
            writer.writerow(last_row)  # Write the data row
    if future_row:
        # Write data to the CSV file
        with open(future_file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(column_headers)  # Write the header row
            writer.writerow(future_row)  # Write the data row
        
        
    return(id1, name1, age1, sex1,future_row2,subtracted, last_row_data, future_row_data)

# Usage with default parameters

id1, name1, age1, sex1, future_row, subtract, last_row_data, future_row_data= export_last_row_to_csv()
lrd=last_row_data.copy()
#print(f'babo{lrd}')

testtime=datetime.now().strftime('%m/%d/%Y')
current_state=pd.read_csv('current_state.csv')
judge1=int(current_state.values.tolist()[0][0])
sl.test_input(id1, testtime, lrd[2],lrd[3],lrd[4], lrd[5],lrd[6],lrd[7],lrd[8], lrd[9],lrd[10],judge1)
#print(first_page.C)
'''