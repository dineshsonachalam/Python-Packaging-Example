from unittest import TestCase
import sample_package

class TestJoke(TestCase):
    def test_is_string(self):
        s = sample_package.joke()
        self.assertTrue(isinstance(s, str))
