def factorial(n):
    res = 1
    if n == 0:
        return(1)
    elif n < 0:
        return(None)
    else:
        for i in range(1,n+1):
            res *= i
        return res

def arrangements(n, k):
    if k > n or k < 0 or n < 0:
        return(0)
    else:
        return(factorial(n)//(factorial(n - k)))


def combinations(n, k):
    if k > n or k < 0 or n < 0:
        return(0)
    else:
        return(factorial(n)//(factorial(k)*factorial(n-k)))


# print(factorial(0))         # 1
# print(factorial(5))          # 120
# print(factorial(-1))         # None
# print("")
# print(arrangements(13, 6))   # 1235520
# print(arrangements(4, 2))    # 12
# print(arrangements(5, 5))    # 120
# print(arrangements(3, 5))    # 0
# print("")
# print(combinations(13, 6))   # 1716
# print(combinations(4, 2))    # 6
# print(combinations(64, 8))   # 4426165368
# print(combinations(5, 0))    # 1
