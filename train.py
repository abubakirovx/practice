def getMaxIndex(arr):
    max = float("-inf")
    indexMax = 0
    for num in arr:
        if num > max:
            max = num
            indexMax = arr.index(max)
    return indexMax


result = getMaxIndex([12, 333, 32, 7, 5, 45, 2, 6])
print(result)