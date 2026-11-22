def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    if not samples:
        return []

    total = len(samples)
    freq = {}
    for x in samples:
        freq[x] = freq.get(x, 0) + 1

    return [(value, freq[value] / total) for value in sorted(freq)]
    pass