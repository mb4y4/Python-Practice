import csv

data = [
    {'Name': 'George Washington', 'Height': 189},
    {'Name': 'John Adams', 'Height': 170},
    {'Name': 'Thomas Jefferson', 'Height': 189},
    {'Name': 'James Madison', 'Height': 163},
    {'Name': 'James Monroe', 'Height': 183},
    # Add more presidents and their heights as needed
]

# Specify the file name
csv_file = 'president_heights.csv'

# Write data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Height'])
    writer.writeheader()
    writer.writerows(data)

print(f"CSV file '{csv_file}' created successfully.")

#then run this to create a csv file to use with "presidents.py"