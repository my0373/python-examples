from unittest import TestCase

from minecoords import calc_y, calc_x, calc_z, calc_dimension


class TryTesting(TestCase):
    def test_calc_y_nether(self):
        """
        Check the nether Y co-ordinates calculation
        """
        self.assertEqual(calc_y(100,"nether"),100)

    def test_calc_z_nether(self):
        self.assertEqual(calc_z(800,"nether"),6400)

    def test_calc_x_nether(self):
        self.assertEqual(calc_z(1000,"nether"),8000)

    def test_calc_z_overworld(self):
        self.assertEqual(calc_z(800,"overworld"),100)

    def test_calc_y_overworld(self):
        self.assertEqual(calc_y(100,"overworld"),100)

    def test_calc_x_overworld(self):
        self.assertEqual(calc_x(800,"overworld"),100)

    def test_calc_dimension_nether(self):
        self.assertEqual(calc_dimension("nether"),"overworld")

    def test_calc_x_type(self):
        self.assertIsInstance(calc_x(800,"overworld"),int)

    def test_calc_dimension_type(self):
        self.assertIsInstance(calc_dimension("overworld"),str)

    def test_calc_dimension_overworld(self):
        self.assertEqual(calc_dimension("overworld"),"nether")



    # def test_always_passes(self):
    #
    #     self.assertTrue(True)
    #
    #
    #
    # def test_always_fails(self):
    #     self.assertTrue(False)