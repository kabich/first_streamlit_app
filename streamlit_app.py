import streamlit
import pandas as pd
import requests

df  = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')




data_selected = streamlit.multiselect('pick some fruits', df['Fruit'].unique(), ['Avocado','Strawberries'])

streamlit.dataframe(df.loc[df['Fruit'].isin(data_selected)])


streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
streamlit.text(fruityvice_response)

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruit_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
df_fruit = pd.json_normalize(fruit_response.json())
streamlit.dataframe(df_fruit)
