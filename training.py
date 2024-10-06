import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import pickle
xgb = pickle.load(open('xgb_model.pkl','rb'))
rand_model = pickle.load(open('rand_model.pkl','rb'))
dec_model = pickle.load(open('dec_model.pkl','rb'))
dl_model = pickle.load(open('dl.pkl','rb'))
svc = pickle.load(open('svc_model.pkl','rb'))
log_model = pickle.load(open('log_model.pkl','rb'))

scaler = pickle.load(open('scaler.pkl','rb'))

df = pd.read_csv('new_data.csv')
x = df.drop('Target',axis=1)
y = df.Target

x_scaled = scaler.transform(x)
x_scaled = pd.DataFrame(x_scaled,columns=x.columns)
#x_scaled

#train sets
x_train = x_scaled.iloc[:2650,:]
y_train = y.iloc[:2650]

#validation sets
x_val = x_scaled.iloc[2650:3650,:]
y_val = y.iloc[2650:3650]

#test sets
x_test = x_scaled.iloc[3650:,:]
y_test = y.iloc[3650:]

model_score = []
def fit_model(model,x_train,x_val,y_train,y_val):
    model.fit(x_train,y_train)
    model_score  = model.score(x_val,y_val)
    return model_score

model_score=fit_model(model = log_model,
          x_train=x_train,
          x_val=x_val,
          y_train=y_train,
          y_val=y_val)
