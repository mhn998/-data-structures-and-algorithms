from code_challenges.array_reverse.array_reverse import reverse_array, reverse_array_2 , reverse_array_3 , reverse_array_4

def test_array_reverse():
    expected = [6, 5, 4, 3, 2, 1]
    inputs = [1, 2, 3, 4, 5, 6]
    actual = reverse_array(inputs)
    assert actual == expected

def test_array_reverse_2():
    expected = [6, 5, 4, 3, 2, 1]
    inputs = [1, 2, 3, 4, 5, 6]
    actual = reverse_array_2(inputs)
    assert actual == expected

def test_array_reverse_3():
    expected = [6, 5, 4, 3, 2, 1]
    inputs = [1, 2, 3, 4, 5, 6]
    actual = reverse_array_3(inputs)
    assert actual == expected

def test_array_reverse_4():
    expected = [6, 5, 4, 3, 2, 1]
    inputs = [1, 2, 3, 4, 5, 6]
    actual = reverse_array_4(inputs)
    assert actual == expected
