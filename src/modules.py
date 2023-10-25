# 25.10.2023
def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def iloczyn(a, b):
    return a * b

def iloraz(a, b):
    return a / b

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop(len(arr) // 2)
        left = []
        right = []
        for i in arr:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [pivot] + quick_sort(right)