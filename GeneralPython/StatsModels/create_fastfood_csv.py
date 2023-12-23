import csv

# Sample data
fast_food_data = [
    {'Name': 'McDonald\'s', 'Type': 'Burger', 'Location': 'Global'},
    {'Name': 'Subway', 'Type': 'Subs', 'Location': 'Global'},
    {'Name': 'Pizza Hut', 'Type': 'Pizza', 'Location': 'Global'},
    {'Name': 'KFC', 'Type': 'Chicken', 'Location': 'Global'},
    # Add more fast-food chains and their details as needed
]

# Specify the file name
csv_file = 'fastfood.csv'

# Write data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Type', 'Location'])
    writer.writeheader()
    writer.writerows(fast_food_data)

print(f"CSV file '{csv_file}' created successfully.")

#RUN THIS PLEASE
#python create_fastfood_csv.py