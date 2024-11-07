#from random import randint


def my_sort(arr):
    """
    Данная функция использует некоторые идеи сортировки Timsort, благодаря этому, при наличии в исходном массиве упорядоченных
    подпоследовательностей (что нередко бывает в настоящих массивах), достигается высокая скорость сортировки.
    """
    run = 32

    def merge(first_l, first_r, second_l, second_r):
        res = []
        while (first_l <= first_r) and (second_l <= second_r):
            if arr[first_l] <= arr[second_l]:
                res.append(arr[first_l])
                first_l += 1
            else:  # arr[first_l] > arr[second_l]
                res.append(arr[second_l])
                second_l += 1

        res.extend(arr[first_l:first_r + 1])
        res.extend(arr[second_l:second_r + 1])

        return res

    def insertion_sort(l, r):
        def is_le(a, b):
            return a <= b

        def is_g(a, b):
            return a > b

        if ((size := r - l) == 0) or (size == 1):
            return

        cmp = is_le if arr[l] <= arr[l + 1] else is_g

        for i in range(l + 2, r + 1):
            while i > l and (not cmp(arr[i - 1], arr[i])):
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                i -= 1

        if arr[l] > arr[r]:
            arr[l:r + 1] = arr[r:None if l == 0 else l - 1:-1]

    subsorted_arrays_r_bounds = []
    l = 0
    while l < len(arr):
        r = min(l + run, len(arr)) - 1
        insertion_sort(l, r)

        r += 1
        while (r < len(arr) - 1) and (arr[r] >= arr[r - 1]):
            r += 1
        r -= 1

        subsorted_arrays_r_bounds.append(r)
        l = r + 1

    if len(subsorted_arrays_r_bounds) < 2:
        return

    first_l = 0
    first_r = subsorted_arrays_r_bounds[0]

    for second_r_index in range(1, len(subsorted_arrays_r_bounds)):
        second_l = subsorted_arrays_r_bounds[second_r_index - 1] + 1
        second_r = subsorted_arrays_r_bounds[second_r_index]

        arr[first_l:second_r + 1] = merge(first_l, first_r, second_l, second_r)

        first_r = second_r


#a = [randint(0, 100) for _ in range(100)]
#print(a)
#my_sort(a)
#print(a)
