def average(L):
    if not L:
        return None

    return sum(L)/len(L)


def test_average():
    assert 3.0 == average([1, 2, 3, 4, 5])


if __name__ == "__main__":
    # L = [1, 2, 3, 4, 5]
    # expected_result = 3
    # result = average(L)
    # assert expected_result == result, "Average function produce incorrect result "

    """
    Hard Coded Testing For average()
    -----
        if expected_result == result:
        print("Passed all test cases")
    else:
        print("Test failed", "received: ", result,
              "expected :", expected_result)
    """
