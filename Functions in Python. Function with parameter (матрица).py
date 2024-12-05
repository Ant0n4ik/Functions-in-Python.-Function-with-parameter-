def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        row.append(i)
        matrix.append(row)
        row.pop()
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
for row in result1:
    print(row)
print()
for row in result2:
    print(row)
print()
for row in result3:
    print(row)
# print(result1)
# print(result2)
# print(result3)