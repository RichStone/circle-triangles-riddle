from math import ceil


class CircleTriangle:
    """

    """

    def __init__(self, bottom_row_size):
        if bottom_row_size < 2:
            raise Exception('A triangle of circles cannot consist of less than 2 circles in the bottom row.')

        self.bottom_row_size = bottom_row_size
        # You can place (bottom_row_circles - 1) 3-circle-triangles in the bottom row.
        # Which is the max amount of small triangles in one row.
        self.max_regular_triangles_bottom_row = self.bottom_row_size - 1
        self.triangle_sum = self.count_regular_triangles() + self.count_upside_down_triangles()
        self.circles_amount = self.calculate_nth_triangular_number()

    def count_regular_triangles(self):
        """
        Regular circle triangles look like a pyramid.

        Returns:
            The count sum of regular triangles.
        """

        # the smallest triangle is a special case
        if self.max_regular_triangles_bottom_row == 1:
            return 1

        subtotal = 0
        multiplier = 1
        for i in range(self.max_regular_triangles_bottom_row, 0, -1):
            subtotal += multiplier * i
            multiplier += 1

        return subtotal

    def count_upside_down_triangles(self):
        """
        Upside down circle triangles look like a reversed pyramid. The circles triangle can have
        (n - 2) upside down circles.

        Returns:
            The count sum of upside down triangles.
        """
        def recursive_count(offset, subtotal):
            offset = offset - 2
            if offset > 0:
                for i in range(1, offset + 1, +1):
                    subtotal += i
                return recursive_count(offset, subtotal)
            return subtotal

        count = recursive_count(self.bottom_row_size, 0)
        return count

    def calculate_nth_triangular_number(self):
        # formula used as described here: https://math.stackexchange.com/a/60581/337926
        return round((self.bottom_row_size ** 2 + self.bottom_row_size) / 2)


if __name__ == '__main__':
    triangle = CircleTriangle(1500)
    print(triangle.triangle_sum)
    print(triangle.circles_amount)
