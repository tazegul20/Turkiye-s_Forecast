import pandas as pd
import mysql.connector as connection
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl as op
from plotly.express import choropleth
conn= connection.connect(
    host='localhost',
    user='root',
    password='22102001',
    database='vscode_db'
)
query="""
SELECT*FROM `Turkiye_forecast`
"""
df=pd.read_sql(query,conn)
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
budget_balance = df.columns[0]
current_account = df.columns[1]
economic_growth= df.columns[2]
inflation= df.columns[3]
investment=df.columns[4]


ax = sns.barplot(data=df)
for i in ax.containers:  """ I wanted to see the values on top of the bars so I added a function to execute it """
    ax.bar_label(i,)

plt.title("Turkey's Forecast")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()
plt.show()
