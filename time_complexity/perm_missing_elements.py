

def solution(A):
    list_sum = 0
    N = len(A)
    for val in A:
        list_sum += val

    val = (N + 1) * (N + 2) // 2

    return val - list_sum



print(solution([2,3,1,5]))