import unittest
from dz40 import split_names_ages

class SplitTest(unittest.TestCase):
    def test_split(self):
        data = [('Alice', 30), ('Bob', 25), ('Charlie', 40)]
        expected_names = ['Alice', 'Bob', 'Charlie']
        expected_ages = [30, 25, 40]
        names, ages = split_names_ages(data)
        self.assertEqual(names, expected_names)
        self.assertEqual(ages, expected_ages)

    def test_split1(self):
        data = []
        expected_names = []
        expected_ages = []
        names, ages = split_names_ages(data)
        self.assertEqual(names, expected_names)
        self.assertEqual(ages, expected_ages)


if __name__ == '__main__':
    unittest.main()
