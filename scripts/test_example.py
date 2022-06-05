import unittest

from .script_example import bubble_sort

# https://docs.python.org/3/library/unittest.html
class TestSort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(bubble_sort([]), [])

    def test_sort(self):
        self.assertEqual(bubble_sort([1, 3, 2]), [1, 2, 3])

    def test_single(self):
        self.assertEqual(bubble_sort([1]), [1])


if __name__ == "__main__":
    unittest.main()
