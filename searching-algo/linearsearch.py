print("------------ This Is Linear Search ------------- ")

# Basic Linear Search


# def linear_search(L, x):
#     n = len(L)
#     i = 0
#     while i < n:
#         if L[i] == x:
#             return i
#         i += 1

#     i = -1
#     return i

# I can implement the same thing with for loop

def linear_search(L, x):
    n = len(L)

    for i in range(n):
        if L[i] == x:
            return i

    return -1


if __name__ == "__main__":
    ListOfNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    CheckNumber = 12
    found_number_index = linear_search(
        ListOfNumber, CheckNumber)
    if found_number_index > -1:
        print("Number found at ", found_number_index,
              " Index  And Number is ", ListOfNumber[found_number_index])
    else:
        print(CheckNumber, " not found in the  list ")
    """
    - This linear search algorithm depends on the number of item I'll search for
    - That's why it's depend on N number 
    - The Worst case of time complexity would be O(n)
    
    """
