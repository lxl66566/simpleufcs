import cProfile
import pstats

from simpleufcs import UFCS


def ufcs():
    temp = UFCS([3, 2, 1]).sorted().map(lambda x: x * 2).filter(lambda x: x > 3).list()
    temp.append(4)
    temp.extend([5])
    return temp


def main():
    for _ in range(100000):
        ufcs()


cProfile.run("main()", "ufcs_stats.prof")

p = pstats.Stats("ufcs_stats.prof")
p.sort_stats("cumulative").print_stats()
