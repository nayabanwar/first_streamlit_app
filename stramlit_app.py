import streamlit
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index),['Avacado','Strawberries'])
fruit_selected=streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index)
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
                                     
                      
          
