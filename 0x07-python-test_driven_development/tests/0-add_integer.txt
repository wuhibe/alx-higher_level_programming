=============================
The ``0-add_integer`` module
=============================

Using ``add_integer``
---------------------

Import the function:

    >>> add_integer = __import__('0-add_integer').add_integer

Now test it:

Tests for Positive Numbers.

    >>> add_integer(2, 7)
    9

    >>> add_integer(1, 9)
    10

    >>> add_integer(26, 24)
    50

    >>> add_integer(12, 3)
    15

    >>> add_integer(2, 1)
    3

Tests for Negative Numbers.

    >>> add_integer(-2, -7)
    -9

    >>> add_integer(-1, -9)
    -10

    >>> add_integer(-26, -24)
    -50

    >>> add_integer(-12, -3)
    -15

    >>> add_integer(-2, -1)
    -3

Tests for positive Floats.

    >>> add_integer(2.1, 7.2)
    9

    >>> add_integer(1.3, 9.5)
    10

    >>> add_integer(26.2, 24.6)
    50

    >>> add_integer(12.6, 3.9)
    15

    >>> add_integer(2.3, 1.1)
    3

Tests for Negative Floats.

    >>> add_integer(-2.3, -7.1)
    -9

    >>> add_integer(-1.2, -9.4)
    -10

    >>> add_integer(-26.5, -24.6)
    -50

    >>> add_integer(-12.5, -3.1)
    -15

    >>> add_integer(-2.7, -1.2)
    -3

Test just one Argument.

    >>> add_integer(1)
    99

    >>> add_integer(2)
    100

    >>> add_integer(3)
    101

    >>> add_integer(4)
    102

    >>> add_integer(5)
    103

test Error Cases.

    >>> add_integer(True, False)
    Traceback (most recent call last):
    TypeError: a must be an integer

    >>> add_integer(2, float("inf"))
    Traceback (most recent call last):
    OverflowError: cannot convert float infinity to integer

    >>> add_integer(5, float("nan"))
    Traceback (most recent call last):
    ValueError: cannot convert float NaN to integer

    >>> add_integer()
    Traceback (most recent call last):
    TypeError: add_integer() missing 1 required positional argument: 'a'

    >>> add_integer(2, "School")
    Traceback (most recent call last):
    TypeError: b must be an integer

    >>> add_integer("Hello", "World")
    Traceback (most recent call last):
    TypeError: a must be an integer

    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer
