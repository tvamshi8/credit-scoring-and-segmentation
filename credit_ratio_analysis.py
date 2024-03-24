import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_white"

data = pd.read_csv("C:\\Users\\vamsh\\Downloads\\credit_scoring.csv")
print(data.head())

print(data.info())
print(data.describe())


credit_utilization_fig = px.box(data, y='Credit Utilization Ratio',
                                title='Credit Utilization Ratio Distribution')
credit_utilization_fig.show()

loan_amount_fig = px.histogram(data, x='Loan Amount', 
                               nbins=20, 
                               title='Loan Amount Distribution')
loan_amount_fig.show()
numeric_df = data[['Credit Utilization Ratio', 
                   'Payment History', 
                   'Number of Credit Accounts', 
                   'Loan Amount', 'Interest Rate', 
                   'Loan Term']]
correlation_fig = px.imshow(numeric_df.corr(), 
                            title='Correlation Heatmap')
correlation_fig.show()