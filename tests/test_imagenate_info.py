import unittest
from imagenate.info import get_info


class TestImagenateInfo(unittest.TestCase):
    def test_get_info(self):
        # keys::
        # gamma
        # chromaticity
        # exif
        # dpi
        # XML:com.adobe.xmp
        info = get_info("tests/assets/blue_100x50.png")

        for k in info:
            print(k)
            print(info[k])
        # # self.assertEqual("hello", "hello", "hello is misssing")
        return info
