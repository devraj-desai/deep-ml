def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    if mode == 'column':
        for i in range(len(matrix[0])):
            sum = 0
            for j in range(len(matrix)):
                sum += matrix[j][i]
            means.append(sum/len(matrix))   
    else:
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(matrix[0])):
                sum += matrix[i][j]
            means.append(sum/len(matrix[0]))
    return means