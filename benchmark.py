from timeit import timeit

from simpleufcs import UFCS

print("benchmark 1")


def ufcs():
    temp = UFCS([3, 2, 1]).sorted().map(lambda x: x * 2).filter(lambda x: x > 3).list()
    temp.append(4)
    temp.extend([5])
    return temp


def normal():
    temp = list(filter(lambda x: x > 3, map(lambda x: x * 2, sorted([3, 2, 1]))))
    temp.append(4)
    temp.extend([5])
    return temp


print("ufcs: ", timeit("ufcs()", globals=globals(), number=10000))
print("normal: ", timeit("normal()", globals=globals(), number=10000))
