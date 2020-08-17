def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # inter_points = {}
    # inter_points = set(arrays[0]).intersection(*arrays)

    # return list(inter_points)

    # aaa = arrays(reduce(set.intersection, [set(item) for item in arrays]))

    arr = []
    map = {}
    for val in arrays:
        for oth in val:
            if map.get(oth) == None:
                map[oth] = 1
            else:
                map[oth] = map[oth] + 1

    for key in map:
        if map[key] >= len(arrays):
            arr.append(key)
    return arr

    # map = {}
    # arr = set()

    # for i in range(len(arrays)):
    #     for j in range(len(arrays[0])):
    #         if(map.get(arrays[i][j]) == None):
    #             map[arrays[i][j]] = 1
    #     else:
    #         map[arrays[i][j]] = map[arrays[i][j]]+1

    # for key in map:
    #     if(map[key] >= len(arrays[0])-1):
    #         arr.add(map[key])
    # return list(arr)


print(intersection([
    [1, 2, 3],
    [1, 4, 5],
    [1, 6, 7]
]))

# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
