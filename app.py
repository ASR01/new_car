import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk
import time
#import columns_enhancement as ce
from sklearn.ensemble import ExtraTreesRegressor


# Import the model

#model = pickle.load(open('./model/optimal_model.pkl','rb'))

# Import the default data
#@st.cache

model = pk.load(open('./model/optimal_model.pkl','rb'))
pipe = pk.load(open('./model/pipe_model.pkl','rb'))

df =  pd.read_csv('./data/enhanced_data.csv')
dfd = pd.read_csv('./data/default_values.csv')

brandtype = df['brandtype'].unique()
carbody = df['carbody'].unique()
fueltype = df['fueltype'].unique()       
aspiration = df['aspiration'].unique()
doornumber = df['doornumber'].unique()
carbody = df['carbody'].unique()
drivewheel = df['drivewheel'].unique()                 
enginelocation = df['enginelocation'].unique()          
enginetype = df['enginetype'].unique()
cylindernumber = df['cylindernumber'].unique()      
fuelsystem  = df['fuelsystem'].unique()            
symboling = df['symboling'].unique()
enginesize = df['enginesize'].unique() 
boreratio = df['boreratio'].unique()
drivewheel = df['drivewheel'].unique()
boreratio = df['boreratio'].unique()

fueltype.sort()
cylindernumber.sort()


#Main Text

st.markdown("# Finding the best market pricing for your new car model.")

st.markdown(""" #### Please select the parameters you are thinking to target.""")



dfd.loc[0,'brandtype'] = st.selectbox('Select the type of brand you want to emulate', brandtype) 


dfd.loc[0,'carbody'] = st.selectbox('Select the type of carbody you want to construct', carbody) 

#selection


st.write('Apart of the brand positioning which are the typical values of the type of car you are looking for?') 

#Chassis

if st.checkbox("Select Chassis Parameters"):
	st.write("Please select the chassis related parameters.")
	
	col1, col2, col3 = st.columns(3)
 
	with col1:
		dfd.loc[0,'carheight'] =	st.slider('Select the Car Height',  min_value = 20, max_value = 120, value = round(dfd.loc[0,'carheight']), step = 1)
		dfd.loc[0,'doornumber'] = 	st.selectbox('Select the number of doors.', doornumber)
	with col2:
		dfd.loc[0,'carlength'] = 	st.slider('Select the Car Length', min_value = 100, max_value = 200, value = round(dfd.loc[0,'carlength']), step = 1)
	with col3:
		dfd.loc[0,'carwidth'] = 	st.slider('Select the Car Width',  min_value = 20, max_value = 120, value = round(dfd.loc[0,'carwidth']), step = 1)
		dfd.loc[0,'curbweight'] =  	st.slider('Select the Curb Weight',  min_value = 20, max_value = 120, value = round(dfd.loc[0,'curbweight']), step = 10)

#print(dfd)

#Motor
if st.checkbox("Select Motor Parameters"):
	st.write("Please select the motor related parameters.")
	col1, col2, col3 = st.columns(3)
	with col1:
		dfd.loc[0,'fueltype'] = st.selectbox('Type of fuel.', fueltype)
		dfd.loc[0,'aspiration'] = st.selectbox('Type of aspiration of the engine.', aspiration)
		dfd.loc[0,'highwaympg'] =  st.slider('Mileage per gallon in highways.',min_value = 3, max_value = 50,value = round(dfd.loc[0,'highwaympg']),step = 1)
		dfd.loc[0,'fuelsystem']= st.selectbox('Fuel system for the engine.', fuelsystem) 
	
	with col2:
		dfd.loc[0,'enginelocation'] = st.selectbox('Location of the engine.', enginelocation)          
		dfd.loc[0,'enginesize']= st.selectbox('Engine size.', enginesize)
		dfd.loc[0,'stroke'] =  st.slider('Stroke type.',min_value = 20, max_value = 300,value = round(dfd.loc[0,'carlength']),step = 1)
		dfd.loc[0,'peakrpm'] =  st.slider('Peak RPM number',min_value = 5000, max_value = 12000,value = round(dfd.loc[0,'peakrpm']),step = 500)

	with col3:
		dfd.loc[0,'enginetype'] = st.selectbox('Type of engine.', enginetype)
		dfd.loc[0,'cylindernumber'] = st.selectbox('Number of cylinders.', cylindernumber)      
		dfd.loc[0,'compressionratio'] = st.slider('Compression Ratio',min_value = 1, max_value = 30,value = round(dfd.loc[0,'compressionratio']),step = 1)
		dfd.loc[0,'citympg'] =  		st.slider('Mileage per gallon in urban environment',min_value = 3, max_value = 50,value = round(dfd.loc[0,'citympg']),step = 1)


#Others
if st.checkbox("Select other car parameters"):
    st.write("Please select other related parameters.")
    col1, col2, col3 = st.columns(3)
    with col1:
        dfd.loc[0,'symboling'] = st.selectbox('Type of insurance modifier.', symboling, )
    with col2:
        dfd.loc[0,'drivewheel'] =  st.selectbox('Train drive',drivewheel)
    with col3:
        dfd.loc[0,'wheelbase'] = st.slider('Wheelbase',min_value = 3, max_value = 50,value = round(dfd.loc[0,'highwaympg']), step = 10)




#st.dataframe(dfd)

test = pipe.predict(dfd)


if (st.button("Calculate prediction ")):
	yprediction = pipe.predict(dfd)
	st.write('The predicted price is in the range of:' ,str (round(yprediction[0])) )
	print(type(yprediction))
	print(yprediction[0])

