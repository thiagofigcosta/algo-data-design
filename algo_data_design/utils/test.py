STATEFUL_TEST_KWARGS = {}


def call(callable_function, **mocked_custom_kwargs):
    # This function is a lambda wrapper that serves to call a mocked function with joined arguments from the original
    # function to be mocked alongside with custom keyword arguments.
    # It should be used as side_effect of unittest.mock.patch
    return lambda *args, **kwargs: callable_function(*args, **kwargs, **mocked_custom_kwargs, **STATEFUL_TEST_KWARGS)


def set_global_mocked_kwargs(**mocked_custom_kwargs):
    STATEFUL_TEST_KWARGS.update(mocked_custom_kwargs)


def clear_global_mocked_kwargs():
    STATEFUL_TEST_KWARGS.clear()
