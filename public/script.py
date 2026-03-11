import csv
import copy

FILE_PATH = "nsdb.txt"

# Varibles declarations
content = []
columns = []
data_template = {}
cleaned_data = []
detected_problem_data = []

# Read TXT File
with open(FILE_PATH, 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        content.append(row)

# Isolate columns
columns = content[0]
del content[0]

# Create columns/keys in the template
for column in columns:
    data_template[column] = ''

# Treat row to make fit in the template and in the right list
for row in content:
    problem_detected = False
    number_of_values = len(row)
    
    # Basic verification of current row
    if number_of_values != len(columns):
        problem_detected = True

    # Mapping data
    template = copy.copy(data_template)
    for index, value in enumerate(row):
        # Get name column with index value of the row
        template[columns[index]] = value

    # Dicriminate data
    if problem_detected:
        detected_problem_data.append(template)
    else:
        cleaned_data.append(template)

# Display results
print(f"===== CLEAR DATA =====")
for data in cleaned_data:
    print(data)

print(f"===== PROBLEM DATA =====")
for data in detected_problem_data:
    print(data)
