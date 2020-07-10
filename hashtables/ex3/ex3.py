def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    int = {}

    for item in sorted(arrays, key=len)[0]:
        int[item] = 1
    for arr in sorted(arrays, key=len)[1:]:
        for item in arr:
            if item in int.keys():
                int[item] += 1
    result = [k for k, v in int.items() if v == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
