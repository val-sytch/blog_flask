import os
import unittest
from blog.servises.img_resizer_and_watermark_add import compare_width_height, image_resize, put_watermark


class CompareWidthHeightTestCase(unittest.TestCase):

    def test_compare_width_height(self):
        """
        Check if function is calculate correctly, if/else structure.
        """
        required_width = 400
        required_height = 300

        result = compare_width_height(required_width, required_height, 1200, 600)
        self.assertEqual(result[0], 400)
        self.assertLess(result[1], 300)

        result = compare_width_height(required_width, required_height, 600, 1200)
        self.assertLess(result[0], 400)
        self.assertEqual(result[1], 300)

        result = compare_width_height(required_width, required_height, 500, 200)
        self.assertEqual(result[0], 400)
        self.assertLess(result[1], 200)

        result = compare_width_height(required_width, required_height, 200, 500)
        self.assertLess(result[0], 200)
        self.assertEqual(result[1], 300)

        result = compare_width_height(required_width, required_height, 300, 200)
        self.assertEqual(result, (300, 200))

    def test_image_resize(self):
        """
        Check if result is tuple of
        1. resized image
        2. tuple of width and heights of image
        Comment: Maybe I should use mock obj instead real file, I swear, I tried, but not succeed.
        """
        tmp_file = os.path.join(os.path.dirname(__file__), "image.jpg")
        result = image_resize(tmp_file, 400, 300)
        self.assertEqual(result[0].mode, "RGBA")
        self.assertEqual(type(result[1]), tuple)

    def test_put_watermark(self):
        """
        1. Check that function do nothing if file with watermark is absent
        2. Check if watermark file is in unsupported format

        """
        # 1
        tmp_file = os.path.join(os.path.dirname(__file__), "image.jpg")
        watermark = os.path.join(os.path.dirname(__file__), "notexists_file.jpg")
        result = put_watermark(tmp_file, watermark, 0.2, (300, 200))
        self.assertEqual(tmp_file, result)
        # 2
        watermark = os.path.join(os.path.dirname(__file__), "watermark1.jpg")
        result = put_watermark(tmp_file, watermark, 0.2, (300, 200))
        self.assertEqual(tmp_file, result)


if __name__ == '__main__':
    unittest.main()
