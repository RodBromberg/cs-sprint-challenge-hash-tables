def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    # [1,3,5,7] 10
    # map{9:0}
    # map{7:1}
    # map{5:2}
    # map(3:3)

    if(len(weights) == 1):
        return None

    map = {}
    arr = []
    for i in range(len(weights)):

        if(map.get(limit-weights[i]) == None):
            map[weights[i]] = i
        else:
            # arr[0] = map.get(complement)
            # arr[1] = i
            arr.append(i)
            arr.append(map.get(limit-weights[i]))

    return arr


weights_3 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_3, 5, 21))
