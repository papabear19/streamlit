# https://www.youtube.com/watch?v=5i97NL1bYdQ

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
		page_title = 'Iris',
		layout = 'wide',
	)

st.title('Iris Data Analysis')

with st.sidebar:
	st.markdown('**Pilih Species**')
	check_setosa = st.checkbox('Iris-setosa')
	check_versicolor = st.checkbox('Iris-versicolor')
	check_virginica = st.checkbox('Iris-virginica')

	species = []
	if check_setosa:
		species.append('Iris-setosa')
	if check_versicolor:
		species.append('Iris-versicolor')
	if check_virginica:
		species.append('Iris-virginica')
	
	st.markdown('**Pilih Variabel**')
	var1 = st.radio('Variabel Utama',
			('SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm')
		)
	var2 = st.radio('Variabel Sekunder',
			('SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm')
		)

data = pd.read_csv('iris_data.csv')
data = data.query('Species in @species')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
	st.dataframe(data)

with col2:
	fig_pie = px.pie(data, names='Species')
	st.plotly_chart(fig_pie, use_container_width=True)

with col3:
	fig_box = px.box(data, x=var1, color='Species')
	st.plotly_chart(fig_box, use_container_width=True)

with col4:
	fig_scatter = px.scatter(data, x=var1, y=var2, color='Species')
	st.plotly_chart(fig_scatter, use_container_width=True)

# python -m venv env --> bikin environment
# env\Scripts\activate --> aktivasi environment
# pip install streamlit --> install streamlit
# streamlit run namafile.py --> running