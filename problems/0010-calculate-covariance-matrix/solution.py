def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # Your code here
    means = []
    features, obs = len(vectors), len(vectors[0])
    for i in range(features):
        sum = 0
        for j in range((obs)):
            sum += vectors[i][j]
        mean = sum/obs
        means.append(mean)

    ans = [[0 for _ in range(features)] for _ in range(features)]

    for i in range(features):
        for j in range(features):
            sum = 0
            for k in range(obs):
                sum += (vectors[i][k] - means[i])*(vectors[j][k] - means[j])
            ans[i][j] = sum/(obs - 1)

    return ans