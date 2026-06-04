"""Unit tests for Algorithms and Data Structures 1 AI - String Search (KMP)."""
import sys

import pytest

from kmp import (
    kmp_failure_table, kmp_search
)


#! TUTORS:
# Ensure that the search algorithms are actually implemented (and not some other algorithm).
# Specifically:
# * Look out for usages of str.find and str.index (which are strictly forbidden!)
# * Check that Rabin-Karp/Kmp aren't just reused for the other method
# * Check that there's no brute-force search implemented


try:
    from conftest import points  # type: ignore
except ImportError:

    def points(points: float):
        return lambda function: function

@points(0)
def test_python_version():
    assert sys.version_info >= (3, 13), \
        f"Python version is too low. Required >=3.13, your version: {sys.version_info.major}.{sys.version_info.minor}"

@points(0.5)
def test_kmp_failure_table():
    str_pattern = "ababac"
    failure_table = kmp_failure_table(str_pattern)
    expected_table = [
        0, 0, 1, 2, 3, 0
    ]
    assert failure_table == expected_table

@points(1)
def test_kmp_failure_table_long():
    str_pattern = "bbbscbabbabbbbfnbb"
    failure_table = kmp_failure_table(str_pattern)
    expected_table = [
        0, 1, 2, 0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 3, 0, 0, 1, 2
    ]
    assert failure_table == expected_table

@points(0.5)
def test_kmp_search_failures():
    with pytest.raises(TypeError):
        kmp_search("aaa", None) # type: ignore
    with pytest.raises(TypeError):
        kmp_search(3, "sdf") # type: ignore
    with pytest.raises(ValueError):
        kmp_search("", "asdf")
    with pytest.raises(ValueError):
        kmp_search("a", "")
    
@points(0.5)
def test_kmp_search_short():
    res = kmp_search("xxx", "abcdexxxunbxxxxke")

    assert len(res) == 3, f"expected the pattern to be found 3 times but was found {len(res)} times"
    assert res == [5, 11, 12]

@points(0.5)
def test_kmp_search_long():
    res = kmp_search("is", (
        "Compares two strings lexicographically. The comparison is based on the Unicode value of "
        "each character in the strings. The character sequence represented by this String object "
        "is compared lexicographically to the character sequence represented by the argument "
        "string. The result is a negative integer if this String object lexicographically "
        "precedes the argument string. The result is a positive integer if this String object "
        "lexicographically follows the argument string. The result is zero if the strings are "
        "equal; compareTo returns 0 exactly when the equals(Object) method would return true."
    ))
    assert len(res) == 9, f"expected the pattern to be found 9 times but was found {len(res)} times"
    assert res == [50, 55, 159, 176, 279, 306, 382, 409, 484]

@points(1)
def test_kmp_special():
    res = kmp_search("xxx", "xxxxxA")
    assert len(res) == 3, f"expected the pattern to be found 3 times but was found {len(res)} times"
    assert res == [0, 1, 2]

points(1)
def test_kmp_special1():
    res = kmp_search("xxx", "xxxXfl, xxxxA")
    assert len(res) == 3, f"expected the pattern to be found 3 times but was found {len(res)} times"
    assert res == [0, 8, 9]

@points(1)
def test_kmp_special2():
    res = kmp_search("xyxy", "xXyxyxyfl, xyxxyxyA")
    assert len(res) == 2, f"expected the pattern to be found 2 times but was found {len(res)} times"
    assert res == [3, 14]

@points(1)
def test_kmp_long_pattern():
    res = kmp_search(
        "ijK lmnopq", 
        "abcdefghijK lmnopqrstuvwxyz, abcdefghijK lmnopqrstuvwxyz.ijk lmnopqr"
    )
    assert len(res) == 2, f"expected the pattern to be found 2 times but was found {len(res)} times"
    assert res == [8, 37]

@points(1)
def test_kmp_very_long_text():
    res = kmp_search("Lorem ips", VERY_LONG_TEXT)
    assert len(res) == 52, \
        f"expected the pattern to be found 52 times but was found {len(res)} times"
    assert res == [
        0, 268, 296, 564, 592, 860, 1159, 1826, 2345, 2373, 2641, 2669, 2937, 2965, 3342, 3370,
        3638, 3666, 3931, 4199, 4227, 4495, 4523, 4791, 5090, 5757, 6019, 6287, 6315, 6583, 6611,
        6879, 7178, 7845, 8364, 8392, 8660, 8688, 8956, 8984, 9361, 9389, 9657, 9685, 9950, 10218,
        10246, 10514, 10542, 10810, 11109, 11776
    ]

VERY_LONG_TEXT = (
    "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore "
    "et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea "
    "rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum "
    "dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore "
    "magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet "
    "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, "
    "consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam "
    "erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd "
    "gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in "
    "hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero "
    "eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te "
    "feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh "
    "euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis "
    "nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem "
    "vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat "
    "nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril "
    "delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option "
    "congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet, "
    "consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam "
    "erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis "
    "nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit "
    "esse molestie consequat, vel illum dolore eu feugiat nulla facilisis. At vero eos et accusam et justo duo "
    "dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. "
    "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore "
    "et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea "
    "rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum "
    "dolor sit amet, consetetur sadipscing elitr, At accusam aliquyam diam diam dolore dolores duo eirmod eos "
    "erat, et nonumy sed tempor et et invidunt justo labore Stet clita ea et gubergren, kasd magna no rebum. "
    "sanctus sea sed takimata ut vero voluptua. est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, "
    "consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam "
    "erat. Consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna "
    "aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita "
    "kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, "
    "consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam "
    "erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd "
    "gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur "
    "sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed "
    "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea "
    "takimata sanctus. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor "
    "invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo "
    "dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. "
    "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore "
    "et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea "
    "rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum "
    "dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore "
    "magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet "
    "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure "
    "dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla "
    "facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit "
    "augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, "
    "sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad "
    "minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo "
    "consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel "
    "illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit "
    "praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta "
    "nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem "
    "ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet "
    "dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper "
    "suscipit lobortis nisl ut aliquip ex ea commodo Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
    "sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At "
    "vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus "
    "est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy "
    "eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam "
    "et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum "
    "dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor "
    "invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo "
    "dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. "
    "Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore "
    "eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum "
    "zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer "
    "adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. "
    "Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex "
    "ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie "
    "consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim "
    "qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor "
    "cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. "
    "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut "
    "laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation "
    "ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in "
    "hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis. At "
    "vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus "
    "est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy "
    "eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam "
    "et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum "
    "dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, At accusam aliquyam diam diam "
    "dolore dolores duo eirmod eos erat, et nonumy sed tempor et et invidunt justo labore Stet clita ea et "
    "gubergren, kasd magna no rebum. sanctus sea sed takimata ut vero voluptua. est Lorem ipsum dolor sit "
    "amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut "
    "labore et dolore magna aliquyam erat. Consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt "
    "ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores "
    "et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem "
    "ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et "
    "dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. "
    "Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit "
    "amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna "
    "aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita "
    "kasd gubergren, no sea takimata sanctus. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed "
    "diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero "
    "eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est "
    "Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy "
    "eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam "
    "et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum "
    "dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor "
    "invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo "
    "dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. "
    "Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore "
    "eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum "
    "zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer "
    "adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. "
    "Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex "
    "ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie "
    "consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim "
    "qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor "
    "cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. "
    "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut "
    "laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation "
    "ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo."
)

if __name__ == "__main__":
    try:
        import pytest_timeout

        pytest_timeout_installed = True
        del sys.modules["pytest_timeout"]
    except ModuleNotFoundError:
        print(
            "Consider installing pytest-timeout to execute all tests even if some test hangs."
        )
        pytest_timeout_installed = False

    if pytest_timeout_installed:
        pytest.main([__file__, "-rA", "--timeout=2"])
    else:
        pytest.main([__file__, "-rA"])
