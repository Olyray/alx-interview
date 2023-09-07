#!/usr/bin/python3
"""The prime game module"""


def is_prime(num):
    """Check for prime number"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def count_primes_up_to_n(n):
    """Count a number"""
    return sum(1 for i in range(2, n + 1) if is_prime(i))


def isWinner(x, nums):
    """Check for the winner"""
    if x < 1 or not nums:
        return None

    maria_wins, ben_wins = 0, 0

    max_num = max(nums)
    primes = [is_prime(i) for i in range(1, max_num + 1)]

    for n in nums:
        primes_count = count_primes_up_to_n(n)
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
