from typing import List


def bubble_sort(a: List[int]) -> List[int]:
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
    return a


if __name__ == "__main__":
    arr = [1, 5, 8, 6]
    sorted_arr = bubble_sort(arr)
    print(sorted_arr)
