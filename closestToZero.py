

def closestToZero(arr = None):
    if not arr:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        index = int(len(arr)/2)
        resFirst = closestToZero(arr[:index])
        resSecond = closestToZero(arr[index:])
        abs_res = min(abs(resFirst), abs(resSecond))
        if abs_res == abs(resFirst) and abs_res != abs(resSecond):
            return computeGoodSign(resFirst, abs_res)
        elif abs_res == abs(resSecond) and abs_res != abs(resFirst):
            return computeGoodSign(resSecond, abs_res)
        else:
            return abs_res

def computeGoodSign(num, abs_num):
    if num < 0:
        return -1 * abs_num
    else:
        return abs_num


if __name__ == "__main__":
    arr = []

