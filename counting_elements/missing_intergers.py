

def solution(A):
    sorted_list = sorted(A)

    if len(sorted_list) > 1:
        for i in range(len(sorted_list)-1):

            if i == 0 and sorted_list[i] > 1:
                return 1
            if len(sorted_list) == 2:
                if sorted_list[i] < 0:
                    return 1
            if sorted_list[i + 1] < 0 and sorted_list[i] < 0:
                if sorted_list[i + 1] - sorted_list[i] >= 0:
                    return 1
            elif sorted_list[i + 1] - sorted_list[i] > 1:
                return sorted_list[i] + 1
        else:
            return sorted_list[i + 1] + 1

    else:
        if sorted_list[0] > 1:
            return sorted_list[0] - 1
        elif sorted_list[0] == 1:
            return sorted_list[0] + 1
        return 1


print(solution([-1,-3]))
