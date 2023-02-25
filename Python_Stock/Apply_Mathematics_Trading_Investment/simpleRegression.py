import pandas as pd
import statsmodels.api as sm

# Load data from CSV file
data = pd.read_csv('data.csv')

# Extract independent and dependent variables
y_col = 'dependent_variable'
x_cols = ['independent_variable_1', 'independent_variable_2', 'independent_variable_3']
X = sm.add_constant(data[x_cols])
y = data[y_col]

# Fit linear regression models for each independent variable
for col in x_cols:
    model = sm.OLS(y, sm.add_constant(data[col])).fit()
    print(f'Regression results for {col}:')
    print(model.summary())
