def insertion_sort():
    array = [8, 4, 5, 1, 3, 6]
    for j in range(1, len(array)):
        i = j - 1
        key = array[j]
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key
    print(array)
    return 0


insertion_sort()
