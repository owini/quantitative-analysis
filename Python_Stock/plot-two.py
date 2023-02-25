import pandas as pd
import matplotlib.pyplot as plt

# Load historical data for Oracle and Intel
orcl = pd.read_csv('ORCL.csv', index_col='Date', parse_dates=True)['Adj Close']
intc = pd.read_csv('INTC.csv', index_col='Date', parse_dates=True)['Adj Close']

# Combine the data into a single DataFrame
data = pd.concat([orcl, intc], axis=1)
data.columns = ['Oracle', 'Intel']

# Calculate daily percentage changes
returns = data.pct_change()

# Plot the stock prices on the same graph
fig, ax = plt.subplots()
ax.plot(returns.index, returns['Oracle'], label='Oracle')
ax.plot(returns.index, returns['Intel'], label='Intel')
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Daily percentage change')
ax.set_title('Oracle vs Intel Stock Performance')
plt.show()
