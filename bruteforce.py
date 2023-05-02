from help import Point, Rectangle


def contains(rect, p):
    return rect.first.x <= p.x < rect.second.x and rect.first.y <= p.y < rect.second.y


def bruteforce_algo(points, rectangles):
    result = []
    for point in points:
        k = 0
        for rect in rectangles:
            if contains(rect, point):
                k += 1
        result.append(k)
    return result
