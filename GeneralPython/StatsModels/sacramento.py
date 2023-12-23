#pip install statsmodels pandas
import pandas as pd
import statsmodels.api as sm

# Load the CSV file
df = pd.read_csv('sacramento.csv')

# Create a new variable 'has_more_than_one_bath' based on 'baths'
df['has_more_than_one_bath'] = (df['baths'] > 1).astype(int)

# Select columns for the logistic regression
independent_vars = ['beds', 'sq__ft', 'price']

# Add a constant term
X = sm.add_constant(df[independent_vars])

# Define the dependent variable
y = df['has_more_than_one_bath']

# Fit the logistic regression model
logit_model = sm.Logit(y, X)
result = logit_model.fit()

# Print the results
print(result.params.round(2))
print(result.pvalues.round(2))
print('The smallest p-value is for sq__ft')