# test module

from pretty_assert import assert_eq

from .m import return_true


class MyClass:
    def a_very_long_function_name_that_makes_python_formatter_to_wrap_lines(self):
        return return_true


assert_eq(
    MyClass().a_very_long_function_name_that_makes_python_formatter_to_wrap_lines()(),
    False,
    "return_true is not False",
)
