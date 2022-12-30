# Binary  Search
print("------------ Binary Search --------")


def binary_search(L, x):
    left = 0
    right = len(L) - 1

    while left <= right:
        mid = (left + right) // 2

        if L[mid] == x:
            return mid

        if L[mid] < x:
            left = mid + 1
        if L[mid] > x:
            right = mid - 1

    return -1


if __name__ == "__main__":
    ListOfNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    CheckNumber = 14
    found_number_index = binary_search(
        ListOfNumber, CheckNumber)
    if found_number_index > -1:
        print("Number found at ", found_number_index,
              " Index  And Number is ", ListOfNumber[found_number_index])
    else:
        print(CheckNumber, " not found in the  list ")

    """
    Binary search alogorithm split the list and then check until get the ultimate number 
    --- 
    It not check every number, that's why The worse complexity of binary search O(log n )
    """
