def quick_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    opp = arr[len(arr) // 2]
    m1 = []
    m2 = []
    mid = []
    for i in arr:
        if i < opp: m1.append(i)
        if i > opp: m2.append(i)
        if i == opp: mid.append(i)
    m1 = quick_sort(m1)
    m2 = quick_sort(m2)
    return m1 + mid + m2

# quick_sort([4, 2, 7, 1, 3, 5])   # [1, 2, 3, 4, 5, 7]
# quick_sort([7, 3, 3, 4, 1])      # [1, 3, 3, 4, 7]
# quick_sort([])                   # []
