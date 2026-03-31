import sys

# Accept input from stdin in a generic format:
# First line: n (number of elements)
# Second line: space-separated numbers (int/float)
# If no input is provided, uses a default sample for quick run.

def parse_input():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return [1, 2, 3]

    if len(lines) == 1:
        parts = lines[0].split()
        if len(parts) > 1:
            return [float(x) for x in parts]
        raise ValueError('Expected space-separated data or 2 lines of input')

    # len(lines) >= 2
    try:
        n = int(lines[0])
    except ValueError as ex:
        raise ValueError('First line must be integer count') from ex

    data = []
    for line in lines[1:]:
        data.extend(float(x) for x in line.split())

    if len(data) < n:
        raise ValueError(f'Expected {n} values but got {len(data)}')
    return data[:n]


def mean_median_std(data):
    data = sorted(data)
    n = len(data)
    mean = sum(data) / n
    median = (data[n // 2] if n % 2 else (data[n // 2 - 1] + data[n // 2]) / 2)
    var = sum((x - mean) ** 2 for x in data) / n
    std = var ** 0.5
    return mean, median, std


def main():
    arr = parse_input()
    mean, median, std = mean_median_std(arr)

    # print results in one line (space-separated) to match example
    print(f'{mean:.6f} {median:.6f} {std:.12f}')


if __name__ == '__main__':
    main()
