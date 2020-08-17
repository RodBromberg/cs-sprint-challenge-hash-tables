def has_negatives(a):
    """
    YOUR CODE HERE
    """
    map = {}

    result = []

    for i in range(len(a)):
        if(map.get(a[i]) == None):
            map[a[i]] = 1
        else:
            map[a[i]] = map[a[i]]+1

    for num in a:
        if(map.get(num*-1) == map.get(num) and num > 0):
            result.append(num)

    return result


# print('gg')
print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
