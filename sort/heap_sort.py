def heapify(arr, n, i):
    largest = i  # 현재 노드를 가장 큰 값으로 가정
    left = 2 * i + 1  # 왼쪽 자식 인덱스
    right = 2 * i + 2  # 오른쪽 자식 인덱스

    # 왼쪽 자식이 부모보다 크면 largest 갱신
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 largest보다 크면 largest 갱신
    if right < n and arr[right] > arr[largest]:
        largest = right

    # largest가 부모 노드가 아니면 교환 후 재귀 호출
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print(f"heapify: {arr}")
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    print(f"초기 배열: {arr}\n")
    # 최대 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 힙에서 요소 추출 후 정렬
    for i in range(n - 1, 0, -1):
        # 루트(최대값)와 마지막 요소 교환
        arr[0], arr[i] = arr[i], arr[0]
        print(f"교환 후 (루트 <-> arr[{i}]): {arr}")

        # 힙 속성 유지
        heapify(arr, i, 0)
        print(f"힙 복원 후: {arr}\n")
    return arr


nums = [12, 11, 13, 5, 6, 7]
sorted_nums = heap_sort(nums.copy())

# 초기 배열: [12, 11, 13, 5, 6, 7]
# heapify: [13, 11, 12, 5, 6, 7]

# 교환 후 (루트 <-> arr[5]): [7, 11, 12, 5, 6, 13]
# heapify: [12, 11, 7, 5, 6, 13]
# 힙 복원 후: [12, 11, 7, 5, 6, 13]

# 교환 후 (루트 <-> arr[4]): [6, 11, 7, 5, 12, 13]
# heapify: [11, 6, 7, 5, 12, 13]
# 힙 복원 후: [11, 6, 7, 5, 12, 13]

# 교환 후 (루트 <-> arr[3]): [5, 6, 7, 11, 12, 13]
# heapify: [7, 6, 5, 11, 12, 13]
# 힙 복원 후: [7, 6, 5, 11, 12, 13]

# 교환 후 (루트 <-> arr[2]): [5, 6, 7, 11, 12, 13]
# heapify: [6, 5, 7, 11, 12, 13]
# 힙 복원 후: [6, 5, 7, 11, 12, 13]

# 교환 후 (루트 <-> arr[1]): [5, 6, 7, 11, 12, 13]
# 힙 복원 후: [5, 6, 7, 11, 12, 13]
