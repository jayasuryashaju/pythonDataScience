def fibonacci_series(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

# Number of terms you want in the Fibonacci series
n_terms = 10
fib_sequence = fibonacci_series(n_terms)

print(f"The first {n_terms} terms of the Fibonacci series are:")
print(fib_sequence)
