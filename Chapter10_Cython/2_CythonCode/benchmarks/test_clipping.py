from timeit import Timer

import numpy as np

import fastvector


v = fastvector.VectorND([np.random.random() for _ in range(100_000)])
a = np.array([np.random.random() for _ in range(100_000)])

num_repeats = 100
num_runs = 3

import_string = """
from __main__ import v, a
import fastvector
import numpy as np
"""

python_timer = Timer(
    "fastvector.python_clip_vector(v, -1, 1, v)", setup=import_string
)

naive_cython_timer = Timer(
    "fastvector.naive_cython_clip_vector(v, -1, 1, v)", setup=import_string
)

cython_timer = Timer(
    "fastvector.cython_clip_vector(v, -1, 1, v)", setup=import_string
)

np_timer = Timer("np.clip(a, -1, 1, a)", setup=import_string)


def main():
    python_mean_time = (
        np.mean(python_timer.repeat(repeat=num_repeats, number=num_runs))
        * 1000.0
    )
    print(f"fastvector.python_clip_vector: {python_mean_time}")

    naive_cython_mean_time = (
        np.mean(naive_cython_timer.repeat(repeat=num_repeats, number=num_runs))
        * 1000.0
    )
    print(f"fastvector.naive_cython_clip_vector: {naive_cython_mean_time}")

    cython_mean_time = (
        np.mean(cython_timer.repeat(repeat=num_repeats, number=num_runs))
        * 1000.0
    )
    print(f"fastvector.cython_clip_vector: {cython_mean_time}")

    np_mean_time = (
        np.mean(np_timer.repeat(repeat=num_repeats, number=num_runs)) * 1000.0
    )
    print(f"np.clip: {np_mean_time}")

    print(
        f"execution time speedup to python: {(python_mean_time / cython_mean_time):.2f}x"
    )
    print(
        f"execution time speedup to naive: {(naive_cython_mean_time / cython_mean_time):.2f}x"
    )
    print(
        f"execution time speedup to numpy: {(np_mean_time / cython_mean_time):.2f}x"
    )


if __name__ == "__main__":
    main()
