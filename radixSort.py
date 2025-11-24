def counting_sort(arr, exp):
    """
    A stable counting sort that sorts arr[] according to the digit represented by exp.
    exp = 1 → sort by units
    exp = 10 → sort by tens
    exp = 100 → sort by hundreds, etc.
    """
    n = len(arr)
    output = [0] * n     # output array
    count = [0] * 10     # since digits are 0–9

    # Count occurrences of each digit
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Convert count[] to prefix sums to get positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (iterate backwards for stability)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the result back into arr[]
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Apply counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        print('The maxNum // exp', max_num // exp)
        counting_sort(arr, exp)
        exp *= 10


# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)  # Output: [2, 24, 45, 66, 75, 90, 170, 802]
