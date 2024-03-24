import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_white"

data = pd.read_csv("C:\\Users\\vamsh\\Downloads\\credit_scoring.csv")
print(data.head())

print(data.info())
print(data.describe())
