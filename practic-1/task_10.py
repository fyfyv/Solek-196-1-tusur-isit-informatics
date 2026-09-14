def index_of_min(values):
    if len(values) == 0: return -1
    else: return values.index(min(values))
if __name__ == "__main__":
    index_of_min([10, -3, -5, 2, 5])   # 2
    index_of_min([1, 2, 3])            # 0
    index_of_min([4, 1, 1, 9])         # 1
    index_of_min([])                   # -1