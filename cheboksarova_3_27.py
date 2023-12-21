"""
merge sorting

method splits the input array into two halves,
recursively sorts each half,
and then merges them into one sorted array
"""
import sys


def merge_two_arrays(list_1, list_2):
    """
    returns a sorted array obtained by merging two already sorted arrays

    Args:
        list_1 (list) = first sorted array
        list_2 (list) = second sorted array

    Returns:
        list: sorted array obtained by merging list_1 and list_2

    Raises:
        None

    Examples:
        merge_two_arrays([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    res = []
    while len(list_1) != 0 and len(list_2) != 0:
        res.append(min(list_1[0], list_2[0]))
        if list_1[0] <= list_2[0]:
            list_1.pop(0)
        else:
            list_2.pop(0)
    if len(list_1) != 0:
        res.extend(list_1)
    else:
        res.extend(list_2)
    return res


def merge_sort(array):
    """sorts the input array in ascending order using merge method"""
    if len(array) == 1:
        return array
    left = merge_sort(array[:(len(array)//2)])
    right = merge_sort(array[(len(array)//2):])
    return merge_two_arrays(left, right)


def main():
    """main function"""
    menu = 'what do you wanna do? enter: \n' \
           '1 - set new array \n' \
           '2 - finish'
    request = '1'
    while request == '1':
        print(menu)
        request = input()
        if request == '1':
            print('enter a sequence of numbers separated by spaces')
            try:
                my_array = [float(el) for el in input().split()]
                res_array = merge_sort(my_array)
                for el in res_array:
                    if el.is_integer():
                        res_array[res_array.index(el)] = int(el)
                print(*res_array)
            except ValueError:
                print('input data is incorrect')
        elif request == '2':
            sys.exit()
        else:
            print('carefully read possible operations')
            request = '1'


if __name__ == '__main__':
    main()
