from pretty_assert import assert_eq

a = {"a": 1, "b": 4}

b = {"b": 2, "a": 1000, "c": 3}

assert_eq(a, b, "a and b are not equal")
