# Solution:

def earthquake_anomaly(readings):
    n = len(readings)
    # Edge case: empty list
    if n == 0:
        return []
    sorted_readings = sorted(readings)
    if n % 2 == 1:
        median = sorted_readings[n // 2]
    else:
        median = (sorted_readings[n // 2 - 1] + sorted_readings[n // 2]) / 2
    threshold = 1.5 * median
    result = []
    for i in range(n):
        if readings[i] > threshold:
            result.append(i)
    return result
