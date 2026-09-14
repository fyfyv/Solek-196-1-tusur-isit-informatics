def circle_diameter(radius):
    return 2*radius
def sum_range(start, end):
    res = 0
    for i in range(start,end+1):
        res += i
    return res
if __name__ == "__main__":
    circle_diameter(5)        # 10
    sum_range(100, 500)       # 120300
    sum_range(1, 10)          # 55
    sum_range(500, 500)       # 500