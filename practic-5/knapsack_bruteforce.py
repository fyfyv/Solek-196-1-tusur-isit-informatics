def knapsack_bruteforce(items, capacity):
    best = 0

    def search(index, remaining, value):
        nonlocal best

        if value > best:
            best = value

        if index == len(items):
            return

        search(index + 1, remaining, value)

        weight, cost = items[index]
        if weight <= remaining:
            search(index + 1, remaining - weight, value + cost)

    search(0, capacity, 0)
    return best


if __name__ == "__main__":
    items = [(2, 10), (3, 15), (5, 30)]
    print(knapsack_bruteforce(items, 5))   # 30

    items = [(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)]
    print(knapsack_bruteforce(items, 7))   # 60
