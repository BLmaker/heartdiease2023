# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:57:10 2023

@author: jlee150
"""


from sklearn import svm
from sklearn.naive_bayes import GaussianNB

import pandas as pd
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.linear_model import LogisticRegression
from normalization import normalizing


def svm_fn(joe):
    with open('svm_model.pkl', 'rb') as f:
        sm1 = pickle.load(f)
    joe=np.array(joe).reshape(1,-1)
    prediction_of_one_line=sm1.predict(joe)
    return prediction_of_one_line[0]

    
def nb_fn(joe):
    with open('nb_model.pkl', 'rb') as f:
        nb1 = pickle.load(f)
    joe=np.array(joe).reshape(1,-1)
    prediction_of_one_line=nb1.predict(joe)
    return prediction_of_one_line[0]


def dt_fn(joe):
    with open('dt_model.pkl', 'rb') as f:
        dt1 = pickle.load(f)
    joe=np.array(joe).reshape(1,-1)
    prediction_of_one_line=dt1.predict(joe)
    return prediction_of_one_line[0]

def rf_fn(joe):
    with open('rf_model.pkl', 'rb') as f:
        rf1 = pickle.load(f)
    joe=np.array(joe).reshape(1,-1)
    prediction_of_one_line=rf1.predict(joe)
    return prediction_of_one_line[0]


def lr_fn(joe):
    joe=normalizing(joe)
    with open('lr_model.pkl', 'rb') as f:
        lr1 = pickle.load(f)
    joe=np.array(joe).reshape(1,-1)
    prediction_of_one_line=lr1.predict(joe)
    return prediction_of_one_line[0]


def knn_fn(joe):
    joe=normalizing(joe)
    with open('knn_model.pkl', 'rb') as f:
        knn = pickle.load(f)
    joe=np.array(joe).reshape(1,-1)
    prediction_of_one_line=knn.predict(joe)
    return prediction_of_one_line[0]

if __name__ == "__main__":
    juan=[47,1,4,160,286,0,2,108,1,1.5,2]