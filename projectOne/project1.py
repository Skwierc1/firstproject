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
import copy

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
    #find points that have the lowest y value
    bottom_points = [points[0]]
    for i in points:
        if bottom_points[0].get_y() > i.get_y():
            bottom_points.clear()
            bottom_points.append(i)
        elif bottom_points[0].get_y() == i.get_y():
            bottom_points.append(i)
    #find the point that has the lowest x and y value
    bottom_left_point = bottom_points[0]
    for j in bottom_points:
        if bottom_left_point.get_x() > j.get_x():
            bottom_left_point = j

    #sort the points list
    #in order of angle respective to the bottom left point
    points.sort(key=lambda point: math.atan2((point.get_y()-bottom_left_point.get_y()),(point.get_x()-bottom_left_point.get_x())))       
   
    #list for convex hull points
    convexHullPoints = []

    #add the bottom left point to the convex hull points list
    convexHullPoints.append(points[0])

    # remove the bottom left point from the points list
    points.pop(0)
    

    
    for k in range(len(points)):
        nextp = points.pop(0)
        clockw = 1
        #while loop until finding the next point
        while clockw == 1:
            #orip -> origin point
            #prep -> previous point
            #nextp -> next point
            prep = convexHullPoints[-1]
            #if there is only one point in the convex hull point list
            #set the point as orip and prep
            if len(convexHullPoints) == 1:
                orip = convexHullPoints[-1]
            else:    
                orip = convexHullPoints[-2]
            #call crossProduct function
            clockw = crossProduct(orip,prep,nextp)
            #if clockwise -> remove the prep from the convex hull list
            if clockw == 1:
                convexHullPoints.pop()
        # if counter clockwise -> add the nextp to the convex hull list
        convexHullPoints.append(nextp)

    return convexHullPoints

def crossProduct(point1, point2, point3):
    # get the coordinates of the points
    x1 = point1.get_x()
    y1 = point1.get_y()
    x2 = point2.get_x()
    y2 = point2.get_y()
    x3 = point3.get_x()
    y3 = point3.get_y()

    # return the cross product
    ans =  (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    
    #clockwise
    if ans < 0:
        return 1
    #counterclockwise
    if ans > 0:
        return -1
    return -1

def largestEmptyCircle(circles):
    #create point list for center of circles
    pointlist = []
    for i in circles:
        pointlist.append(i.get_center())
    #deepcopy the pointlist for convexHull finc
    pointlisttemp= copy.deepcopy(pointlist)

    #get the convexHull point list
    convexHullList = convexHull(pointlisttemp)
    
    #get the circles that's in convex hull (excluding the circles with points that's in convex hull point list
    circle_in_c = [x for x in circles if x.get_center() not in convexHullList]
    
    #set circle and circle size as null first
    l_circle = None
    l_circle_r = 0
    for j in circle_in_c:
        include_p = False
        for k in pointlist:
            #if the point and the center of the circle is not the same
            if j.get_center() != k:  
                #if radius is smaller than the distance between the center and a point
                if (j.get_radius())> math.sqrt(((k.get_x() - j.get_center().get_x())**2) + ((k.get_y() - j.get_center().get_y())**2)):
                    include_p = True
        #if there is no point in the circle            
        if include_p == False:
            #if the circle is larger than any other circle, set the circle
            if l_circle_r < j.get_radius():
                l_circle = j

    return l_circle


#create list of points, lines, and circles for test
def create_test_obj():
    point1 = Point(3, 0)
    point2 = Point(5, 2)
    point3 = Point(4, 4)
    point4 = Point(1, 5)
    point5 = Point(0, 3)
    point6 = Point(2, 3)
    points = [point1, point2, point3, point4, point5, point6]
   
    lineSegment1 = LineSegment(point1, point2)
    lineSegment2 = LineSegment(point3, point4)
    lineSegment3 = LineSegment(point5, point6)
    lineSegments = [lineSegment1, lineSegment2, lineSegment3]


    circle1 = Circle(point1,4)
    circle2 = Circle(point2,3)
    circle3 = Circle(point3,2)
    circle4 = Circle(point4,3)
    circle5 = Circle(point5,3)
    circle6 = Circle(point6,1)
    circles = [circle1, circle2, circle3, circle4, circle5, circle6]

    #return list of points, lines, and circles
    return points, lineSegments, circles

#return string value of all the points, lines, and circles
def show_obj(points, lineSegments, circles):
    
    # get points's string value
    obj_list = "Points: "
    for i in points:
        obj_list += i.__repr__()
        obj_list += ", "
    obj_list = obj_list.rstrip(obj_list[-1]) 
    obj_list = obj_list.rstrip(obj_list[-1])

    # get lines's string value
    obj_list += "\nLines: "
    for i in lineSegments:
        obj_list += i.__repr__()
        obj_list += ", "
    obj_list = obj_list.rstrip(obj_list[-1]) 
    obj_list = obj_list.rstrip(obj_list[-1])

    #get circles's string value
    obj_list += "\nCircles: "
    for i in circles:
        obj_list += i.__repr__()
        obj_list += ", "
    obj_list = obj_list.rstrip(obj_list[-1]) 
    obj_list = obj_list.rstrip(obj_list[-1]) 
    obj_list += "\n"

    #return the string
    return obj_list


def main():
    test_points, test_lineSegments, test_Circles = create_test_obj()
    print(show_obj(test_points, test_lineSegments, test_Circles))


    

    




if __name__ == "__main__":
    main()
