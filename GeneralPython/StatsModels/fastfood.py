
# Use the fastfood.csv file to complete the following assignment. Create a file,
# fastfood.py, that loads the .csv file and runs a regression predicting calories from
# total_fat, sat_fat, cholesterol, and sodium, in that order. Add a constant using
# sm.add_constant(data).
# ● Then, print the following to two decimals
# print(model.mse_total.round(2))
# print(model.rsquared.round(2))
# print(model.params.round(2))
# print(model.pvalues.round(2))


#pip install statsmodels pandas
import pandas as pd
import statsmodels.api as sm

# Load the CSV file
df = pd.read_csv('fastfood.csv')

# Select columns for the regression
independent_vars = ['total_fat', 'sat_fat', 'cholesterol', 'sodium']

# Add a constant term
df['const'] = 1

# Fit the regression model
model = sm.OLS(df['calories'], sm.add_constant(df[independent_vars])).fit()

# Print the results
print(f"MSE Total: {model.mse_total.round(2)}")
print(f"R-squared: {model.rsquared.round(2)}")
print("Coefficients:")
print(model.params.round(2))
print("P-values:")
print(model.pvalues.round(2))
