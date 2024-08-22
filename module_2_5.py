def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
             matrix[i].append(value)
    return matrix
result1 = get_matrix(3, 2,9)
result2 = get_matrix(5, 4,3)
result3 = get_matrix(4, 3,7)
print(result1)
print(result2)
print(result3)






