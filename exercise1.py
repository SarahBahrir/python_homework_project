def find_min(a, key=lambda x: x[0]):
    if not a:
        raise ValueError("List is empty")
    minimum= a[0]
    min_value=key(minimum)
    for element in a[1:]:
        current_value=key(element)
        if current_value < min_value:
            minimum=element
            min_value=key(element)
    return minimum
def find_max(a, key=lambda x: x[3]):
    if not a:
        raise ValueError("List is empty")
    maximum= a[0]
    max_value=key(maximum)
    for element in a[1:]:
        current_value=key(element)
        if current_value > max_value:
            maximum=element
            max_value=key(element)
    return maximum


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




if __name__ == "__main__":
    # Example usage
    tuples_list = create_random_tuples(100, 3, [int, float, str])
    for t in tuples_list:
        print(t)
    #שאלה 4
    #a
    print("\nMinimum by first element:")
    print(find_min(tuples_list, key=lambda x: x[0]))

    #b
    min = find_min(tuples_list, key=lambda x: x[3])
    max = find_max(tuples_list, key = lambda x:x[3])

    #c
    # התוכנית תרוץ על כל המערך פעמים ולכן זמן הריצה יהיה O(N)

    #שאלה 5

    tuples_list1 = create_random_tuples(100, 3, [int, float, str])
    tuples_list2 = create_random_tuples(100, 3, [int, float, str])
    tuples_list3 = create_random_tuples(100, 3, [int, float, str])
    sort_insertion(tuples_list1, key=lambda x: x[0])

    sort_insertion(tuples_list2, key=lambda x: x[1])

    sort_insertion(tuples_list3, key=lambda x: x[2])