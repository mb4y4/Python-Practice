
# Use the sacramento.csv file to complete the following assignment. Create a file,
# sacramento.py, that loads the .csv file and runs a logistic regression. The
# regression should predict whether or not a house has 1 or more than one
# bathroom based on beds, sqft, and price, in that order.
# ● You will need to create a new variable from baths, and it should make it such that
# those observations of 1 bath correspond to a value of 0, and those with more
# than 1 bath correspond to a 1.
# ● Make sure to add a constant using sm.add_constant(X)
# ● Your file should print the results in this way:
# print(mod.params.round(2))
# print(mod.pvalues.round(2))
# print('The smallest p-value is for sqft')


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