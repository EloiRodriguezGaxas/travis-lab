import unittest
import hello as hello

class TestHelloFile(unittest.TestCase):

    def test_positive(self):
        result = hello.addTwoNumbers(1, 3)
        self.assertEqual(result, 4)

    def test_negative(self):
        result = hello.addTwoNumbers(-1, -10)
        self.assertEqual(result, -11)

if __name__ == '__main__':
    unittest.main()