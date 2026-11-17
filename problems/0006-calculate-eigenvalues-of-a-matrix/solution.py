import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    # eigenvalues, _ = np.linalg.eig(matrix)
    # eigenvalues = np.sort(eigenvalues)[::-1]
    # return eigenvalues.tolist()

    ## OR

    trace = matrix[0][0] + matrix[1][1]
    det = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
    a = (trace + (trace**2 - 4*det)**0.5)/2
    b = (trace - (trace**2 - 4*det)**0.5)/2
    return [a, b]