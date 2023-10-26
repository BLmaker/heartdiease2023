# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 22:17:55 2023

@author: jlee150
"""

import sqlite3 


def make_query_str(arr):
    for i in range(len(arr)):
        arr[i]=str(arr[i])
    str2="','".join(arr)
    str2="'"+str2+"'"
    return(str2)

def user_data_fetch(id_num):
    
    query= 'select datetime, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope  from tests  where id='+str(id_num)
    try:
        conn1 = sqlite3.connect('health_data.db')
        cursor = conn1.cursor()
        cursor.execute(query)
        result=cursor.fetchall()
    finally: 
        conn1.close()
    return(result)


def user_id_fetch(id_num):
    query= 'select first_name, last_name, dob, sex  from users  where id='+str(id_num)
    try:
        conn1 = sqlite3.connect('health_data.db')
        cursor = conn1.cursor()
        cursor.execute(query)
        result=cursor.fetchall()
    finally: 
        conn1.close()
    return(result)
 



def test_input(id1,today, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, target):
    b=[id1,today, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, target]
    str2=make_query_str(b)
    str1= 'insert into tests(id, testtime, cp, trestbps, chol, fbs, restecg,'+\
        'thalach, exang, oldpeak, slope, target) values(' \
        + str2 +")"
    conn1 = sqlite3.connect('health_data.db')
    cursor = conn1.cursor()
    try: 
        cursor.execute(str1)  
        conn1.commit()
    finally:
        conn1.close()


def member_input(id1, fname, lname, dob, sex):
    b=[id1, fname, lname, dob, sex]
    str2=make_query_str(b)
    str1='insert into users(id, first_name, last_name, dob, sex)   values(' \
        + str2 +")"
    print(str1)
    
    conn1 = sqlite3.connect('health_data.db')
    cursor = conn1.cursor()
    try: 
        cursor.execute(str1)  
        conn1.commit()
    finally:
        conn1.close()
    
    
if __name__ == '__main__':    
  
    #member_input(5, 'Hong', 'Gildong', '1/15/1960', 1)
    #test_input(1,'10/23/2023',4,160,286,0,2,108,1,1.5,2,1)
    a=user_id_fetch(1)
    