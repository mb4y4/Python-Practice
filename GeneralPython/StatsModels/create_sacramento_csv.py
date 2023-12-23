import csv

# Sample data
data = [
    {'beds': 3, 'sq__ft': 1500, 'price': 300000, 'baths': 2},
    {'beds': 4, 'sq__ft': 2000, 'price': 400000, 'baths': 2.5},
    {'beds': 2, 'sq__ft': 1200, 'price': 250000, 'baths': 1},
    {'beds': 5, 'sq__ft': 2500, 'price': 500000, 'baths': 3},
    {'beds': 3, 'sq__ft': 1800, 'price': 350000, 'baths': 2.5},
    # Add more data as needed
]

# Specify the file name
csv_file = 'sacramento.csv'

# Write data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['beds', 'sq__ft', 'price', 'baths'])
    writer.writeheader()
    writer.writerows(data)

print(f"CSV file '{csv_file}' created successfully.")
