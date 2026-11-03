
def fractional_knapsack(values, weights, capacity):
    items = []

    for i in range(len(values)):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i], i))

    items.sort(reverse=True)

    total_profit = 0.0
    fractions = [0.0] * len(values)

    for ratio, value, weight, index in items:

        if capacity <= 0:
            break

        if weight <= capacity:
            fractions[index] = 1.0
            total_profit += value
            capacity -= weight

        else:
            fractions[index] = capacity / weight
            total_profit += value * fractions[index]
            capacity = 0

    return total_profit, fractions


n = int(input("Enter number of items: "))

values = list(map(int, input("Enter item values: ").split()))

weights = list(map(int, input("Enter item weights: ").split()))

capacity = int(input("Enter knapsack capacity: "))


if n <= 0 or len(values) != n or len(weights) != n:
    print("Invalid number of items or input lengths.")

elif any(w <= 0 for w in weights) or capacity < 0:
    print("Weights must be positive and capacity non-negative.")

else:
    profit, fractions = fractional_knapsack(
        values, weights, capacity
    )

    print("Maximum profit:", profit)
    print("Fractions of items selected:", fractions)
