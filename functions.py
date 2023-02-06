from typing import Generator, Iterable, Any
from itertools import chain, combinations

import numpy as np
from numpy import int_
from numpy.typing import NDArray


def _power_set(iterable: Iterable[int]) -> chain[tuple[int, ...]]:
    """Generates powerset"""
    s = [*iterable]

    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def _ordered_intersection(
    primary: Iterable[Any], comp: Iterable[Any]
) -> Generator[Any, None, None]:
    """Gets intersection between iterables; preserving order of the primary one"""
    comp_set = set(comp)

    return (value for value in primary if value in comp_set)


def get_all_cliques(matrix: NDArray[int_]) -> list[list[tuple[int, ...]]]:
    """Gets all 2^n cliques"""

    m, n = matrix.shape

    i_power_set = [*_power_set(range(m))][1:]
    j_power_set = [*_power_set(range(n))][1:]

    return [
        [i_subset, j_subset]
        for i_subset in i_power_set
        for j_subset in j_power_set
        if np.all(matrix[i_subset, :][:, j_subset])
    ]


def get_maximal_cliques(cliques: list[list[tuple[int]]]) -> list[list[tuple[int, ...]]]:
    """Gets maximal cliques from a list of cliques"""
    maximal_cliques = cliques[:]
    for a in cliques:
        for b in cliques:
            if (
                set(a[0]).issubset(set(b[0]))
                and set(a[1]).issubset(set(b[1]))
                and a != b
            ):
                maximal_cliques.remove(a)
                break

    return maximal_cliques


def get_intersecting_cliques(
    cliques: list[list[tuple[int]]],
) -> list[list[tuple[int, ...]]]:
    """Get intersection between two cliques"""

    len_cliques = len(cliques)
    intersecting_cliques = [
        [
            tuple(_ordered_intersection(cliques[i][0], cliques[j][0])),
            tuple(_ordered_intersection(cliques[i][1], cliques[j][1])),
        ]
        for i in range(len_cliques)
        for j in range(len_cliques)
        if j > i
    ]

    return intersecting_cliques


def to_clique_notation(cliques: list) -> list[Any]:
    """Translates to mathematical notation by finding all pairs (and enumerating from 1 instead of 0)

    e.g. [[0,1],[0,3]] --> [11, 14, 21, 24]
    """

    maths_cliques = []
    for k in range(len(cliques)):
        clique = cliques[k]
        maths_cliques.append([])
        for i in range(len(clique[0])):
            for j in range(len(clique[1])):
                a = clique[0][i] + 1
                b = clique[1][j] + 1
                maths_cliques[k].append(int(str(a) + str(b)))

    return maths_cliques
