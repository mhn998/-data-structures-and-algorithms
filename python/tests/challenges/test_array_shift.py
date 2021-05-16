from code_challenges.array_shift.array_shift import insertShiftArray , insertShiftArray_1

def test_array_shift_even():
    expected=[2,4,5,6,8]
    actual= insertShiftArray([2,4,6,8], 5)
    assert actual == expected

def test_array_shift_odd():
    expected=[4,8,15,16,23,42]
    actual= insertShiftArray([4,8,15,23,42], 16)
    assert actual == expected

def test_array_shift_1_even():
    expected=[2,4,5,6,8]
    actual= insertShiftArray_1([2,4,6,8], 5)
    assert actual == expected


def test_array_shift_1_odd():
    expected = [4,8,15,16,23,42]
    actual = insertShiftArray_1([4,8,15,23,42], 16)
    assert actual == expected
