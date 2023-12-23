
# gpa_dict = {'A':4.0, 'A-':3.66, 'B+':3.33, 'B':3.0, 'B-':2.66, 'C+':2.33, 'C':2.0,
# 'C-':1.66, 'D+':1.33, 'D':1.00, 'D-':.66, 'F':0.00}

# ● Create a program that takes four letter grade arguments and prints
# out the corresponding GPA, to two decimals. Your program should work both in
# arguments are upper-case and lower-case.

# ● Your program should print in the form:
# “My GPA is x”
# Where x = GPA calculation

def calculate_gpa(grade1, grade2, grade3, grade4):
    # The given GPA dictionary
    gpa_dict = {'A': 4.0, 'A-': 3.66, 'B+': 3.33, 'B': 3.0, 'B-': 2.66,
                'C+': 2.33, 'C': 2.0, 'C-': 1.66, 'D+': 1.33, 'D': 1.0, 'D-': 0.66, 'F': 0.0}

    try:
        # Convert grades to uppercase for case-insensitive comparison
        grade1, grade2, grade3, grade4 = grade1.upper(), grade2.upper(), grade3.upper(), grade4.upper()

        # Calculate GPA
        total_gpa = gpa_dict.get(grade1, 0) + gpa_dict.get(grade2, 0) + gpa_dict.get(grade3, 0) + gpa_dict.get(grade4, 0)
        average_gpa = total_gpa / 4

        # Print the GPA to two decimal places
        print(f"My GPA is {average_gpa:.2f}")
    except:
        print("An error occurred. Please check your input.")

# Example usage:
grade1 = input("Enter the first letter grade: ")
grade2 = input("Enter the second letter grade: ")
grade3 = input("Enter the third letter grade: ")
grade4 = input("Enter the fourth letter grade: ")

calculate_gpa(grade1, grade2, grade3, grade4)