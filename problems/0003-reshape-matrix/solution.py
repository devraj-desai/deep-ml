import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    if not a or not a[0]:
        return []
    try:
        arr = np.array(a).flatten().tolist()        
        new_rows, new_cols = new_shape
        if new_cols * new_rows != len(arr):
            return []
        reshaped_matrix = [
            [arr[i*new_cols + j] for j in range(new_cols)] 
            for i in range(new_rows)
        ]
        return reshaped_matrix
    except (ValueError, IndexError):
        return []


    ## OR


    if not a or not a[0]:
        return []
        
    new_row, new_col = new_shape

    if len(np.array(a).flatten().tolist()) != new_col * new_row:
        return []

    return np.array(a).reshape(new_shape).tolist()