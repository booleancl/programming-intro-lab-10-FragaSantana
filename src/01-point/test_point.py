from point import Point

class TestDice:
    def test_is_a_point(self):
        point = Point()
        assert isinstance(point, Point)

    def test_init(self):
        point = Point(0,0)
        assert point.y == 0
        assert point.x == 0
    
    def test_move(self):
        point = Point(0,0)
        point.move(3,4)
        assert point.x == 3
        assert point.y == 4
    
    def test_reset(self):
        point = Point(4,3)
        point.reset()
        assert point.x == 0
        assert point.y == 0
    
    def test_distance_to(self):
        point_a = Point()
        point_b = Point(4,3)
        assert point_a.distance_to(point_b) == 5.0

