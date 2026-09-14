def is_divisor(a, b):
    if (a == 0):        return False
    elif(b % a == 0):   return True
    else:               return False
if __name__ == "__main__":
    is_divisor(3, 12)   # True
    is_divisor(5, 12)   # False
    is_divisor(0, 12)   # False
    is_divisor(7, 0)    # True