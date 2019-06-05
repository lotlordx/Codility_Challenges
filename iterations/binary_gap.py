

def solution(N):
    """"Find longest sequence of zeros in binary representation of an integer. """
    binary_equivalent = "{:b}".format(N)
    length_array = []
    length = 0

    for i in range(0, len(binary_equivalent)):

        if binary_equivalent[0] != binary_equivalent[i]:
            length += 1
        else:
            if length > 0:
                length_array.append(length)
                length = 0

    real_length_array = max(length_array) if length_array else 0
    # if not length_array:
    #     real_length_array = 0
    # else:
    #     real_length_array = max(length_array)


    return binary_equivalent,length_array,real_length_array

print(solution(647))