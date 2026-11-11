def knapsack_dp(items, capacity):
    dp = [0] * (capacity + 1)

    for weight, value in items:
        for current in range(capacity, weight - 1, -1):
            candidate = dp[current - weight] + value
            if candidate > dp[current]:
                dp[current] = candidate

    return dp[capacity]


if __name__ == "__main__":
    items = [(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)]
    print(knapsack_dp(items, 7))   # 60

    items = [(6, 10), (5, 9), (5, 8)]
    print(knapsack_dp(items, 10))  # 17
