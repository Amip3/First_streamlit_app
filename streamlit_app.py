import streamlit
streamlit.title(' My New Healthy Menu for this Month')

streamlit.header(':sunrise: Breakfast Menu')
streamlit.text('Apple & Blueberry Oatmal')
streamlit.text('Berry smothie and yogurt Smoothie')
streamlit.text(' Avocado toast with organic Egg')


import pandas

streamlit.title(':banana::strawberry: Build Your Own Fruit Smoothie 🍋 🍍')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#  Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Straberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)
