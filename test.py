from simpleufcs import UFCS

# basic chain (print test)
(
    UFCS([3, 2, 1])
    .sorted(key=lambda x: x <= 1)
    .map(lambda x: x * 2)
    .filter(lambda x: x > 3)
    .list()
    .print()
)

# filter, map, sorted
assert (
    UFCS([3, 2, 1])
    .map(lambda x: x * 2)
    .sorted(key=lambda x: x <= 3)
    .filter(lambda x: x > 3)
    .sorted()
    .list()
) == [4, 6]

# other list functions
temp = UFCS([3, 2, 1])
temp.append(4)
temp.extend([5, 6])
assert temp.sorted() == [1, 2, 3, 4, 5, 6]

# dict
assert (
    UFCS({"a": 1, "b": 2, "c": 3}.items()).filter(lambda pair: pair[1] > 2).dict()
) == dict(filter(lambda pair: pair[1] > 2, {"a": 1, "b": 2, "c": 3}.items()))
