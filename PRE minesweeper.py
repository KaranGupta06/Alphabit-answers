l, b = map(int, input().split())
matrix = []
count = 0

for _ in range(b):
    matrix.append(list(map(int, input().split())))

for i in range(l):
    for j in range(b):
        if matrix[j][i] == 1:
            for g in range(9):
                x_d, y_d = g//3-1, g%3-1
                if j + y_d in range(b) and i + x_d in range(l) and matrix[j+y_d][i+x_d] == 0:
                    count += 1

print(count)