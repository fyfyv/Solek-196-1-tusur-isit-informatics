def compare(m, n):
    if (m == n): return "The numbers are equal"
    if (m > n): return "Number m > n"
    if (m < n): return "Number m < n"
if __name__ == "__main__":
    compare(5, 3)   # 'Number m > n'
    compare(3, 5)   # 'Number m < n'
    compare(4, 4)   # 'The numbers are equal'