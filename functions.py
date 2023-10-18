# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 23:07:42 2023

@author: jlee150
"""

import pandas as pd
import math
from sklearn.linear_model import LinearRegression

        
        

def do_regression(data_x,data_y, hat_x):
    hat_x=pd.Series(pd.to_datetime(hat_x)).values.astype(float)
    lm=LinearRegression()
    model=lm.fit(data_x.values.reshape(-1,1), data_y)
    predictions = lm.predict(hat_x.reshape(-1,1))
    for i in range(2):
        predictions=sum(predictions)
    return (predictions)



def merge_table(table1, today1,gender, input_data):
    table1=table1.drop(table1.columns[10], axis=1)
    sex1=[gender]*table1.shape[0]
    ###
    table1.insert(1, 'sex', sex1)
    ###
    #print(table1)
    head1=[today1, gender]+input_data
    #print(type(table1))
    table1.loc[len(table1)]=head1
    return(table1)


def forecasting(dbname, input_data):
    future_output=[0]*11
    f=open(dbname)
    info=f.readline()
    f.close()
    regdata1 = pd.read_csv(dbname, parse_dates=['date'], skiprows=1)
    regdata1 = regdata1.drop(regdata1.columns[0], axis=1)
    #print(regdata1[0,:])
    info1=info.split(',')
    
    name=info1[0]
    
    dob=pd.to_datetime(info1[1])
    sex=info1[2].rstrip().strip()
    
    if sex=='M':
        gender=1
    else:
        gender=0

    # Load the time series data
    today1=pd.to_datetime('today')
    #print(today1)
    #data = pd.read_csv('swiss3.csv', parse_dates=['date'], skiprows=1)
    age=math.floor((today1.normalize()-
                    pd.to_datetime(dob).normalize())/(pd.Timedelta('365 days')))
    
    a1=pd.DateOffset(days=365)
    next_year=pd.to_datetime('today')+a1
    
    # input age, sex,  input the current values into the table
    future_output[0]=age+1
    future_output[1]=gender
    for i in range(len(input_data)):
        future_output[i+2]=input_data[i]
    
    regdata1=merge_table(regdata1,today1,gender,input_data )
    columns1=[4,5,8,10]
    #print(regdata1.head())
    for i in columns1:
        #print(i)
        data_x=pd.to_datetime(regdata1['date'], format='%Y-%m-%d')
        data_y=regdata1.iloc[:,i-1].values.reshape(-1,1)
        reg1=do_regression(data_x, data_y, next_year)
        reg1=math.floor(reg1)
        future_output[i-1]=reg1
        
    return name,age,gender,next_year,future_output

if __name__ == '__main__':
    
    

    dbname='swiss3.csv'
    reg2=pd.read_csv('reg2.csv')
    reg2=reg2.drop(columns=['Unnamed: 0'], axis=1)
    
    input_data=[4,160,286,0,2,108,1,1.5,2]
    

    name,age1,sex1,year1,d=forecasting(dbname, input_data)
    