
# Use the german_credit_data.csv file to complete the following assignment.
# Create a file, german.py, that loads the .csv file and runs a regression predicting
# credit amount from age and duration, in that order. Add a constant using
# sm.add_constant(data).
# ● You will need to rename the column 'Credit amount' to 'Credit_amount'.
# ● Then, print the parameters and R-squared to 2 decimals using
# print(model.params.round(2))
# print(model.rsquared.round(2))


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
