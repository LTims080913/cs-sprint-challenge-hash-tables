def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    box = {}
    for x in range(len(weights)):
        box[weights[x]] = x
    for x in range(len(weights)):
        package = limit-weights[x]
        if package in box:
            return (max(x, box[package]), min(x, box[package]))
    return None