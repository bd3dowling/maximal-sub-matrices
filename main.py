from numpy import int_
from numpy.typing import NDArray

from functions import (
    get_all_cliques,
    get_maximal_cliques,
    get_intersecting_cliques,
    to_clique_notation,
)


def main(matrix: NDArray[int_]) -> tuple[list[int], list[int]]:
    cliques = get_all_cliques(matrix)
    maximal_cliques = get_maximal_cliques(cliques)
    intersecting_cliques = get_intersecting_cliques(maximal_cliques)
    maximal_intersecting_cliques = get_maximal_cliques(intersecting_cliques)

    return (
        to_clique_notation(maximal_cliques),
        to_clique_notation(maximal_intersecting_cliques),
    )
