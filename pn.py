def perfect_number (n):
    sum_divisors = 0

    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i

    return sum_divisors == n