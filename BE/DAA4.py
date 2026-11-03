
def knapsack(values, weights, capacity):
    n = len(values)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= weights[i - 1]

    selected.reverse()

    return dp[n][capacity], selected


n = int(input("Enter number of items: "))

values = list(map(int, input("Enter item values: ").split()))

weights = list(map(int, input("Enter item weights: ").split()))

capacity = int(input("Enter knapsack capacity: "))


if n <= 0 or len(values) != n or len(weights) != n:
    print("Invalid number of items or input lengths.")

elif any(w <= 0 for w in weights) or capacity < 0:
    print("Weights must be positive and capacity non-negative.")

else:
    maximum, selected = knapsack(values, weights, capacity)

    print("Maximum profit:", maximum)
    print("Selected item numbers:", selected)

    print("Time complexity: O(n * capacity)")
    print("Space complexity: O(n * capacity)")
