import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for _ in range(rows):
    row = input(f"Enter row {_ + 1} (comma-separated values): ").split(',')
    matrix.extend(int(x.strip()) for x in row)

print(f"Matrix: \n{np.array(matrix).reshape(rows, cols)}")

values = list(map(int, input("Enter row as comma-separated values: ").split(',')))
matrix1 = np.array(values).reshape(rows, cols)
print(f"Matrix: \n{matrix1}")



#rotate clockwise
rotated = np.rot90(matrix1, k=-1)

for row in rotated:
    print(row)
