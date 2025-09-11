import unittest
from dz42 import merge_lists

class MergeTest(unittest.TestCase):
    def test_merge(self):
        list1 = [1, 2]
        list2 = ['a', 'b']
        list3 = []
        expected_merged_list = [1, 2, 'a', 'b']

        merged_list = merge_lists(list1, list2, list3)
        self.assertEqual(merged_list, expected_merged_list)


if __name__ == '__main__':
    unittest.main()
