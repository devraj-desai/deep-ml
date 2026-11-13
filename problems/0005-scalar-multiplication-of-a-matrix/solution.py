import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    return (scalar*np.array(matrix)).tolist()

    ##OR

    return [[matrix[i][j]*scalar for j in range(len(matrix[0]))]
             for i in range(len(matrix))]
    pass