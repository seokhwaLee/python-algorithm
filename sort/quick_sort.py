def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    print(f"pivot: {pivot}, left : {left}, middle : {middle}, right : {right}")
    return quick_sort(left) + middle + quick_sort(right)


# 테스트
nums = [10, 80, 30, 90, 40, 50, 70]
print(quick_sort(nums))
# pivot: 90, left : [10, 80, 30, 40, 50, 70], middle : [90], right : []
# pivot: 40, left : [10, 30], middle : [40], right : [80, 50, 70]
# pivot: 30, left : [10], middle : [30], right : []
# pivot: 50, left : [], middle : [50], right : [80, 70]
# pivot: 70, left : [], middle : [70], right : [80]
# [10, 30, 40, 50, 70, 80, 90]
