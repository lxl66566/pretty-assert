from pretty_assert import (
    assert_,
    assert_eq,
    assert_ge,
    assert_gt,
    assert_in,
    assert_le,
    assert_lt,
    assert_ne,
    assert_not_in,
)

some_bool = True
some_number = 1
assert_(some_bool)  # you can assert without comment
assert_(some_bool, "some_bool is not True")
assert_eq(some_number, 1, "some_number is not 1")
assert_ne(some_number, 2, "some_number is 1")
assert_gt(some_number, 0, "some_number is not greater than 0")
assert_lt(some_number, 2, "some_number is not less than 2")
assert_ge(some_number, 1, "some_number is not greater than or equal to 1")
assert_le(some_number, 1, "some_number is greater than or equal to 1")
assert_in(some_number, [1, 2], "some_number is not in [1, 2]")
assert_not_in(some_number, [2, 3], "some_number is in [2, 3]")
