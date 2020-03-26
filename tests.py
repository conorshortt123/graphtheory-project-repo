# Conor Shortt
# Run tests on regex program.

import regex

if __name__ == "__main__":
    tests = [
        ["a.b|b*", "bbbbb", True],
        ["a.b|b*", "bbx", False],
        ["a.b", "abbbb", False],
        ["b**", "b", True],
        ["b*", "", True],
        ["b+", "bbbb", True],
        ["a.b", "ab", True],
        ["a?", "a", True],
        ["a?", "aaa", False]
    ]

    for test in tests:
        assert regex.match(test[0], test[1]) == test[2], test[0] + \
        (" should match " if test[2] else " should not match ") + test[1]