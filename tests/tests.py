from src.Queue import Queue
from src.fiboandfasctori import fibo, fibo_recursive, factorial, factorial_recursive
from src.sort import bubble_sort, quick_sort, counting_sort, radix_sort, heap_sort, bucket_sort
from src.stack import Stack
import pytest

class TestTest:
    def test(self):
        "Тесты"
        assert fibo_recursive(1) == 1
        assert fibo_recursive(2) == 1
        assert fibo_recursive(3) == 2
        assert fibo_recursive(4) == 3
        assert fibo_recursive(5) == 5
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
        assert factorial_recursive(1) == 1
        assert factorial_recursive(2) == 2
        assert factorial_recursive(3) == 6
        assert factorial_recursive(4) == 24
        assert factorial_recursive(5) == 120
        assert fibo(1) == 1
        assert fibo(2) == 1
        assert fibo(3) == 2
        assert fibo(4) == 3
        assert fibo(5) == 5
        assert counting_sort([1])==[1]
        assert counting_sort([]) == []
        assert radix_sort([1],10) == [1]
        assert radix_sort([],10) == []
        assert bubble_sort([1]) == [1]
        assert bubble_sort([]) == []
        assert heap_sort([1]) == [1]
        assert heap_sort([]) == []
        assert quick_sort([1]) == [1]
        assert quick_sort([]) == []
        assert counting_sort([4, 5, 1]) == [1, 4, 5]
        assert counting_sort([1, 3, 6, 1, 2]) == [1, 1, 2, 3, 6]
        assert counting_sort([10, 15, 9]) == [9, 10, 15]
        assert radix_sort([10, 15, 9],10) == [9, 10, 15]
        assert radix_sort([1, 3, 6, 1, 2],10) == [1, 1, 2, 3, 6]
        assert radix_sort([4, 5, 1],10) == [1, 4, 5]
        assert bubble_sort([4, 5, 1]) == [1, 4, 5]
        assert bubble_sort([1, 3, 6, 1, 2]) == [1, 1, 2, 3, 6]
        assert bubble_sort([10, 15, 9]) == [9, 10, 15]
        assert bubble_sort(['c','b','a']) == ['a','b','c']
        assert bubble_sort(['ad','a','ab']) == ['a','ab','ad']
        assert quick_sort([4, 5, 1]) == [1, 4, 5]
        assert quick_sort([1, 3, 6, 1, 2]) == [1, 1, 2, 3, 6]
        assert quick_sort([10, 15, 9]) == [9, 10, 15]
        assert quick_sort(['c', 'b', 'a']) == ['a', 'b', 'c']
        assert quick_sort(['ad', 'a', 'ab']) == ['a', 'ab', 'ad']
        assert heap_sort([4, 5, 1]) == [1, 4, 5]
        assert heap_sort([1, 3, 6, 1, 2]) == [1, 1, 2, 3, 6]
        assert heap_sort([10, 15, 9]) == [9, 10, 15]
        assert heap_sort(['c', 'b', 'a']) == ['a', 'b', 'c']
        assert heap_sort(['ad', 'a', 'ab']) == ['a', 'ab', 'ad']
        assert bucket_sort([8.42,3.47,9.45,9.41],4)==[3.47, 8.42, 9.41, 9.45]
        assert bucket_sort([3.46,9.41,8.52],None) == [3.46,8.52,9.41]
        assert bucket_sort([3.46,9.41,8.54,8.52,9.01],5) == [3.46,8.52,8.54,9.01,9.41]
        s = Stack()
        s.push(4)
        s.push(3)
        s.push(1)
        assert s.pop() == 1
        assert s.peek() == 3
        assert s.is_empty() is True
        f = Queue()
        f.enqueue(4)
        f.enqueue(3)
        f.enqueue(1)
        assert f.dequeue() == 4
        assert f.front() == 3
        assert f.is_empty() is True

    def TestErrors(self):
        "Тестирование ошибок"
        with pytest.raises(IndexError):
            s = Stack()
            s.pop()
            s.peek()
            q = Queue()
            q.front()
            q.dequeue()
