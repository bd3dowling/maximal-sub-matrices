from numpy import array
from main import main


def test_main() -> None:
    matrix = array(
        [
            [1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 1],
        ]
    )
    expected_maximal_cliques = [
        [21, 22, 23, 28],
        [31, 32, 33, 34],
        [41, 45],
        [51, 56, 57],
        [86, 87, 89],
        [21, 22, 23, 31, 32, 33],
        [45, 65],
        [56, 57, 86, 87],
        [11, 12, 21, 22, 31, 32],
        [56, 76, 86],
        [11, 21, 31, 41, 51],
    ]
    expected_maximal_intersecting_cliques = [
        [21, 22, 23],
        [31, 32, 33],
        [45],
        [41],
        [56, 57],
        [51],
        [86, 87],
        [21, 22, 31, 32],
        [56, 86],
        [11, 21, 31],
    ]

    actual_maximal_cliques, actual_maximal_intersecting_cliques = main(matrix)

    assert actual_maximal_cliques == expected_maximal_cliques
    assert actual_maximal_intersecting_cliques == expected_maximal_intersecting_cliques
