from help import Point, Rectangle


def generatePoints(n, m):
    points = []
    for i in range(m):
        points.append(Point(pow(3469 * i, 31) % (20 * n), pow(6089 * i, 31) % (20 * n)))
    return points


def generateRectangles(n):
    rectangles = []
    for i in range(n):
        rectangles.append(Rectangle(Point(10 * i, 10 * i), Point(10 * (2 * n - i), 10 * (2 * n - i))))
    return rectangles

