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
