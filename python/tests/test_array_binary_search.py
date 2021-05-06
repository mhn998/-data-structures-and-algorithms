from code_challenges.array_binary_search.array_binary_search import BinarySearch

def test_BinarySearch_1():
    actual= BinarySearch([4,8,15,16,23,42], 15)
    expected= 2
    assert actual==expected

def test_BinarySearch_2():
    actual= BinarySearch([11,22,33,44,55,66,77], 90)
    expected= -1
    assert actual==expected


def test_BinarySearch_3():
    actual= BinarySearch([1, 2, 3.5, 5, 6, 7], 3.5)
    expected= 2
    assert actual==expected



def test_BinarySearch_4():
    actual= BinarySearch(['str1' , 'str2'], 4)
    expected= "Are you trying to fool me? please insert an array of numbers!"
    assert actual==expected


def test_BinarySearch_5():
    actual= BinarySearch([4,8,15,23,42,55,64,69], '1')
    expected= "it seems you are trying wrong input types , please insert any number"
    assert actual==expected
