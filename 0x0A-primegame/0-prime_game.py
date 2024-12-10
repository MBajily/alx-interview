#!/usr/bin/python3
"""
Prime Game implementation where Maria and Ben play optimally.
"""


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check for primality

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def get_primes(n):
    """
    Get a list of all prime numbers up to n.

    Args:
        n (int): Maximum number to check for primes

    Returns:
        list: List of prime numbers
    """
    return [num for num in range(2, n + 1) if is_prime(num)]


def isWinner(x, nums):
    """
    Determine the winner of the prime game across multiple rounds.

    Args:
        x (int): Number of rounds
        nums (list): List of maximum numbers for each round

    Returns:
        str: Name of the player with most wins, or None if no clear winner
    """
    if not nums or x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Edge case: if n is 1, Ben wins immediately
        if n == 1:
            ben_wins += 1
            continue

        primes = get_primes(n)

        # If no primes, Ben wins
        if not primes:
            ben_wins += 1
            continue

        # Simulate game with optimal play
        game_state = [True] * (n + 1)  # Track available numbers
        current_player = 0  # 0 for Maria, 1 for Ben

        while True:
            # Find the next available prime
            prime_found = False
            for prime in primes:
                if prime <= n and game_state[prime]:
                    # Remove prime and its multiples
                    for multiple in range(prime, n + 1, prime):
                        game_state[multiple] = False
                    prime_found = True
                    break

            # If no prime available, current player loses
            if not prime_found:
                if current_player == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            # Switch players
            current_player = 1 - current_player

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
