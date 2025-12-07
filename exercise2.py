from itertools import pairwise

#1
def sort_insertion(a, key=lambda x: x[0]):

    for i in range(1, len(a)):
        current = a[i]
        j = i - 1
        while j >= 0 and key(a[j]) > key(current):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = current
    return a

def create_random_tuples(n, k, types=None):

    import random
    import string

    if types is None:
        types = [int] * k  # Default to int if no types provided

    if len(types) != k:
        raise ValueError("Length of types must be equal to k")

    def random_element(t):
        if t == int:
            return random.randint(0, 1000)
        elif t == float:
            return random.uniform(0.0, 1000.0)
        elif t == str:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        else:
            raise ValueError(f"Unsupported type: {t}")

    result = []
    for _ in range(n):
        tuple_elements = tuple(random_element(t) for t in types)
        result.append(tuple_elements)

    return result
# 2
#a

def merge(a, b, key):
    i, j = 0, 0
    result = []

    if not is_sorted(a,key) or not is_sorted(b,key):
        return None

    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # הוספת השאריות אם נשארו
    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1

    return result


def mergesort(arr, key):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid], key)
    right = mergesort(arr[mid:], key)

    return merge(left, right, key)

#b
def is_sorted(a, key):
    for i,j in pairwise(a):
        if key(i) > key(j):
            return False
    return True

#3
#a
def merge_sorted_lists(lists, key):
    result = []

    for lst in lists:
        merged = merge(result, lst, key)
        if merged is None:
            return None
        result = merged

    return result
#b
#O(k^2*n)

#4
#a

def partition_lomuto(a, key):
    pivot = a[-1]
    i = -1
    for j in range(len(a)-1):
        if key(a[j]) <= key(pivot):
            i += 1
            a[i], a[j] = a[j], a[i]
    # העברת pivot למקום הנכון
    a[i+1], a[-1] = a[-1], a[i+1]
    return i+1
#b
def partition_hoare(a, key):
    pivot = a[len(a)//2]
    i = 0
    j = len(a)-1
    while True:
        while key(a[i]) < key(pivot):
            i += 1
        while key(a[j]) > key(pivot):
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
#c
#The pivot’s initial choice is fixed (like the last element for Lomuto or the middle for Hoare),
#but its final position after partitioning isn’t predetermined and depends on how the elements are rearranged.


#d
# Both functions have linear time complexity: O(n)

#5
def dual_pivot_partition(a, key):
    if key(a[0]) > key(a[-1]):
        a[0], a[-1] = a[-1], a[0]

    pivot1 = a[0]
    pivot2 = a[-1]

    lt = 1
    gt = len(a)-2
    i = 1

    while i <= gt:
        if key(a[i]) < key(pivot1):
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif key(a[i]) > key(pivot2):
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1

    a[0], a[lt-1] = a[lt-1], a[0]
    a[-1], a[gt+1] = a[gt+1], a[-1]

    return lt-1, gt+1








if __name__ == "__main__":
    tuples_list = create_random_tuples(5, 3, [int, float, str])
    print("Before sorting:")
    print(tuples_list)

    sorted_by_first = sort_insertion(tuples_list.copy(), key=lambda x: x[0])
    print("\nSorted by first element (int):")
    print(sorted_by_first)

    sorted_by_second = sort_insertion(tuples_list.copy(), key=lambda x: x[1])
    print("\nSorted by second element (float):")
    print(sorted_by_second)

    sorted_by_third = sort_insertion(tuples_list.copy(), key=lambda x: x[2])
    print("\nSorted by third element (str):")
    print(sorted_by_third)


