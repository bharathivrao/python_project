def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes_up_to(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def next_prime(n):
    for num in range(n + 1, 2 * n):
        if is_prime(num):
            return num
    return None

def main():
    n = int(input("Enter a number: "))
    primes = get_primes_up_to(n)
    next_prime_num = next_prime(n)
    print(f"Primes up to {n}: {primes}")
    print(f"Next prime after {n}: {next_prime_num}")

if __name__ == "__main__":
    main()