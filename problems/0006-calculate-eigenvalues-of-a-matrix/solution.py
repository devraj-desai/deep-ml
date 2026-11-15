import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    eigenvalues, _ = np.linalg.eig(matrix)
    eigenvalues = np.sort(eigenvalues)[::-1]
    return eigenvalues.tolist()