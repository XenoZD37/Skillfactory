def arr_sort(arr):
    if (len(arr) == 1):
            return arr
    else:
        middle = len(arr) // 2
        arr_left = arr_sort(arr[:middle])
        arr_right = arr_sort(arr[middle:])

        return merge(arr_left, arr_right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def bin_search(arr, check_num, i_low, i_high):
    if (i_high >= i_low):
        middle = i_low + (i_high - i_low) // 2
    
    if (check_num > arr[middle]):
        if middle + 1 >= len(arr) or check_num <= arr[middle + 1]:
            return middle
    if (check_num <= arr[middle]):
        return bin_search(arr, check_num, i_low, middle)
    else:
        return bin_search(arr, check_num, middle, i_high)

    
num_arr = list(map(int, input("Введите последовательность чисел через пробел:\n").split(' ')))

check_num = int(input("Введите число:\n"))
num_arr = arr_sort(num_arr)
if (check_num <= num_arr[0]):
    print("Заданное число меньше или равно наименьшему элементу в списке")
else: 
    if (check_num > num_arr[-1]):
        print("Заданное число больше чем наибольший элемент в списке")
    else:
        print(bin_search(num_arr, check_num, 0, len(num_arr)))
