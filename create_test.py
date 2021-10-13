import unittest
import  check


class MyTestCase(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(check.word_count(),3)


if __name__ == '__main__':
    unittest.main()