import pandas as pd
import numpy as np
import plotly.express as px

yashdata = pd.read_csv("data.csv")
print(yashdata.head())

high_price = yashdata.sort_values(by='price', ascending=False).head(300000)

flight_count = high_price['airline'].value_counts()
fig = px.bar(
    x=flight_count.index,
    y=flight_count.values,
    title="Airline Count In Top 100 High Price Flight",
    labels={"x":"Airline","y":"Count"}
)
fig.show()



import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv("data.csv")

grouped = df.groupby(['airline', 'destination_city']).size().reset_index(name='flight_count')
print(grouped.head())

fig = px.bar(
    grouped,
    x='airline',
    y='flight_count',
    color='destination_city',
    title='Flight Count by Airline and Destination City',
    labels={'flight_count': 'Number of Flights'},
    barmode='group'
)
fig.show()
