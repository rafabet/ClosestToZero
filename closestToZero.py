from functools import reduce

def closestToZero(arr = None):
    if not arr:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return reduce(lambda x, y: x if abs(y) > abs(x) else y, arr)


def computeGoodSign(num, abs_num):
    if num < 0:
        return -1 * abs_num
    else:
        return abs_num


if __name__ == "__main__":
    arr = []

