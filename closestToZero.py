from functools import reduce

def closestToZero(arr = None):
    if not arr:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return reduce(lambda x, y: x if abs(y) > abs(x) else y, arr)


if __name__ == "__main__":
    arr = []

