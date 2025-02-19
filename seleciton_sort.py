def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        print(nums)
    return nums


# 테스트
nums = [64, 25, 12, 22, 11]
print(selection_sort(nums))  # 출력: [11, 12, 22, 25, 64]
