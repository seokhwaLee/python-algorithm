def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
        print(nums)
    return nums


# 테스트
nums = [9, 5, 1, 4, 3]
print(insertion_sort(nums))  # 출력: [1, 3, 4, 5, 9]
