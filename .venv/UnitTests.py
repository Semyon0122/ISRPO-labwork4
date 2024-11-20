import unittest
import math

import square
import triangle
import rectangle
import circle

class TestGeometryFunctions(unittest.TestCase):

    '''square'''
    def test_square_area(self):
        with self.subTest("Positive side"):
            self.assertEqual(square.area(4), 16)
        with self.subTest("Zero side"):
            self.assertEqual(square.area(0), 0)
        with self.subTest("Negative side"):
            self.assertEqual(square.area(-2.5), 0)
        with self.subTest("String input"):
            with self.assertRaises(TypeError):
                square.area("string")

    def test_square_perimeter(self):
        with self.subTest("Positive side"):
            self.assertEqual(square.perimeter(4), 16)
        with self.subTest("Zero side"):
            self.assertEqual(square.perimeter(0), 0)
        with self.subTest("Negative side"):
            self.assertEqual(square.perimeter(-2.5), 0)
        with self.subTest("String input"):
            with self.assertRaises(TypeError):
                square.perimeter("string")

    '''triangle'''
    def test_triangle_area(self):
        with self.subTest("Positive sides"):
            self.assertEqual(triangle.area(4, 5), 10)
        with self.subTest("Zero height"):
            self.assertEqual(triangle.area(0, 4), 0)
        with self.subTest("Negative sides"):
            self.assertEqual(triangle.area(-10, -10), 0)
        with self.subTest("String input"):
            with self.assertRaises(TypeError):
                triangle.area("string")

    def test_triangle_perimeter(self):
        with self.subTest("Valid sides"):
            self.assertEqual(triangle.perimeter(4, 3, 2), 9)
        with self.subTest("One side zero"):
            self.assertEqual(triangle.perimeter(0, 3, 5), 0)
        with self.subTest("Negative sides"):
            self.assertEqual(triangle.perimeter(-2.5, 2.5, 5), 0)
        with self.subTest("String input"):
            with self.assertRaises(TypeError):
                triangle.perimeter("string")

    '''rectangle'''
    def test_rectangle_area(self):
        with self.subTest("Positive sides"):
            self.assertEqual(rectangle.area(3, 3), 9)
        with self.subTest("One side zero"):
            self.assertEqual(rectangle.area(0, 10), 0)
        with self.subTest("Negative side"):
            self.assertEqual(rectangle.area(-2.5, 2.5), 0)
        with self.subTest("String input"):
            with self.assertRaises(TypeError):
                rectangle.area("string")

    def test_rectangle_perimeter(self):
        with self.subTest("Positive sides"):
            self.assertEqual(rectangle.perimeter(4, 5), 18)
        with self.subTest("Zero sides"):
            self.assertEqual(rectangle.perimeter(0, 0), 0)
        with self.subTest("Negative side"):
            self.assertEqual(rectangle.perimeter(-10, 10), 0)
        with self.subTest("String input"):
            with self.assertRaises(TypeError):
                rectangle.perimeter("string")

    '''circle'''
    def test_circle_area(self):
        with self.subTest("Positive radius"):
            self.assertAlmostEqual(circle.area(3), math.pi * 3 * 3)
        with self.subTest("Zero radius"):
            self.assertEqual(circle.area(0), 0)
        with self.subTest("Negative radius"):
            self.assertEqual(circle.area(-2.5), 0)
        with self.subTest("String input"):
            with self.assertRaises(TypeError):
                circle.area("string")

    def test_circle_perimeter(self):
        with self.subTest("Positive radius"):
            self.assertAlmostEqual(circle.perimeter(4), 2 * math.pi * 4)
        with self.subTest("Zero radius"):
            self.assertEqual(circle.perimeter(0), 0)
        with self.subTest("Negative radius"):
            self.assertEqual(circle.perimeter(-10), 0)
        with self.subTest("String input"):
            with self.assertRaises(TypeError):
                circle.perimeter("string")




def run_tests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestGeometryFunctions)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    total_tests = result.testsRun
    failed_tests = len(result.failures) + len(result.errors)
    if total_tests >= failed_tests and total_tests > 0:
        successful_tests = total_tests - failed_tests
        success_rate = (successful_tests / total_tests) * 100
    else:
        successful_tests = 0
        success_rate = 0

    print("\n" + "=" * 40)
    print(f"Total tests run: {total_tests}")
    print(f"Successful tests: {successful_tests}")
    print(f"Failed tests: {failed_tests}")
    print(f"Success rate: {success_rate:.2f}%")
    print("=" * 40)


if __name__ == "__main__":
    run_tests()