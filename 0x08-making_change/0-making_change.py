#!/usr/bin/python3
"""
Module to determine the minimum number of coins needed to meet a total amount.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations
        total (int): Target total amount

    Returns:
        int: Fewest number of coins needed to meet total, or -1 if impossible
    """
    # Handle base cases
    if total <= 0:
        return 0

    # Initialize DP table with max value (total + 1)
    # This ensures non-possible totals remain max value
    dp = [float('inf')] * (total + 1)

    # 0 total requires 0 coins
    dp[0] = 0

    # Compute minimum coins for each amount from 1 to total
    for amount in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= amount:
                # Update minimum coins needed
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return result, use -1 if total can't be met
    return dp[total] if dp[total] != float('inf') else -1
