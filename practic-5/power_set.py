def power_set(items):
    subsets = [()]

    for item in items:
        subsets += [subset + (item,) for subset in subsets]

    return subsets


if __name__ == "__main__":
    print(power_set([1, 2, 3]))
    # [(), (1,), (2,), (1, 2), (3,), (1, 3), (2, 3), (1, 2, 3)]
