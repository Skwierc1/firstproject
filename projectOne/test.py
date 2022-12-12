#  test fle for project1.py using pytest
import project1 as project1


# test for point
# testing requirements:
#     # Point(x, y) - Create a point with the given x and y coordinates.
#     # __repr__() - Return a string representation of the point.
#     # get_x() - Return the x coordinate of the point.
#     # get_y() - Return the y coordinate of the point.
#     # set_x(x) - Set the x coordinate of the point.
#     # set_y(y) - Set the y coordinate of the point.

def test_point():
    point = project1.Point(1, 2)
    assert point.get_x() == 1
    assert point.get_y() == 2
    point.set_x(3)
    point.set_y(4)
    assert point.get_x() == 3
    assert point.get_y() == 4


# test for line segment
# testing requirements:
#     # LineSegment(point1, point2) - Create a line segment with the given endpoints.
#     # __repr__() - Return a string representation of the line segment.
#     # get_point1() - Return the first endpoint of the line segment.
#     # get_point2() - Return the second endpoint of the line segment.
#     # set_point1(point) - Set the first endpoint of the line segment.
#     # set_point2(point) - Set the second endpoint of the line segment.

def test_line_segment():
    point1 = project1.Point(1, 2)
    point2 = project1.Point(3, 4)
    line_segment = project1.LineSegment(point1, point2)
    assert line_segment.get_point1() == point1
    assert line_segment.get_point2() == point2
    line_segment.set_point1(project1.Point(5, 6))
    line_segment.set_point2(project1.Point(7, 8))
    assert line_segment.get_point1() == project1.Point(5, 6)
    assert line_segment.get_point2() == project1.Point(7, 8)



# test for Circle class
# testing requirements:
#     # Circle(point, radius) - Create a circle with the given center point and radius.
#     # __repr__() - Return a string representation of the circle.
#     # get_center() - Return the center point of the circle.
#     # get_radius() - Return the radius of the circle.
#     # set_center(point) - Set the center point of the circle.
#     # set_radius(radius) - Set the radius of the circle.

def test_circle():
    point = project1.Point(1, 2)
    circle = project1.Circle(point, 3)
    assert circle.get_center() == point
    assert circle.get_radius() == 3
    circle.set_center(project1.Point(4, 5))
    circle.set_radius(6)
    assert circle.get_center() == project1.Point(4, 5)
    assert circle.get_radius() == 6


# test for distance function
# testing requirements:
#     # distance(point1, point2) - Return the distance between the two points.
def test_distance():
    # Test 1
    point1 = project1.Point(1, 2)
    point2 = project1.Point(3, 4)
    assert project1.distance(point1, point2) == 2.8284271247461903

    # Test 2
    point1 = project1.Point(1, 2)
    point2 = project1.Point(1, 2)
    assert project1.distance(point1, point2) == 0


# test for lineSegmentIntersection function
# testing requirements:
#     # lineSegmentIntersection(lineSegment1, lineSegment2) - Return the intersection point of the two line segments.
def test_lineSegmentIntersection():
    # Test 1
    point1 = project1.Point(1, 2)
    point2 = project1.Point(3, 4)
    point3 = project1.Point(5, 6)
    point4 = project1.Point(7, 8)
    lineSegment1 = project1.LineSegment(point1, point2)
    lineSegment2 = project1.LineSegment(point3, point4)
    assert project1.lineSegmentIntersection(lineSegment1, lineSegment2) == None



# test for closestPairOfPoints function
# testing requirements:
#     # closestPairOfPoints(points) - Return the closest pair of points in the list.
def test_closestPairOfPoints():
    # Test 1
    point1 = project1.Point(1, 2)
    point2 = project1.Point(3, 4)
    point3 = project1.Point(5, 6)
    point4 = project1.Point(7, 8)
    point5 = project1.Point(9, 10)
    point6 = project1.Point(11, 12)
    point7 = project1.Point(13, 14)
    point8 = project1.Point(15, 16)
    point9 = project1.Point(17, 18)
    point10 = project1.Point(19, 20)
    point11 = project1.Point(21, 22)

    points = [point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11]
    assert project1.closestPairOfPoints(points) == (point1, point2)

    # Test 2
    point1 = project1.Point(1, 2)
    point2 = project1.Point(19, 20)
    point3 = project1.Point(5, 6)
    point4 = project1.Point(7, 8)
    point5 = project1.Point(9, 10)
    point6 = project1.Point(11, 12)
    point7 = project1.Point(13, 14)
    point8 = project1.Point(15, 16)
    point9 = project1.Point(17, 18)
    point10 = project1.Point(3, 4)
    point11 = project1.Point(21, 22)
    point12 = project1.Point(23, 24)
    
    points = [point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12]
    assert project1.closestPairOfPoints(points) == (point1, point10)


# test for convexHull function - monotone chain algorithm
# testing requirements:
#     # convexHull(points) - Return the convex hull of the points.
def test_monoCovexHull():
    # Test 1
    point1 = project1.Point(1, 1)
    point2 = project1.Point(3, 0)
    point3 = project1.Point(3, 2)
    point4 = project1.Point(5, 1)
    point5 = project1.Point(0, 3)
    point6 = project1.Point(2, 4)
    point7 = project1.Point(5, 4)
    point8 = project1.Point(1, 5)
    point9 = project1.Point(2, 6)
    point10 = project1.Point(4, 5)
    point11 = project1.Point(2, 3)

    points = [point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11]
    assert project1.convexHull(points) == [point2, point4, point7, point10, point9, point8, point5, point1]
 
    # Test 2
    point1 = project1.Point(1,0)
    point2 = project1.Point(2,1)
    point3 = project1.Point(3,1)
    point4 = project1.Point(1,2)
    point5 = project1.Point(2,3)
    point6 = project1.Point(2,4)
    point7 = project1.Point(0,2)

    points = [point1, point2, point3, point4, point5, point6, point7]
    assert project1.convexHull(points) == [point1, point3, point6, point7]

def test_largestEmptyCircle():
    # Test 1
    point1 = project1.Point(1,0)
    point2 = project1.Point(2,1)
    point3 = project1.Point(3,1)
    point4 = project1.Point(1,2)
    point5 = project1.Point(2,3)
    point6 = project1.Point(2,4)
    point7 = project1.Point(0,2)


    circle1 = project1.Circle(point1,3)
    circle2 = project1.Circle(point2,1)
    circle3 = project1.Circle(point3,2)
    circle4 = project1.Circle(point4,5)
    circle5 = project1.Circle(point5,3)
    circle6 = project1.Circle(point6,1)
    circle7 = project1.Circle(point7,1)
    
    circles = [circle1, circle2, circle3, circle4, circle5, circle6, circle7]
    assert project1.largestEmptyCircle(circles) == circle2


def test_show_obj():

    point1 = project1.Point(1,0)
    point2 = project1.Point(2,1)
    point3 = project1.Point(3,1)
    point4 = project1.Point(1,2)
    points = [point1,point2,point3,point4]

    lineSegment1 = project1.LineSegment(point1, point2)
    lineSegment2 = project1.LineSegment(point3, point4)
    lineSegments = [lineSegment1,lineSegment2]

    circle1 = project1.Circle(point1,3)
    circle2 = project1.Circle(point2,1)
    circle3 = project1.Circle(point3,2)
    circle4 = project1.Circle(point4,5)
    circles = [circle1,circle2, circle3, circle4]
    assert project1.show_obj(points, lineSegments,circles) == "Points: (1, 0), (2, 1), (3, 1), (1, 2)\nLines: LineSegment((1, 0), (2, 1)), LineSegment((3, 1), (1, 2))\nCircles: Circle((1, 0), 3), Circle((2, 1), 1), Circle((3, 1), 2), Circle((1, 2), 5)\n"





