from collections import deque

def solution(A,K):
    deque_element = deque(A)
    deque_element.rotate(K)
    return list(deque_element)





print(solution([1, 2, 3, 4], 2))