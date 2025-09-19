def sub(a, b):
    return a - b

def length(list):
    return len(list)

def test_sub_and_len():
    assert (sub(3, 2)) == 1
    assert(length([1, 2, 3, 4])) == 4