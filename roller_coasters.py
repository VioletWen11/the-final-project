import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Use a built-in matplotlib style
plt.style.use('ggplot')

st.title('Roller Coasters Around the World')
df1 = pd.read_csv('roller_coasters.csv')
df2 = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
df3 = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
st.write('Notice: This app is built to analyse four parts of roller coasters around the world.')

# Part 1: The safe speed
st.subheader('Part 1: the Safe Speed')
st.write('According to the formula for circular motion v = (gr)^0.5, we choose g = 9.8 and r = height/2 to calculate the safe speed of roller coasters.')
fig, ax = plt.subplots(figsize=(20, 10))
v_list = []
df1 = df1[df1['height'] != 902]    
for i in df1['height']:
    v = ((i / 2) * 9.8) ** 0.5
    v_list.append(v)
ax.plot(v_list)
st.pyplot(fig)
st.write('As a result, the safe speed on the top should be between 0 and 35')
st.write('In order to build a safe roller coasters, the safe speed should be considered seriously.')

# Part 2: Material Type
st.subheader('Part 2: Material Type')
fig, ax = plt.subplots(figsize=(8, 5)) 
x = np.array(df1.material_type.value_counts() / len(df1.material_type))
ax.pie(x, labels=['Steel', 'na', 'Wooden', 'Hybrid'])
st.pyplot(fig)
st.write('According to the data, there are about four different types of roller coasters. It can be seen from the data that steel is the most used material for roller coasters, while hybrid is the least.')
st.write('Steel roller coasters are made for longer spans, more unique and more stable structures. Wooden roller coaster is the oldest and most classic, it can give people a unique sense of ups and downs. Now the market began to use a new type of mixed roller coaster, integrating the above two advantages.')

# Part 3: regression analysis
st.subheader('Part 3: Linear Regression Analysis')
st.write('We use Excel to find the correlation of speed and height')
image = Image.open('regression1.jpg')
st.image(image, caption='Regression Analysis')
st.write('Since the P value is small, the model is doable')

image = Image.open('regression2.jpg')
st.image(image, caption='Regression Analysis')
st.write('y = height, x = speed')
st.write('We delete two extreme values(height = 902)')
image = Image.open('regression3.jpg')
st.image(image, caption='Regression Analysis')
st.write('When we select the data of high ranking roller coasters, we find the regression is dramatic.')

# Part 4: Popularity
st.subheader('Part 4: Popularity')
st.subheader('Steel Roller Coasters who won the Golden Ticket Award')
st.write('Notice: Choose the four categories in the sidebox before, or there may be error for exceeding the limitation')
# points filter
points_filter = st.slider('The minimal points:', 0, 1400, 59)
df2 = df2[df2.Points >= points_filter]

st.subheader('Roller Coasters and Their Points')

# create an input form
form = st.sidebar.form("park_form")
park_filter = form.text_input('Park Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")
if park_filter != 'ALL':
    df2 = df2[df2.Park == park_filter]

genre = st.sidebar.radio(
    "Choose point level",
    ('Low 0~200', 'Medium 200~550', 'High 550~', 'All'))

if genre == 'Low 0~200':
    df2 = df2[df2.Points <= 200]
elif genre == 'Medium 200~550':
    df2 = df2[(df2.Points > 200) & (df2.Points < 550)]
elif genre == 'High 550~':
    df2 = df2[df2.Points > 550]

df4 = df2[['Name', 'Park', 'Supplier', 'Points']]
fig, ax = plt.subplots(figsize=(20, 10))
x = df4.groupby('Name')['Points'].mean()
x.plot.bar(ax=ax)
st.pyplot(fig)

# Parks and their points
st.subheader('Parks and their Points')
fig, ax = plt.subplots()
df_park = df2[['Park', 'Points']].groupby('Park').mean()
df_park.sort_values('Points', ascending=False).plot.bar(ax=ax)
st.pyplot(fig)

# Built year and points
st.subheader('The Built Year of the Roller Coaster and the Points They Got')
fig, ax = plt.subplots()
x = df2[['Year Built', 'Points']].groupby('Year Built').mean()
x.plot(ax=ax)
st.pyplot(fig)

# Suppliers and their points
st.subheader('Suppliers and Their Points')
fig, ax = plt.subplots()
df_park = df2[['Supplier', 'Points']].groupby('Supplier').mean()
df_park.sort_values('Points', ascending=False).plot.bar(ax=ax)
st.pyplot(fig)

# Percentage of roller coasters owned by suppliers
st.subheader('The Percentage of Roller Coasters Owned by the Suppliers in the Market')
fig, ax = plt.subplots(figsize=(8, 5))
x = np.array(df3.Supplier.value_counts() / len(df3.Supplier))
ax.pie(x, labels=['B&M', 'Intamin', 'RMC', 'Schwarzkopf', 'Rocky Mountain', 'Mack', 'Arrow', 'Morgan', 'Lagan', 'Vekoma', 'Schwarz', 'Chance', 'Premier', 'Morgan/Arrow', 'Zierer'])
st.pyplot(fig)
