def binary_search(nums, n, lo, hi):
    lo = 0
    hi = len(nums)
    step = 0

    while lo < hi:
        step += 1
        mid = int((lo + hi) / 2)

        if nums[mid] == n:
            print("step: ", step)
            return mid
        elif nums[mid] < n:
            lo = mid + 1
        else:
            hi = mid
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1

    while i < n and arr[i] <= target:
        i *= 2
    if arr[i] == target:
        return i

    return binary_search(arr, target, i // 2, min(i, n - 1))



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
target = 32
result = exponential_search(arr, target)

print("Element found at index: ", result)