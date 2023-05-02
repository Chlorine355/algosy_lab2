class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Rectangle:
    def __init__(self, first: Point, second: Point):
        self.first = first
        self.second = second

    def __repr__(self):
        return f"[{self.first}, {self.second}]"


class Node:
    def __init__(self, value, left, right, leftInd, rightInd):
        self.value = value
        self.left = left
        self.right = right
        self.leftInd = leftInd
        self.rightInd = rightInd


class Event:
    def __init__(self, x, beginY, endY, status):
        self.x = x
        self.beginY = beginY
        self.endY = endY
        self.status = status

    def getX(self):
        return self.x


def binsearch(arr, value):
    left = 0
    right = len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > value:
            right = mid
        else:
            left = mid + 1
    return left - 1


def compress(rectangles: [Rectangle]):
    compressX, compressY = set(), set()
    for rect in rectangles:
        compressX.add(rect.first.x)
        compressY.add(rect.first.y)

        compressX.add(rect.second.x)
        compressY.add(rect.second.y)
    return sorted(list(compressX)), sorted(list(compressY))