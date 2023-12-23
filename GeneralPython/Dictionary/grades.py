def calculate_average(subject_to_exclude):
    # The given grades dictionary
    grades = {'Biology': 80, 'Physics': 88, 'Chemistry': 98, 'Math': 89, 'English': 79,
              'Music': 67, 'History': 68, 'Art': 53, 'Economics': 95, 'Psychology': 88}

    try:
        # Check if the subject is in the dictionary
        if subject_to_exclude in grades:
            # Exclude the specified subject and calculate the average
            excluded_grades = [grade for subject, grade in grades.items() if subject != subject_to_exclude]
            average = sum(excluded_grades) / len(excluded_grades)

            # Print the average to two decimal places
            print(f"{average:.2f}")
        else:
            print("Subject not found in the grades dictionary.")
    except ZeroDivisionError:
        print("Cannot calculate average with no subjects.")

# Example usage:
user_input = input("Enter a subject to exclude: ")
calculate_average(user_input)
