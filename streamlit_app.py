import streamlit
import pandas as pd
import requests
import snowflake.connector

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


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute('select * from pc_rivery_db.public.fruit_load_list')
