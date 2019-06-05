
def solution(A):
    array_length = len(A)
    sorted_array = sorted(A)
    last_element = sorted_array[-1]

    if array_length == last_element:
        for i in range(array_length-1):
            if sorted_array[i + 1] - sorted_array[i] <= 0:
                return 0
        return 1
    return 0

print(solution([9, 5, 7, 3, 2, 7, 3, 1, 10, 8]))