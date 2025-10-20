import unittest
from ci_demo.my_module import add

class TestAdd(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(2, 3), 5)  # Ce test va échouer à cause du +1 dans add()

if __name__ == '__main__':
    unittest.main()