
def fibonacci_series(n):
    if n < 0:
        return []

    series = []
    first, second = 0, 1

    for _ in range(n):
        series.append(first)
        first, second = second, first + second

    return series
