# fizzbuzz.pyのテストコード
import unittest
from fizzbuzz import fizzbuzz


# FizzBuzzが正しく動作するかテスト
class TestFizzBuzz(unittest.TestCase):
    # テストする
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(15), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
