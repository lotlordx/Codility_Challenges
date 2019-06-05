# def solution(A):
#
#
#     val = True
#     counter = 1
#     try:
#         while val:
#             if A[0] == A[counter]:
#                 del A[0]
#                 del A[counter-1]
#                 counter = 0
#             counter +=1
#     except:
#         return A[0]

def solution(A):
    sorted_array = sorted(A)
    val = True
    counter = 0

    while val:
        try:
            if sorted_array[counter] != sorted_array[counter+1]:
                return sorted_array[counter]
            counter +=2
        except:
            return sorted_array[counter]

print(solution([1, 3, 4, 5, 3, 1, 4, 5, 7, 7, 8,8,19, 10, 11, 10, 11,2,3,2,2,2,3,19,23,40,40]))
