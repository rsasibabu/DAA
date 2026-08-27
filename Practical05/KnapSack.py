n = int(input("Enter number of items: "))

weight = []
value = []

for i in range(n):
    weight.append(int(input(f"Enter weight of item {i+1}: ")))
    value.append(int(input(f"Enter value of item {i+1}: ")))

capacity = int(input("Enter knapsack capacity: "))

dp = [[0] * (capacity + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        if weight[i-1] <= w:
            dp[i][w] = max(
                value[i-1] + dp[i-1][w - weight[i-1]],
                dp[i-1][w]
            )
        else:
            dp[i][w] = dp[i-1][w]

print("Maximum value =", dp[n][capacity])
