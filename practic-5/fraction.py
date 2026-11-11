def reduce_fraction(fraction):
    numerator, denominator = fraction

    a, b = numerator, denominator
    while b:
        a, b = b, a % b

    return numerator // a, denominator // a


if __name__ == "__main__":
    print(reduce_fraction((45, 120)))   # (3, 8)
    print(reduce_fraction((10, 5)))     # (2, 1)
    print(reduce_fraction((7, 3)))      # (7, 3)
