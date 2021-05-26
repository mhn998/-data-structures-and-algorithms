from code_challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_multi_bracket_validation_1():
    actual= multi_bracket_validation(f'[({{}}]')
    expected= False
    assert actual==expected

def test_multi_bracket_validation_2():
    actual= multi_bracket_validation('{(})')
    expected= False
    assert actual==expected

def test_multi_bracket_validation_3():
    actual= multi_bracket_validation('(](')
    expected= False
    assert actual==expected

def test_multi_bracket_validation_4():
    actual= multi_bracket_validation('{([("Muhannad"[)]]})')
    expected= False
    assert actual==expected

def test_multi_bracket_validation_5():
    actual= multi_bracket_validation(f'({{]}})')
    expected= False
    assert actual==expected

def test_multi_bracket_validation_6():
    actual= multi_bracket_validation(f'{{}}')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_7():
    actual= multi_bracket_validation('(Muhannad)')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_8():
    actual= multi_bracket_validation(f'{{}}(){{}}')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_9():
    actual= multi_bracket_validation(f'(){{}}[[]]')
    expected= True
    assert actual==expected
