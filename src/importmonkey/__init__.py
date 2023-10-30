#!/usr/bin/env python3

"""This is importmonkey. See the only function, add_path, for documentation."""

# Updating __version__ information:
#     * Format is <major>.<minor>.<patch>
#     * Never use leading or trailing zeroes in any of minor/major/patch.
#     * Increment more if an increment results in a leading or trailing zero.
#     * Incrementing major resets minor and patch to 0.
#     * Incrementing minor resets patch to 0.
#     * Incrementing patch does not affect other numbers.
#     * Never decrement a number except when resetting to zero like above.

__version__ = "0.0.3"
__all__ = ["add_path"]
__author__ = "Markus Hirsimäki"
__copyright__ = "This work is dedicated to public domain under The Unlicense."
__license__ = "The Unlicense (https://choosealicense.com/licenses/unlicense/)"

import sys
import inspect
import pathlib


def add_path(new_path, allow_backslashes=False):
    """Adds a new path to sys.path relative to the caller's file's directory.

    The basis for the relative path being added is the __file__ attribute of
    the caller. You can inspect the path by simply doing print(__file__). If
    new_path argument is an absolute path, the base path from __file__ is
    ignored.

    The path being added is returned so you can wrap the function call in
    print to help find the correct path to add: print(add_path(mypath)).

    Paths containing unicode characters are supported.

    Paths works differently in Windows and Unix-like systems. On Windows,
    the drive is not reset when the argument is a rooted relative path.
    (e.g., "\\foo").

    See pathlib documentation for details about how paths will work at
    https://docs.python.org/3/library/pathlib.html

    Example 1 (relative path):
        add_path("./../mydir")  # Add path from a sibling directory.
        add_path("../mydir")  # Same as above, current directory ./ is implied.
        import py_file_in_mydir  # Import works now.
        py_file_in_mydir.my_func()

    Example 2 (absolute path):
        add_path("/home/username/mydir")
        import py_file_in_mydir  # Import works now.
        py_file_in_mydir.my_func()

    Example 3 (Windows path. Note: Unix-like paths work on Windows.):
        add_path("C:\\Users\\myuser\\Desktop\\mydir", allow_backslashes=True)
        import py_file_in_mydir  # Import works now.
        py_file_in_mydir.my_func()

    Args:
        new_path (str): The path to be added, relative to the caller's file.
        allow_backslashes (bool, optional): Allow backslashes in path. Default
            is False. You should only use this if you are certain you need
            backslashes. Unix-style paths can and should be used on Windows.

    Returns:
        str: The path that was added to sys.path.

    Raises:
        TypeError: If new_path or allow_backslashes has wrong type.
        ValueError: If new_path does not resolve to a valid directory.
        ValueError: If new_path already exists in sys.path.
        FileNotFoundError: If the caller's filepath can not be determined.
        RuntimeError: For unexpected exceptions.
    """
    if type(new_path) is not str:
        msg = (
            "Was expecting the new_path argument to be a string."
            f" Found {repr(type(new_path))} instead."
        )
        raise TypeError(msg)
    if new_path == "":
        msg = (
            "Was expecting new path to be a non-empty string. Got empty string"
            " instead. Try using './' to refer to your file's directory for"
            " example."
        )
        raise ValueError(msg)
    if type(allow_backslashes) is not bool:
        msg = (
            "Was expecting the allow_backslashes argument to be a bool."
            f" Found {repr(type(allow_backslashes))} instead."
        )
        raise TypeError(msg)
    if "\\" in new_path and not allow_backslashes:  # "\\" is single \.
        msg = (
            "Found a backslash character in the path. Use forward slashes"
            " instead for compatibility with windows and Unix paths. If"
            " you are certain that backslashes are needed, set the"
            " argument allow_backslashes to True."
        )
        raise ValueError(msg)

    # Caller's frame is required to find the caller's filename and path
    # so that relative paths can be used as arguments for adding a path.
    try:
        caller_frame = inspect.currentframe().f_back
    except AttributeError:
        caller_frame = None
    if caller_frame is None:
        msg = (
            "Failed to find the caller's stack frame. Can not deduce"
            " caller's file path as a basis for path to be added. Is the"
            " function being used outside of a file or is a non-cPython"
            " interpreter being used?"
        )
        raise FileNotFoundError(msg)

    caller_file = inspect.getframeinfo(caller_frame).filename
    base_path = pathlib.Path(caller_file).parent.resolve()
    final_path = (base_path / pathlib.Path(new_path)).resolve()

    if not final_path.is_dir():
        msg = (
            f"The path given ({repr(str(final_path))}) points to something"
            " else than an existing directory. Try checking the spelling."
            " Relative paths start from the caller's file's directory."
        )
        raise ValueError(msg)

    final_path_str = str(final_path)

    if final_path_str not in sys.path:
        sys.path.append(final_path_str)
    else:
        msg = f"The path {repr(final_path_str)} is already found in sys.path."
        raise ValueError(msg)
    return final_path_str
