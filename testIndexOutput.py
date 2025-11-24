
arr = [170, 45, 75, 90, 802, 24, 2, 66]
exp = 1
n = len(arr)
output = [0] * n
count = [0] * 10

# Count occurrences of each digit and put it in the count list
for num in arr:
    index = (num // exp) % 10
    #print(f"Index is {index}")
    count[index] += 1
    #print(f"Count is {count}")

# Convert count[] to prefix sums to get positions
for i in range(1, 10):
    count[i] += count[i - 1]

print(count)
