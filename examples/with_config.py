import pretty_assert

# you can init config before using assert
pretty_assert.init(
    comment_message_color="red",
    comment_message_attrs=["bold"],
    other_message_color="blue",
    file_path_color="green",
    code_color="yellow",
    line_number_color="grey",
    exit=False,
    classic_eq=True,
    show_source_info=False,
)

some_number = 1
try:
    pretty_assert.assert_eq(some_number, 2, "some_number and 2 are not equal")
except AssertionError:
    print("AssertionError get!")

pretty_assert.init(
    exit=True,
)

# exit!
pretty_assert.assert_eq(some_number, 2, "some_number and 2 are not equal")
