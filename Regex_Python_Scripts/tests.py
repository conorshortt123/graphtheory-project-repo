# Conor Shortt
# Run tests on regex program.

import regex

def test():

    tests = [
        # Concatenation tests
        [
            ["a.b", "ab", True],
            ["a.b.c", "ab", False],
            ["b.c", "bc", True],
            ["c.a", "ca", True],
            ["a.c", "a", False]
        ],
        # OR operator tests
        [
            ["a.b|b", "ab", True],
            ["a.b.c|z", "ab", False],
            ["b.c|b.a", "bc", True],
            ["c.a|a.c", "ac", True],
            ["a.c|b", "a", False]
        ],
        # Plus operator tests
        [
            ["a.b+", "abbbbb", True],
            ["b+", "bbbbbx", False],
            ["a|b+", "bbbb", True],
            ["a?.b+", "b", True],
            ["a.c+", "accccc", True]
        ],
        # Question mark operator tests
        [
            ["a?.b", "ab", True],
            ["c?", "cx", False],
            ["b.a?", "ba", True],
            ["a?.b+", "a", False],
            ["a.c?", "ac", True]
        ],
        # Kleene star tests
        [
            ["a*.b", "aaaaaab", True],
            ["c*", "ccccx", False],
            ["b.a*", "baaaa", True],
            ["a*.b", "aaa", False],
            ["a+.c*", "aaaaaccccc", True],
            ["a.b|b*", "abbbbx", False],
            ["b**", "b", True]
        ]
    
    ]

    for testArray in tests:
        for test in testArray:
            assert regex.match(test[0], test[1]) == test[2], test[0] + \
            (" should match " if test[2] else " should not match ") + test[1]