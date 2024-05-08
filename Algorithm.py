matrix = [[], []]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            matrix[i][j].append(0)
        elif i == len(matrix) - 1:
            matrix[i][j].append(1)
        else:
            matrix[i][i+1].append(1)
            matrix[i][i-1].append(1)

print()
