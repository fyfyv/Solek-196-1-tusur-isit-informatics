def is_balanced(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack


if __name__ == "__main__":
    print(is_balanced("()"))       # True
    print(is_balanced("([])"))     # True
    print(is_balanced("([{}])"))   # True
    print(is_balanced("(]"))       # False
    print(is_balanced("([)]"))     # False
    print(is_balanced("("))        # False
    print(is_balanced(""))         # True
