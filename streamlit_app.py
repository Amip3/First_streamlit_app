import streamlit
streamlit.title(' My New Healthy Menu for this Month')

streamlit.header(':sunrise: Breakfast Menu')
streamlit.text('Apple & Blueberry Oatmal')
streamlit.text('Berry smothie and yogurt Smoothie')
streamlit.text(' Avocado toast with organic Egg')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
