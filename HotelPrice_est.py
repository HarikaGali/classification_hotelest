### Hotel Price estimation ###

# Base Libraries
import pandas as pd
import numpy as np

# Deployment libraries
import streamlit as sl
#model pickled lib
import joblib
############# Data File ###########
data=pd.read_csv("hotelfinal")

data.dropna(axis=0).reset_index(drop=True)

########### Loading Trained Model Files ########
model = joblib.load("Hotel_price.pkl")
model_ohe = joblib.load("Hotel_ohe.pkl")
model_sc = joblib.load("Hotel_sc.pkl")

########## UI Code #############

# Ref: https://docs.streamlit.io/library/api-reference

# Title
sl.title("Hotel Price estimation")

sl.dataframe(data.head())


