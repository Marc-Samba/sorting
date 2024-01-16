import sorting.py

def test_sort():
    #test de cas simples
    assert sorting.quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sorting.quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sorting.quick_sort([1, 3, 2, 5, 4]) == [1, 2, 3, 4, 5]
    assert([])==[]
    assert([1])==[1]
    assert([1,2])==[1,2]