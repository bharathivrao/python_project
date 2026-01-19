file_path = input("Enter the file path: ")

total_sales = 0
record_with_max_sales = None

try:
    with open(file_path, 'r') as file:
        next(file)
        contents = file.readlines();
except FileNotFoundError:
    print(f"File not found: {file_path}")
except IOError:
    print(f"Error reading file: {file_path}")

for record in contents:
    print(record)

category = {}

max_record = []
for record in contents:
    values = record.split(',')
    if values[2] in category:
        category[values[2]] += float(values[3])
    else:
        category[values[2]] = float(values[3])
    if len(max_record) == 0 or float(max_record[3]) < float(values[3]):
        max_record = values

for key in category:
    print(f"Total sales for category {key} is {category[key]}")

print(f"Record with max sale is {max_record[2]} with value of {max_record[3]}")