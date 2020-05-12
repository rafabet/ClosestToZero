from functools import reduce

def closestToZero(arr = None):
    if not arr:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return reduce(lambda x, y: getSign(x, y), arr)


def getSign(x, y):

    if abs(y) > abs(x):
        return x
    elif abs(y) == abs(x):
        if y >= 0:
            return y
        else:
            return x
    else:
        return y

if __name__ == "__main__":
    arr = []

