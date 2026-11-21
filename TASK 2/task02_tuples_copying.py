"""Q2: Tuples, mutability, aliasing and copying."""
import copy
import sys
import timeit

def make_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def demonstrate():
    bus_stops = {
        ("12.9716", "77.5946"): "Central Station",
        ("13.0358", "77.5970"): "City Market",
    }
    print("Tuple-key lookup:", bus_stops[("12.9716", "77.5946")])

    original = [[1, 2], [3, 4]]
    alias = original
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    original[0][0] = 99
    print("Aliased value:", alias[0][0])
    print("Shallow nested value:", shallow[0][0])
    print("Deep nested value:", deep[0][0])

    bad_grid = [[0] * 3] * 3
    good_grid = make_grid(3, 3)
    bad_grid[0][0] = 1
    good_grid[0][0] = 1
    print("Aliased grid:", bad_grid)
    print("Independent grid:", good_grid)
    for stop, name in bus_stops.items():
        print("Stop:", stop, "Name:", name)

if __name__ == "__main__":
    demonstrate()
    values = list(range(10000))
    tuple_values = tuple(values)
    print("List shallow size:", sys.getsizeof(values), "bytes")
    print("Tuple shallow size:", sys.getsizeof(tuple_values), "bytes")
    print("List indexing seconds:", timeit.timeit("x[5000]", globals={"x": values}, number=100000))
    print("Tuple indexing seconds:", timeit.timeit("x[5000]", globals={"x": tuple_values}, number=100000))
