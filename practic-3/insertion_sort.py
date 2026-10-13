def insertion_sort(arr):
    arrr = list(arr)
    for i in range(1,len(arrr)):
        j = i
        while j > 0 and arrr[j-1] > arrr[j]:
            temp =  arrr[j]
            arrr[j] = arrr[j-1]
            arrr[j-1] = temp
            j = j-1
    return arrr

print(insertion_sort([4, 2, 7, 1, 3, 5]))   # [1, 2, 3, 4, 5, 7]
