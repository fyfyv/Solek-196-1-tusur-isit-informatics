def guests_by_seat(seats):
    result = [0] * len(seats)
    j = 1
    for i in seats:
        result[i-1] = j
        j +=1
    return result
if __name__ == "__main__":    
    guests_by_seat([1, 2, 3, 5, 4])
    guests_by_seat([11, 6, 8, 2, 10, 9, 4, 7, 3, 1, 5])

# def guests_by_seat(seats):
#     y = []
#     for i in range(1,len(seats)+1):
#         y.append(seats.index(i)+1)
#     print(y)
# guests_by_seat([1, 2, 3, 5, 4])
# # [1, 2, 3, 5, 4]
# guests_by_seat([11, 6, 8, 2, 10, 9, 4, 7, 3, 1, 5])
# # [10, 4, 9, 7, 11, 2, 8, 3, 6, 5, 1]