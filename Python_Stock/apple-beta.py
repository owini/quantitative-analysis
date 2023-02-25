import pandas as pd
import statsmodels.api as sm

# Load historical data for Apple and the S&P 500
aapl = pd.read_csv('AAPL.csv', index_col='Date', parse_dates=True)['Adj Close'].pct_change().dropna()
spy = pd.read_csv('SPY.csv', index_col='Date', parse_dates=True)['Adj Close'].pct_change().dropna()

# Combine the data into a single DataFrame
data = pd.concat([aapl, spy], axis=1)
data.columns = ['AAPL', 'SPY']

# Define the dependent and independent variables for the regression
X = sm.add_constant(data['SPY'])
y = data['AAPL']

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Print the beta coefficient (slope)
print('Beta of Apple:', model.params['SPY'])
