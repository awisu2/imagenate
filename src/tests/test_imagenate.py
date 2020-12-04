import unittest
import imagenate

class TestImagenate(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(imagenate.hello(), 'hello', 'hello is misssing')
