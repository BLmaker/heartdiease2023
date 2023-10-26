import sqlite3
import csv
from normalization import normalizing
from functions import do_regression, merge_table, forecasting
import pandas as pd
import math
from sklearn.linear_model import LinearRegression
from datetime import datetime

# Function to create and initialize the database
def initialize_database():
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()

    # Create the "lifestyle" table
    cursor.execute('''CREATE TABLE IF NOT EXISTS lifestyle (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        smoking INT,
                        alcohol INT,
                        sodium INT,
                        fat INT,
                        exercise INT,
                        weight REAL,
                        height REAL,
                        stress INT,
                        sleep_hours REAL,
                        water_consumption REAL
                    )''')

    # Create the "User input" table
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_input (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        age INT,
                        sex TEXT,
                        cp INT,
                        trestbps INT,
                        chol INT,
                        fbs INT,
                        restecg INT,
                        thalach INT,
                        exang INT,
                        oldpeak REAL,
                        slope INT
                    )''')

    conn.commit()
    conn.close()

# Function to insert user input data into the "lifestyle" and "User input" tables
def insert_data_into_tables_old(lifestyle_data, user_input_data):
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()

    # Insert user input data into the "lifestyle" table
    cursor.execute('''INSERT INTO lifestyle 
                      (smoking, alcohol, sodium, fat, exercise, weight, height, stress, sleep_hours, water_consumption)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   lifestyle_data)

    # Insert user input data into the "User input" table
    #cursor.execute('''INSERT INTO user_input
     #                 (age, sex, cp, trestbps, chol, fbs,
      #                restecg, thalach, exang, oldpeak, slope)
       #               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        #           user_input_data)
    
    cursor.execute('''INSERT INTO user_input
                      (age, sex, cp, trestbps, chol, fbs,
                      restecg, thalach, exang, oldpeak, slope)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   user_input_data)
    user_input_data[1]=datetime.now().strftime('%m/%d/%Y')
    cursor.execute('''INSERT INTO tests
                      (id, testtime, cp, trestbps, chol, fbs,
                      restecg, thalach, exang, oldpeak, slope)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   user_input_data)

    conn.commit()
    conn.close()


def insert_data_into_tables(user_input_data):
    uk=pd.DataFrame(user_input_data) #from first page
    uk.to_csv('current_user_input_data.csv')