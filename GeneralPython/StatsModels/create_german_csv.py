import csv

# Sample data
data = [
    {'Age': 25, 'Duration': 12, 'Credit_amount': 1500},
    {'Age': 30, 'Duration': 24, 'Credit_amount': 3000},
    {'Age': 35, 'Duration': 18, 'Credit_amount': 2000},
    {'Age': 40, 'Duration': 36, 'Credit_amount': 5000},
    {'Age': 45, 'Duration': 15, 'Credit_amount': 2500},
    # Add more data as needed
]

# Specify the file name
csv_file = 'german_credit_data.csv'

# Write data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Age', 'Duration', 'Credit_amount'])
    writer.writeheader()
    writer.writerows(data)

print(f"CSV file '{csv_file}' created successfully.")
