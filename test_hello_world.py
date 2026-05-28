import unittest
from hello_world import greet

class TestHelloWorld(unittest.TestCase):
    def test_greet_default(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_greet_custom(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

if __name__ == "__main__":
    unittest.main()
