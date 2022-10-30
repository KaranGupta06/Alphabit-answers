l, b = map(int, input().split())
matrix = []

for _ in range(b):
    matrix.append(list(map(int, input().split())))

for i in range(b):
    for j in range(l):
        if matrix[i][j] == 1:
            matrix[i][j] = 'm'

for i in range(l):
    for j in range(b):
        if matrix[j][i] == 'm':
            for g in range(9):
                x_d, y_d = g//3-1, g%3-1
                if j + y_d in range(b) and i + x_d in range(l) and matrix[j+y_d][i+x_d] != 'm':
                    matrix[j+y_d][i+x_d] += 1

largest = (0, 0)
for i, j in enumerate(matrix):
    count = 0
    for k in j:

        if k != 'm':
            count += k
        
        if count > largest[1]:
            largest = (i+1, count)

print(*largest)
