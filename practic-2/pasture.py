def pasture_area(wire, w):
    if ((wire - (2*w))/2) == 0:
        return(0.0)
    else:
        a = ((wire/3)*w)-((2/3)*(w**2))
        return(a)
def best_pasture(wire):
    a = -2/3
    b = wire/3
    c= 0
    w = -b/(2*a)
    l = (wire - (2*w))/3
    area = w*l
    return(w,l,area)


# pasture_area(100, 25)
# pasture_area(100, 10)
# pasture_area(100, 50)
# print("")
# best_pasture(100)         # (25.0, 16.666..., 416.666...)
# best_pasture(60)          # (15.0, 10.0, 150.0)
# best_pasture(12)          # (3.0, 2.0, 6.0)
