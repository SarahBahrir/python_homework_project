#1 the aswer in the word file

#2
def quick_kth(arr, left, right, k, key=lambda x: x):
    if left <= right:
        pivot = arr[right]
        pivot_key = key(pivot)

        i = left
        for j in range(left, right):
            if key(arr[j]) <= pivot_key:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[right] = arr[right], arr[i]

        if i == k:
            return arr[i]
        elif k < i:
            return quick_kth(arr, left, i - 1, k, key)
        else:
            return quick_kth(arr, i + 1, right, k, key)


#3

#4
class Tree:
    def __init__(self, key=lambda x: x):
        self.root = None
        self.key = key

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(tree, value):
    if tree.root is None:
        tree.root = Node(value)
        return

    curr = tree.root
    while True:
        if tree.key(value) < tree.key(curr.value):
            if curr.left is None:
                curr.left = Node(value)
                return
            curr = curr.left
        else:
            if curr.right is None:
                curr.right = Node(value)
                return
            curr = curr.right


