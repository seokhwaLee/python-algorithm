def bubble_sort(nums: list) -> list:
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):  # 마지막 1개는 이미 정렬됨
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # swap
            print(nums)
    return nums


print("버블정렬")
nums = [5, 3, 8, 2, 1]
print("nums:", nums)
bubble_sort(nums)
# [5, 3, 8, 2, 1]
# [3, 5, 8, 2, 1]
# [3, 5, 8, 2, 1]
# [3, 5, 2, 8, 1]
# [3, 5, 2, 1, 8]
# [3, 5, 2, 1, 8]
# [3, 2, 5, 1, 8]
# [3, 2, 1, 5, 8]
# [2, 3, 1, 5, 8]
# [2, 1, 3, 5, 8]
# [1, 2, 3, 5, 8]


def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # 교환이 발생했는지 확인
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  # 두 개의 원소 비교 후 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # 교환이 발생했음을 표시
        if not swapped:  # 교환이 없었다면, 이미 정렬된 상태이므로 종료
            break
    return arr


print("최적화 버블정렬")
nums = [2, 3, 4, 5, 8]  # 이미 정렬된 배열
print("nums:", nums)
print(optimized_bubble_sort(nums))  # 출력: [2, 3, 4, 5, 8]
