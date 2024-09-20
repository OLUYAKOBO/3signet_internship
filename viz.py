import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


st.title('Interactive Data Visualization Dashboard with Plotly')
st.markdown("""
Explore your dataset interactively by selecting different visualizations 
and applying filters using the controls on the left.
""")


@st.cache_data
def load_data():
    data = pd.read_csv('students_dropout.csv') 
    return data

data = load_data()


st.sidebar.header('Data Filtering Options')

if st.sidebar.checkbox('Show data overview'):
    st.subheader('Dataset Overview')
    st.write(data.head(2))

#Select columns for scatter plot
st.sidebar.subheader('Scatter Plot Options')
scatter_x = st.sidebar.selectbox('Select X-axis for Scatter Plot',
                                ['Admission grade','Age at enrollment',
                                 'Curricular units 1st sem (without evaluations)',
                                 'Curricular units 2nd sem (credited)',
                                 'Curricular units 2nd sem (enrolled)',
                                 'Curricular units 2nd sem (evaluations)',
                                 'Curricular units 2nd sem (approved)',
                                 'Curricular units 2nd sem (grade)',
                                 'Curricular units 2nd sem (without evaluations)'])

scatter_y = st.sidebar.selectbox('Select Y-axis for Scatter Plot',
                                ['Admission grade','Age at enrollment',
                                 'Curricular units 1st sem (without evaluations)',
                                 'Curricular units 2nd sem (credited)',
                                 'Curricular units 2nd sem (enrolled)',
                                 'Curricular units 2nd sem (evaluations)',
                                 'Curricular units 2nd sem (approved)',
                                 'Curricular units 2nd sem (grade)',
                                 'Curricular units 2nd sem (without evaluations)'])

scatter_color = st.sidebar.selectbox('Select color for Scatter Plot', data.select_dtypes(include=['object', 'category']).columns)

#st.write(plt.scatter(data[scatter_x],data[scatter_y]))
    
st.subheader('Visualizations')

# Scatter Plot
st.markdown('**Scatter Plot**')
scatter_fig = px.scatter(data, x=scatter_x, y=scatter_y, color=scatter_color,
                         title=f'Scatter Plot: {scatter_x} vs {scatter_y}')
st.plotly_chart(scatter_fig)

# Histogram
st.sidebar.subheader('Histogram Options')
hist_column = st.sidebar.selectbox('Select column for histogram', ['Admission grade','Age at enrollment',
                                                                   'Curricular units 1st sem (without evaluations)',
                                                                   'Curricular units 2nd sem (credited)',
                                                                   'Curricular units 2nd sem (enrolled)',
                                                                   'Curricular units 2nd sem (evaluations)',
                                                                   'Curricular units 2nd sem (approved)',
                                                                   'Curricular units 2nd sem (grade)',
                                                                   'Curricular units 2nd sem (without evaluations)'])
bins = st.sidebar.slider('Number of bins', 5, 50, 20)

st.markdown('**Histogram**')
hist_fig = px.histogram(data, x=hist_column, nbins=bins,
                        title=f'Histogram of {hist_column}')
st.plotly_chart(hist_fig)



# Bar Chart
st.sidebar.subheader('Bar Chart Options')
bar_x = st.sidebar.selectbox('Select X-axis for bar chart', ['Nacionality','Target','Debtor','Scholarship holder',
                                                             'Tuition fees up to date',
                                                             'Gender',
                                                             'Displaced',
                                                             'Marital status'])
bar_y = st.sidebar.selectbox('Select Y-axis for bar chart', ['Nacionality','Target','Debtor','Scholarship holder',
                                                             'Tuition fees up to date',
                                                             'Gender',
                                                             'Displaced',
                                                             'Marital status'])

st.markdown('**Bar Chart**')
bar_fig = px.bar(data, x=bar_x, y=bar_y,title=f'Bar Chart: {bar_x} vs {bar_y}')
st.plotly_chart(bar_fig)
   
    
    
    
    
    
    
    
    
    
    
    
    
    
