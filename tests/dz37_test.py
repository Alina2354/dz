from unittest import TestCase
from dz37 import divide

class DivideTest(TestCase):
    def test_divide(self):
        self.assertEqual(divide(10,2),5.0)

    def test_exceptions1(self):
        with self.assertRaises(TypeError) as e:
            divide('dfvf', 2)

    def test_exceptions2(self):
        with self.assertRaises(ZeroDivisionError) as e:
            divide(5, 0)

if __name__ == '__main__':
    main()