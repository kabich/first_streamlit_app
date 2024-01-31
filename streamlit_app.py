import streamlit
import pandas as pd

df  = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

streamlit.dataframe(df)


streamlit.multiselect('pick some fruits', df['Fruit'].unique(), ['Avocado','Strawberries'])
