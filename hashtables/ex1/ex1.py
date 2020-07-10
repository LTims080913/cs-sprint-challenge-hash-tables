def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    box = {}
    for x in range(len(weights)):
        box[weights[x]] = x
    for x in range(len(weights)):
        dif = limit-weights[x]
        if dif in box:
            return (max(x, box[dif]), min(x, box[dif]))
    return None