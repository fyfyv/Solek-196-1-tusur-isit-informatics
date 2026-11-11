def fib(n):
    memo = {0: 0, 1: 1}

    def calculate(k):
        if k not in memo:
            memo[k] = calculate(k - 1) + calculate(k - 2)
        return memo[k]

    return calculate(n)


if __name__ == "__main__":
    print(fib(0))    # 0
    print(fib(1))    # 1
    print(fib(2))    # 1
    print(fib(5))    # 5
    print(fib(10))   # 55
