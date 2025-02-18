def linear_search(nums: list, target: int) -> int:
    for idx in range(len(nums)):
        if nums[idx] == target:
            return idx
    return -1


nums = [0, 1, 2, 3, 4]
target = 2
print(linear_search(nums, target))
