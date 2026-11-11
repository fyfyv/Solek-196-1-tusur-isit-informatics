def greedy_knapsack(items, capacity):
    remaining = capacity
    total = 0

    for weight, value in sorted(items, key=lambda item: item[1], reverse=True):
        if weight <= remaining:
            remaining -= weight
            total += value

    return total


if __name__ == "__main__":
    print(greedy_knapsack([(2, 10), (3, 15), (5, 30)], 5))       # 30
    print(greedy_knapsack([(6, 10), (5, 9), (5, 8)], 10))        # 10
