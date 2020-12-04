import unittest
from imagenate.concat import concat_image_by_path, Direction
import os


class TestImagenate(unittest.TestCase):
    def test_create_concat_image(self):
        print(f"getcwd {os.getcwd()}")
        # img = create_concat_image('tests/assets/blue_100x50.png', 'tests/assets/red_100x50.png')
        img = concat_image_by_path(
            [
                "tests/assets/blue_100x50.png",
                "tests/assets/red_100x50.png",
                "tests/assets/green_100x50.png",
            ],
            direction=Direction.HORIZONTAL,
        )
        print(img)
        img.save("concat.png")
        self.assertEqual("hello", "hello", "hello is misssing")
