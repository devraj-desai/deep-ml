import math

def sigmoid(z: float) -> float:
    #Your code here
    epsilon = math.ulp(1.0)
    result = 1/(1 + math.exp(-z))
    return result