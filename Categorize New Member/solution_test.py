from solution import open_or_senior

def test_case_1():
    assert open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]) == ['Open', 'Senior', 'Open', 'Senior']

def test_case_2():
    assert open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]) == ['Open', 'Open', 'Senior', 'Open']
