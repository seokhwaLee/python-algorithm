def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    print(f"merge : {left}, {right}")
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr


# 테스트
nums = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(nums))
# merge : [27], [43]
# merge : [38], [27, 43]
# merge : [3], [9]
# merge : [82], [10]
# merge : [3, 9], [10, 82]
# merge : [27, 38, 43], [3, 9, 10, 82]
# [3, 9, 10, 27, 38, 43, 82]
