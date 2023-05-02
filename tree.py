from help import Point, Rectangle, Node, Event
from help import compress, binsearch


def buildTree(arr, leftInd, rightInd):
    if leftInd + 1 == rightInd:
        return Node(arr[leftInd], None, None, leftInd, rightInd)
    mid = (leftInd + rightInd) // 2
    left = buildTree(arr, leftInd, mid)
    right = buildTree(arr, mid, rightInd)

    return Node(left.value + right.value, left, right, left.leftInd, right.rightInd)


def insert(node, begin, end, value):
    if begin <= node.leftInd and node.rightInd <= end:
        return Node(node.value + value, node.left, node.right, node.leftInd, node.rightInd)

    if node.rightInd <= begin or end <= node.leftInd:
        return node

    newNode = Node(node.value, node.left, node.right, node.leftInd, node.rightInd)
    newNode.left = insert(newNode.left, begin, end, value)
    newNode.right = insert(newNode.right, begin, end, value)
    return newNode


def buildPersistentSegmentTree(rectangles, compressX, compressY):
    if len(rectangles) == 0:
        return None
    events = [0 for _ in range(len(rectangles) * 2)]
    roots = [0 for _ in range(len(events))]

    ind = 0
    for rect in rectangles:
        events[ind] = Event(binsearch(compressX, rect.first.x),
                            binsearch(compressY, rect.first.y),
                            binsearch(compressY, rect.second.y ),
                            1)
        ind += 1
        events[ind] = Event(binsearch(compressX, rect.second.x ),
                            binsearch(compressY, rect.first.y),
                            binsearch(compressY, rect.second.y),
                            -1)
        ind += 1

    events.sort(key=lambda el: el.getX())

    root = buildTree([0 for _ in range(len(compressY))], 0, len(compressY))

    endX = events[0].x
    ind = 0
    for event in events:
        if endX != event.x:
            roots[ind] = root
            ind += 1
            endX = event.x
        root = insert(root, event.beginY, event.endY, event.status)
    return roots


def getAnswer(node, target):
    if node is not None:
        mid = (node.leftInd + node.rightInd) // 2
        if target < mid:
            return node.value + getAnswer(node.left, target)
        else:
            return node.value + getAnswer(node.right, target)
    return 0


def segtree(points, compressX, compressY, roots):
    answer = [0 for _ in range(len(points))]
    if not roots:
        return answer
    for i in range(len(points)):
        posX = binsearch(compressX, points[i].x)
        posY = binsearch(compressY, points[i].y)

        if posX == -1 or posY == -1:
            answer[i] = 0
        else:
            answer[i] = getAnswer(roots[posX], posY)
    return answer


def tree_prepare(points, rectangles):
    compressed = compress(rectangles)
    compressX = compressed[0]
    compressY = compressed[1]
    roots = buildPersistentSegmentTree(rectangles, compressX, compressY)
    return points, compressX, compressY, [x if x else None for x in roots]
