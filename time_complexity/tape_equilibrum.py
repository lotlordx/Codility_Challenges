
#
def solution_one(A):
    min_val = 0

    for i in range(len(A)-1):
        new_min = abs(sum(A[:i+1]) - sum(A[i+1:]))
        if min_val == 0:
            min_val = new_min
        else:
            if new_min < min_val:
                min_val = new_min
    return min_val

def solution_two(A):
    min_val = 0

    for i in range(len(A)-1):
        first_val = sum(A[:i+1])
        second_val = sum(A[i+1:])
        new_min = abs(sum(A[:i+1]) - sum(A[i+1:]))

        if not min_val == 0 and new_min < min_val:
            min_val = new_min
        elif min_val == 0:
            min_val = new_min
    return min_val

def solution(A):
    array_length = len(A)-1
    array_sum = sum(A)
    next_element = 0
    min_val = None

    for i in range(array_length):
        next_element += A[i]
        new_min = abs(next_element - (array_sum - next_element))

        if min_val is None:
            min_val = new_min
        elif not min_val == 0 and new_min < min_val:
            min_val = new_min

    return min_val

A = [1, 2, 3, 4]
# print(A[1:])
print(solution(A))