import streamlit
import pandas as pd
import requests

df  = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')




data_selected = streamlit.multiselect('pick some fruits', df['Fruit'].unique(), ['Avocado','Strawberries'])

streamlit.dataframe(df.loc[df['Fruit'].isin(data_selected)])


streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
