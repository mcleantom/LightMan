from unittest import TestCase

from light_man import Point, Rectangle


class TestModels(TestCase):
    def test_rectangle(self):
        p1 = Point(x=0, y=0)
        p2 = Point(x=1, y=1)
        r = Rectangle(p1=p1, p2=p2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        shp = r.to_shapely()
        self.assertEqual(shp.bounds, (0, 0, 1, 1))
