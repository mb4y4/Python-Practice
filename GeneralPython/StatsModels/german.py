#pip install statsmodels pandas
import pandas as pd
import statsmodels.api as sm

# Load the CSV file
df = pd.read_csv('german_credit_data.csv')

# Rename the 'Credit amount' column to 'Credit_amount'
df.rename(columns={'Credit amount': 'Credit_amount'}, inplace=True)

# Select columns for the regression
independent_vars = ['age', 'duration']

# Add a constant term
df['const'] = 1

# Fit the regression model
model = sm.OLS(df['Credit_amount'], sm.add_constant(df[independent_vars])).fit()

# Print the results
print("Coefficients:")
print(model.params.round(2))
print(f"R-squared: {model.rsquared.round(2)}")
