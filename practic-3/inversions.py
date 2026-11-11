def count_inversions(arr):
    def merge_sort(a):
        if len(a) <= 1:
            return a, 0

        mid = len(a) // 2
        left, left_inv = merge_sort(a[:mid])
        right, right_inv = merge_sort(a[mid:])

        merged = []
        i = j = 0
        inversions = left_inv + right_inv

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                # все оставшиеся элементы left больше right[j]
                inversions += len(left) - i

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions

    return merge_sort(list(arr))[1]

if __name__ == "__main__":
    print(count_inversions([1, 2, 3]))       # 0
    print(count_inversions([3, 2, 1]))       # 3
    print(count_inversions([2, 4, 1, 3, 5])) # 3
    print(count_inversions([5, 4, 3, 2, 1])) # 10
