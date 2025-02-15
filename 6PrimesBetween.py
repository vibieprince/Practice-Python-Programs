def print_primes(n):
    primes = [True] * (n + 1)  # Assume all numbers are prime
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for i in range(2, int(n**0.5) + 1):  # Iterate up to √n
        if primes[i]:  # If i is prime
            for j in range(i * i, n + 1, i):  # Mark multiples of i as non-prime
                primes[j] = False

    # Print all prime numbers
    print("Prime numbers between 1 and 100:")
    for i in range(1, n + 1):
        if primes[i]:
            print(i, end=" ")

# Call the function for numbers up to 100
print_primes(100)