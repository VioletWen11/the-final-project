import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


st.title('Roller Coasters Around the World')

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path1 = os.path.join(current_dir, 'roller_coasters.csv')
file_path2 = os.path.join(current_dir, 'Golden_Tickert_Award_Winners_Steel.csv')

df1 = pd.read_csv(file_path1)

df2 = pd.read_csv(file_path2)

df3 = pd.read_csv(file_path2)


st.write('Notice: This app is built to analyse four parts of roller coasters around the world.')

# Part 1: The safe speed
st.subheader('Part 1: the Safe Speed')
st.write('According to the formula for circular motion v = (gr)^0.5, we choose g = 9.8 and r = height/2 to calculate the safe speed of roller coasters.')
fig, ax = plt.subplots(figsize=(20, 10))
v = 0
v_list=[]
df1 = df1[df1['height'] != 902]    
for i in df1['height']:
     v = ((i/2)*9.8)**0.5
     v_list.append(v)
plt.plot(v_list)
st.pyplot(fig)
st.write('As a result, the safe speed on the top should be between 0 and 35')
st.write('In order to build a safe roller coasters, the safe speed should be considered seriously.')


# Part 2: Material Type
st.subheader('Part 2: Material Type')
fig, ax=plt.subplots(figsize=(8, 5)) 
x = np.array(df1.material_type.value_counts()/len(df1.material_type))#用一维数组存入各个饼块的尺寸。
plt.pie(x, labels= ['Steel', 'na', 'Wooden', 'Hybrid'])
plt.show()#显示饼状图
st.pyplot(fig)
st.write('according to the data, there are about four different types of roller coasters. It can be seen from the data that steel is the most used material for roller coasters , while hybrid is the least. ')
st.write('Steel roller coasters are made for longer spans, more unique and more stable structures. Wooden roller coaster is the oldest and most classic, it can give people a unique sense of ups and downs, now the market began to use a new type of  mixed roller coaster, integrated the above two advantages')


# Part 3: regression analysis
st.subheader('Part 3: Linear Regression Analysis')
st.write('We use Excel to find the correlation of speed and height')
from PIL import Image
image_path1 = os.path.join(current_dir, 'regression1.jpg')
image = Image.open(image_path1)
st.image(image, caption='Sunrise by the mountains')
st.write('Since the P value is small, the model is doable')

image_path2 = os.path.join(current_dir, 'regression2.jpg')
image = Image.open(image_path2)
st.image(image, caption='Sunrise by the mountains')
st.write('y = height, x = speed')
st.write('We delete two extreme values(height = 902)')

image_path3 = os.path.join(current_dir, 'regression3.jpg')
image = Image.open(image_path3)
st.image(image, caption='Sunrise by the mountains')
st.write('When we select the data of high ranking roller coasters, we find the regression is dramatic.')

# Part 4: Popularity
st.subheader('Part 4: Popularity')
st.subheader('Steel Roller Coasters who won the Golden Ticket Award')
st.write('Notice: Choose the four categories in the sidebox before, or there may be erro for exceeding the limitation')
# points filter
points_filter = st.slider('The minimal points:', 0, 1400, 59)
df2 = df2[df2.Points >= points_filter]

st.subheader('Roller Collars and Their Points')

# create a input form
form = st.sidebar.form("park_form")
park_filter = form.text_input('Park Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")
if park_filter!='ALL':
    df2 = df2[df2.Park == park_filter]


genre = st.sidebar.radio(
    "Choose point level",
    ('Low 0~200', 'Medium 200~550', 'High 550~', 'All'))

if genre == 'Low 0~200':
    df2 = df2[df2.Points <= 200]
elif genre == 'Medium 200~550':
    df2 = df2[df2.Points > 200]
    df2 = df2[df2.Points < 550]
elif genre == 'High 550~':
    df2 = df2[df2.Points > 550]
elif genre == 'All':
    df2 == df2

df4 = df2[['Name', 'Park', 'Supplier', 'Points']]
fig, ax = plt.subplots(figsize=(20, 10))
x = df4.groupby('Name')['Points'].mean()
x.plot.bar(ax = ax)
st.pyplot(fig)

# park 与 评分
st.subheader('Parks and their Points')
fig, ax=plt.subplots()
df_park = df2[['Park', 'Points']].groupby('Park').mean()
df_park.sort_values('Points', ascending=False).plot.bar(ax=ax)
st.pyplot(fig)

# 生产年份与评分关系
st.subheader('The Built Year of the Roller Coaster and the Points They Got')
fig, ax=plt.subplots()
x = df2[['Year Built', 'Points']].groupby('Year Built').mean()
x.plot(ax=ax)
st.pyplot(fig)

# supplier 与 评分
st.subheader('Suppliers and Their Points')
fig, ax=plt.subplots()
df_park = df2[['Supplier', 'Points']].groupby('Supplier').mean()
df_park.sort_values('Points', ascending=False).plot.bar(ax=ax)
st.pyplot(fig)

# supplier 所拥有过山车的数量
st.subheader('The Percentage of Roller Coasters Owned by the Suppliers in the Market')
fig, ax=plt.subplots(figsize=(8, 5))
x = np.array(df3.Supplier.value_counts()/len(df3.Supplier))#用一维数组存入各个饼块的尺寸。
plt.pie(x, labels= ['B&M', 'Intamin', 'RMC', 'Schwarzkopf', 'Rocky Mountain', 'Mack', 'Arrow', 'Morgan', 'Lagan', 'Vekoma', 'Schwarz', 'Chance', 'Premier', 'Morgan/Arrow', 'Zierer'])#绘制饼状图，默认是从x轴正方向逆时针开始绘图
plt.show()#显示饼状图
st.pyplot(fig)

