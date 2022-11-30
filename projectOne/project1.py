#You need to be able to represent the following on a plane (Euclidean 2-dimensional space):
    # Points
    # Line Segments
    # Circles

#You need to be able to perform the following operations on the above objects:
    # Line segment intersection: Find the intersections between a given set of line segments.
    # Closest pair of points: Given a set of points, find the two with the smallest distance from each other.
    # Convex hull: Given a set of points, find the smallest convex polyhedron/polygon containing all the points, represented as the set of points on the polygon edge.
    # Largest empty circle: Given a set of points, find a largest circle with its center inside of their convex hull and enclosing none of them.


# Program ----------------------------------------------------------------

# libraries / modules
import math


# Point class
# testing requirements:
#     # Point(x, y) - Create a point with the given x and y coordinates.
#     # __repr__() - Return a string representation of the point.
#     # get_x() - Return the x coordinate of the point.
#     # get_y() - Return the y coordinate of the point.
#     # set_x(x) - Set the x coordinate of the point.
#     # set_y(y) - Set the y coordinate of the point.
class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # if none, return false
        if other is None:
            return False
        # if not a point, return false
        if not isinstance(other, Point):
            return False
        # if x and y are equal, return true
        if self.x == other.x and self.y == other.y:
            return True

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def get_point(self):
        return (self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


# LineSegment class
# testing requirements:
#     # LineSegment(point1, point2) - Create a line segment with the given endpoints.
#     # __repr__() - Return a string representation of the line segment.
#     # get_point1() - Return the first endpoint of the line segment.
#     # get_point2() - Return the second endpoint of the line segment.
#     # set_point1(point) - Set the first endpoint of the line segment.
#     # set_point2(point) - Set the second endpoint of the line segment.
class LineSegment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __repr__(self):
        return "LineSegment({}, {})".format(self.point1, self.point2)

    def get_point1(self):
        return self.point1

    def get_point2(self):
        return self.point2

    def set_point1(self, point):
        self.point1 = point

    def set_point2(self, point):
        self.point2 = point
    

# Circle class
# testing requirements:
#     # Circle(point, radius) - Create a circle with the given center and radius.
#     # __repr__() - Return a string representation of the circle.
#     # get_center() - Return the center of the circle.
#     # get_radius() - Return the radius of the circle.
#     # set_center(point) - Set the center of the circle.
#     # set_radius(radius) - Set the radius of the circle.
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def get_center(self):
        return self.center

    def get_radius(self):
        return self.radius

    def set_center(self, center):
        self.center = center

    def set_radius(self, radius):
        self.radius = radius

    def __repr__(self):
        return "Circle({}, {})".format(self.center, self.radius)

# lineSegmentIntersection function
# testing requirements:
#     # lineSegmentIntersection(lineSegment1, lineSegment2) - Return the intersection point of the two line segments, or None if they do not intersect.
def lineSegmentIntersection(lineSegment1, lineSegment2):
    # get the points of the line segments
    point1 = lineSegment1.get_point1()
    point2 = lineSegment1.get_point2()
    point3 = lineSegment2.get_point1()
    point4 = lineSegment2.get_point2()

    # get the coordinates of the points
    x1 = point1.get_x()
    y1 = point1.get_y()
    x2 = point2.get_x()
    y2 = point2.get_y()
    x3 = point3.get_x()
    y3 = point3.get_y()
    x4 = point4.get_x()
    y4 = point4.get_y()

    # calculate the denominator
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    # if the denominator is 0, the lines are parallel
    if denominator == 0:
        return None

    # calculate the numerator
    numerator1 = x1 * y2 - y1 * x2
    numerator2 = x3 * y4 - y3 * x4

    # calculate the intersection point
    x = (numerator1 * (x3 - x4) - (x1 - x2) * numerator2) / denominator
    y = (numerator1 * (y3 - y4) - (y1 - y2) * numerator2) / denominator

    # return the intersection point
    return Point(x, y)


# distance function is a helper function for closestPairOfPoints found below
# testing requirements:
#     # distance(point1, point2) - Return the distance between the two points.
def distance(point1, point2):
    x1 = point1.get_x()
    y1 = point1.get_y()
    x2 = point2.get_x()
    y2 = point2.get_y()

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# closestPairOfPoints function
# testing requirements:
#     # closestPairOfPoints(points) - Return a tuple containing the two closest points in the given set of points.
def closestPairOfPoints(points):
    # initialize the closest points
    closestPoints = (points[0], points[1])

    # initialize the closest distance
    closestDistance = distance(closestPoints[0], closestPoints[1])

    # loop through the points
    for i in range(len(points)):
        # loop through the points again
        for j in range(i + 1, len(points)):
            # get the distance between the points
            distanceBetweenPoints = distance(points[i], points[j])

            # if the distance between the points is less than the closest distance
            if distanceBetweenPoints < closestDistance:
                # update the closest points
                closestPoints = (points[i], points[j])

                # update the closest distance
                closestDistance = distanceBetweenPoints

    # return the closest points
    return closestPoints


# convexHull function - monotone chain algorithm
# testing requirements:
#     # convexHull(points) - Return a list of points that form the convex hull of the given set of points.
def convexHull(points):
    # sort the points by x-coordinate
    points.sort(key=lambda point: point.get_x())

    # initialize the upper and lower hulls
    upperHull = []
    lowerHull = []

    # loop through the points
    for point in points:
        # while the upper hull has at least 2 points and the cross product of the last 2 points and the current point is less than or equal to 0
        while len(upperHull) >= 2 and crossProduct(upperHull[-2], upperHull[-1], point) <= 0:
            # remove the last point from the upper hull
            upperHull.pop()

        # append the current point to the upper hull
        upperHull.append(point)

    # loop through the points in reverse
    for point in reversed(points):
        # while the lower hull has at least 2 points and the cross product of the last 2 points and the current point is less than or equal to 0
        while len(lowerHull) >= 2 and crossProduct(lowerHull[-2], lowerHull[-1], point) <= 0:
            # remove the last point from the lower hull
            lowerHull.pop()

        # append the current point to the lower hull
        lowerHull.append(point)

    # remove the last point from the upper hull
    upperHull.pop()

    # remove the last point from the lower hull
    lowerHull.pop()

    # return the upper hull + lower hull
    return upperHull + lowerHull

# crossProduct function is a helper function for convexHull found above
# testing requirements:
#     # crossProduct(point1, point2, point3) - Return the cross product of the vectors formed by the given points.
def crossProduct(point1, point2, point3):
    # get the coordinates of the points
    x1 = point1.get_x()
    y1 = point1.get_y()
    x2 = point2.get_x()
    y2 = point2.get_y()
    x3 = point3.get_x()
    y3 = point3.get_y()

    # return the cross product
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def main():
    pass

    

    




if __name__ == "__main__":
    main()
