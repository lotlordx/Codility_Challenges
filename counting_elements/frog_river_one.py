def solution_one(X, A):
    array_length = len(A)

    for i in range(array_length):
        if A[i] == X:
            return i
    return -1

def solution(X, A):
    # write your code in Python 2.6
    enum = list(enumerate(A))
    frog, leaves = 0, [False] * (X)
    for minute, leaf in enumerate(A):
        if leaf <= X:
            leaves[leaf - 1] = True
        while leaves[frog]:
            frog += 1
            if frog == X: return minute
    return -1
print(solution(2, [2, 2, 2, 2, 2]))