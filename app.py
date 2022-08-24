import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os
from PIL import Image

#iris_data = load_iris()
## separate the data into features and target
#features = pd.DataFrame( iris_data.data, columns=iris_data.feature_names)
#target = pd.Series(iris_data.target)

## split the data into train and test
#x_train, x_test, y_train, y_test = train_test_split( features, target, test_size=0.2, stratify=target )

##model
#model = RandomForestClassifier()

#def plot_pie_chart(probabilities):
    #fig = go.Figure(
            #data=[go.Pie(
                #labels=list(iris_data.target_names),
                #values=probabilities[0]
            #)]
        #)
    #fig = fig.update_traces(
            #hoverinfo='label+percent',
            #textinfo='value',
            #textfont_size=15
        #)
    #return fig

#def construct_sidebar():
    #cols = [col for col in features.columns]
    
    #st.sidebar.markdown( '<p class="header-style">Iris Data Classification</p>', unsafe_allow_html=True )
    #sepal_length = st.sidebar.selectbox(f"Select {cols[0]}", sorted(features[cols[0]].unique()) )
    
    #sepal_width = st.sidebar.selectbox(f"Select {cols[1]}",sorted(features[cols[1]].unique()) )
    
    #petal_length = st.sidebar.selectbox(f"Select {cols[2]}", sorted(features[cols[2]].unique()) )
    
    #petal_width = st.sidebar.selectbox( f"Select {cols[3]}", sorted(features[cols[3]].unique()) )
    #values = [sepal_length, sepal_width, petal_length, petal_width]    
    #return values
    

#def main():
st.title("DuraMAT Streamlit Analysis App")

dmt_image=Image.open('https://raw.githubusercontent.com/starman91/Iris-Example/main/images/logo-duramat-reversed-600.png')
st.image(dmt_image)
st.subheader("Hello Researcher")
    
    #values = construct_sidebar()
    
    #model.fit(x_train, y_train)
    #values_to_predict = np.array(values).reshape(1, -1)
    #values_to_predict = np.array(values).reshape(1, -1)
    #prediction = model.predict(values_to_predict)
    #prediction_str = iris_data.target_names[prediction[0]]
    #probabilities = model.predict_proba(values_to_predict)    
    
    #st.markdown(
        #"""
        #<style>
        #.header-style {
            #font-size:25px;
            #font-family:sans-serif;
        #}
        #</style>
        #""",
        #unsafe_allow_html=True
    #)

    #st.markdown(
        #"""
        #<style>
        #.font-style {
            #font-size:20px;
            #font-family:sans-serif;
        #}
        #</style>
        #""",
        #unsafe_allow_html=True
    #)
    #st.markdown(
        #'<p class="header-style"> Iris Data Predictions </p>',
        #unsafe_allow_html=True
    #)

    #column_1, column_2 = st.columns(2)
    #column_1.markdown( f'<p class="font-style" >Prediction </p>', unsafe_allow_html=True )
    #column_1.write(f"{prediction_str}")

    #column_2.markdown( '<p class="font-style" >Probability </p>', unsafe_allow_html=True )
    #column_2.write(f"{probabilities[0][prediction[0]]}")

    #fig = plot_pie_chart(probabilities)
    #st.markdown( '<p class="font-style" >Probability Distribution</p>', unsafe_allow_html=True )
    #st.plotly_chart(fig, use_container_width=True)    
    
      
#if __name__ == '__main__':
    #main()
