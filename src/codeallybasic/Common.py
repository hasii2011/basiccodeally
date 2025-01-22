
#
# https://www.codetable.net/hex/a
#
XML_END_OF_LINE_MARKER: str = '&#xA;'


def cmp(left, right):
    """
    Python 2 stand in

    Args:
        left:
        right:

    Returns:
        -1 if left < right

        0 if left = right

        1 if left > right
    """
    return (left > right) - (left < right)


def apply(callback, args=None, kwargs=None):
    """
    Python 2 stand in

    Stolen from:  https://github.com/stefanholek/apply

    Call a callable object with positional arguments taken from the
    tuple args, and keyword arguments taken from the optional dictionary
    kwargs; return its results.
    """
    if args is None:
        args = ()
    if kwargs is None:
        kwargs = {}
    return callback(*args, **kwargs)
