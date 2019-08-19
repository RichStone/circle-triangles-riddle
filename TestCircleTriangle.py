import unittest
from CircleTriangle import CircleTriangle


class TestEuroTriangle(unittest.TestCase):
    def test_regular_triangle_counts_6_bottom_row_circles_correctly(self):
        triangle = CircleTriangle(6)
        self.assertEqual(35, triangle.count_regular_triangles())

    def test_regular_triangle_counts_5_bottom_row_circles_correctly(self):
        triangle = CircleTriangle(5)
        self.assertEqual(20, triangle.count_regular_triangles())

    def test_regular_triangle_counts_4_bottom_row_circles_correctly(self):
        triangle = CircleTriangle(4)
        self.assertEqual(10, triangle.count_regular_triangles())

    def test_regular_triangle_counts_3_bottom_row_circles_correctly(self):
        triangle = CircleTriangle(3)
        self.assertEqual(4, triangle.count_regular_triangles())

    def test_smallest_even_bottom_triangle_counts_one(self):
        triangle = CircleTriangle(2)
        self.assertEqual(1, triangle.count_regular_triangles())

    def test_smallest_odd_bottom_triangle_counts_zero_upside_down_triangles(self):
        triangle = CircleTriangle(2)
        self.assertEqual(0, triangle.count_upside_down_triangles())

    def test_upside_down_triangles_counted_correctly_for_4_bottom_row_circles(self):
        triangle = CircleTriangle(4)
        self.assertEqual(3, triangle.count_upside_down_triangles())

    def test_upside_down_triangles_counted_correctly_for_5_odd_bottom_row_circles(self):
        triangle = CircleTriangle(5)
        self.assertEqual(7, triangle.count_upside_down_triangles())

    def test_upside_down_triangles_counted_correctly_for_6_bottom_row_circles(self):
        triangle = CircleTriangle(6)
        self.assertEqual(13, triangle.count_upside_down_triangles())

    def test_impossible_to_initialize_a_triangle_with_circles_in_bottom_row_less_than_2(self):
        with self.assertRaises(Exception) as context:
            CircleTriangle(1)
        self.assertTrue('A triangle of circles cannot consist of less than 2 circles in the bottom row.' in str(context.exception))

    def test_get_correct_triangle_sums(self):
        triangle = CircleTriangle(2)
        self.assertEqual(1, triangle.triangle_sum)

        triangle = CircleTriangle(3)
        self.assertEqual(5, triangle.triangle_sum)

        triangle = CircleTriangle(4)
        self.assertEqual(13, triangle.triangle_sum)

        triangle = CircleTriangle(5)
        self.assertEqual(27, triangle.triangle_sum)

    def test_counts_circles_correctly(self):
        triangle = CircleTriangle(2)
        self.assertEqual(3, triangle.circles_amount)

        triangle = CircleTriangle(3)
        self.assertEqual(6, triangle.circles_amount)

        triangle = CircleTriangle(4)
        self.assertEqual(10, triangle.circles_amount)
