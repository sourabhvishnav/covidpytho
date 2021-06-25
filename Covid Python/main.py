import plotly.express as px
import pandas as pd

data = pd.read_csv('data.csv')
fig = px.scatter(data, x='date', y='cases', size='cases',
                 color='country', size_max=60)
fig.show()