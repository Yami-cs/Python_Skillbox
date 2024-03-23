class BlockErrors:
    def __init__(self, error_types):
        self.error_types = error_types

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            if issubclass(exc_type, self.error_types):
                return True
            else:
                raise exc_value
        return False

# Test cases
def test_block_errors():
    # Test when error is ignored
    with BlockErrors({ZeroDivisionError, TypeError}):
        a = 1 / 0

    # Test when error is propagated
    try:
        with BlockErrors({ZeroDivisionError}):
            a = 1 / '0'
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")

    # Test nested blocks
    outer_err_types = {TypeError}
    with BlockErrors(outer_err_types):
        inner_err_types = {ZeroDivisionError}
        with BlockErrors(inner_err_types):
            a = 1 / '0'
        print('Inner block: executed without errors')
    print('Outer block: executed without errors')

    # Test ignoring all exceptions
    with BlockErrors({Exception}):
        a = 1 / '0'

if __name__ == '__main__':
    test_block_errors()
