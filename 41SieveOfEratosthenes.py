def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)  # Create a list initialized to True
    p = 2  # Start with the first prime number

    while p * p <= n:
        if primes[p]:  # If p is a prime
            for i in range(p * p, n + 1, p):  # Mark all multiples of p as False
                primes[i] = False
        p += 1

    # Collect all prime numbers
    prime_numbers = [num for num in range(2, n + 1) if primes[num]]
    return prime_numbers

# Taking user input
num = int(input("Enter a number: "))
print(f"Prime numbers up to {num}:", sieve_of_eratosthenes(num))
