
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    a, b = 0, 1
    result = []

    for _ in range(n):
        result.append(a)
        a, b = b, a + b

    return result


n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Non-recursive Fibonacci:")
    print(fibonacci_iterative(n))

    print("Recursive Fibonacci:")
    print([fibonacci_recursive(i) for i in range(n)])

    print("Iterative time complexity: O(n)")
    print("Iterative space complexity: O(n) including output")
    print("Recursive time complexity: O(2^n) approximately")
    print("Recursive space complexity: O(n)")
