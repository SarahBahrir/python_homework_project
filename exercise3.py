#2
#הערך המוחזר מהפונקציה זה לא המקום המדויק של הפיבוט
# ולכן צריך לבדוק גם את המיקום הזה ולכן p1 נכנס איתו גם בפונקציה
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi)         # תיקון! לא pi-1
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    return low

#3

#a
def parent(i):
    return (i - 1) // 2

#b
def left(i):
    return 2 * i + 1

#c
def right(i):
    return 2 * i + 2


#4
def is_max_heap(arr, i=0, key=lambda x: x):
    n = len(arr)

    for child in range(i + 1, n):
        parent_idx =parent(child)
        if key(arr[parent_idx]) < key(arr[child]):
            return False
    return True

#5

def max_heapify(arr, i, heap_size, key=lambda x: x):
    idx_left = left(i)
    idx_right = right(i)

    # נניח שהאיבר הגדול ביותר נמצא ב-i
    largest = i

    # אם הילד השמאלי קיים והוא גדול מהשורש
    if idx_left < heap_size and key(arr[idx_left]) > key(arr[largest]):
        largest = idx_left

    # אם הילד הימני קיים והוא גדול מהגדול ביותר שמצאנו עד עכשיו
    if idx_right < heap_size and key(arr[idx_right]) > key(arr[largest]):
        largest = idx_right

    # אם אחד הילדים גדול מהשורש — מחליפים ועושים heapify רקורסיבי
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size, key)







