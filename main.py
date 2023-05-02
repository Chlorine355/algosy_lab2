from time import perf_counter_ns

from tree import *
from bruteforce import *
from map import *
from generate import *


bruteTime = []
mapPrepTime = []
treePrepTime = []
mapTime = []
treeTime = []

count = 2 ** 12
n = 14
for i in range(n):
    rectangles = generateRectangles(count)
    points = generatePoints(count, 100000)

    t1 = perf_counter_ns()
    bruteforce_algo(points, rectangles)
    bruteTime.append(perf_counter_ns() - t1)

    t1 = perf_counter_ns()
    args = map_prepare(rectangles)
    mapPrepTime.append(perf_counter_ns() - t1)

    t1 = perf_counter_ns()
    map_algo(points, *args)
    mapTime.append(perf_counter_ns() - t1)

    t1 = perf_counter_ns()
    args = tree_prepare(points, rectangles)
    treePrepTime.append(perf_counter_ns() - t1)

    t1 = perf_counter_ns()
    segtree(*args)
    treeTime.append(perf_counter_ns() - t1)


    print(count, "Bruteforce time:", bruteTime)
    print(count, "Map prep time:", mapPrepTime)
    print(count, "Maptime time:", mapTime)
    print(count, "Tree prep time:", treePrepTime)
    print(count, "Tree time:", treeTime)
    print("---------------------------------------------------")




