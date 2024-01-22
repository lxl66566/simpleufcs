# simpleufcs

A simple ~~(and ugly)~~ Uniform Function Call Syntax (UFCS) implementation in python.

## Usage

Installation:

```sh
pip install simpleufcs
```

Usage:

```py
from simpleufcs import UFCS
UFCS([3, 2, 1]).sorted(key=lambda x: x <= 1).map(lambda x: x * 2).list().print()
```

## benchmark

In the [benchmark](./benchmark.py), the UFCS implementation is 3-8 times slower than the built-in method.

Windows, python 3.12

| bench | ufcs                | builtin              |
| ----- | ------------------- | -------------------- |
| 1     | 0.02407699999457691 | 0.006241800001589581 |

Linux, python 3.11.6

| bench | ufcs               | builtin              |
| ----- | ------------------ | -------------------- |
| 1     | 0.0327424000006431 | 0.004318577999583795 |
