from curses import def_shell_mode
import streamlit as st
st.title('Hello from cxy')
import pandas as pd
import matplotlib.pyplot as plt

# create datadrame
df = pd.DataFrame({
    'name':['John', 'Mary', 'Tom'],
    'gender':['male', 'female', 'male'],
    'age':[20, 22, 21],
})

# set title
st.title('first app')

# show dataframe
st.write(df)

# show a plot

fig, ax = plt.subplots()
df.age.plot(ax=ax)
st.pyplot(fig)
plt.style.use('seaborn')

df = pd.read_csv('worldcities.csv')
df.head()

df.population.describe()


plt.style.use('seaborn')


st.title('World Cites')
df = pd.read_csv('worldcities.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
population_filter = st.slider('Minimal Population (Millions):', 0.0, 40.0, 3.6)  # min, max, default

# create a multi select
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  # options
     df.capital.unique())  # defaults

# create a input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")


# filter by population
df = df[df.population >= population_filter]

# filter by capital
df = df[df.capital.isin(capital_filter)]

if country_filter!='ALL':
    df = df[df.country == country_filter]

# show on map
st.map(df)

# show dataframe
st.subheader('City Details:')
st.write(df[['city', 'country', 'population']])

# show the plot
st.subheader('Total Population By Country')
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)