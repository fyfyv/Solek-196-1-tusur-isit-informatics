def count_inversions(arr):
    cnt = 0
    for i in range(1,len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            temp =  arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j = j-1
            cnt += 1
    return cnt

print(count_inversions([1, 2, 3]))      # 0
print(count_inversions([3, 2, 1]))      # 3
print(count_inversions([2, 4, 1, 3, 5])) # 3
print(count_inversions([5, 4, 3, 2, 1])) # 10
