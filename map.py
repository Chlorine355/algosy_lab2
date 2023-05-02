from help import *


def map_prepare(rectangles):
    compressX, compressY = compress(rectangles)
    cmap = [[0 for _1 in range(len(compressX))] for _ in range(len(compressY))]
    for rect in rectangles:
        firstIndX = binsearch(compressX, rect.first.x)
        firstIndY = binsearch(compressY, rect.first.y)
        secondIndX = binsearch(compressX, rect.second.x + 1)
        secondIndY = binsearch(compressY, rect.second.y + 1)

        for i in range(firstIndY, secondIndY):
            for j in range(firstIndX, secondIndX):
                cmap[i][j] += 1

    return cmap, compressX, compressY


def map_algo(points, map, compressX, compressY):
    answer = [0 for _ in range(len(points))]

    for i in range(len(points)):
        posX = binsearch(compressX, points[i].x)
        posY = binsearch(compressY, points[i].y)

        if posX == -1 or posY == -1:
            answer[i] = 0
        else:
            answer[i] = map[posY][posX]
    return answer
