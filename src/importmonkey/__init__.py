#!/usr/bin/env python3

"""This is importmonkey. See the only function, add_path, for documentation."""

import inspect
import pathlib
import sys

# __version__ is single source of truth for packaging; <major>.<minor>.<patch> is used.
# Trailing/leading zeroes are not allowed. Lone zeroes (such as in 0.1.0) are allowed.
# When incrementing any of major, minor, patch, reset other numbers after it to zero.
# A number with trailing zero is skipped (eg. 0.10.0) and incremented more (eg. 0.11.0).
__version__ = "2.1.0"
__all__ = ["add_path"]
__author__ = "Markus Hirsimäki"
__copyright__ = "This work is dedicated to public domain under The Unlicense."
__license__ = "The Unlicense (https://choosealicense.com/licenses/unlicense/)"


def add_path(new_path, allow_backslashes=False):
    """Adds a new path to sys.path. Relative paths use the caller's directory as base.

    The caller's __file__ attribute is used to get base directory for relative paths.
    If caller's __file__ is not available, current working directory is used. These can
    be inspected with "print(__file__)" and "print(os.getcwd())". If the new_path
    argument is an absolute path, the base path is ignored.

    The path being added is returned so that it may be can wrapped with print to help
    find the correct path to add like so: "print(add_path(mypath))".

    Paths containing unicode characters are supported. Paths works differently in
    Windows and Unix-like systems. On Windows, the drive is not reset when the argument
    is a rooted relative path (e.g., "\\foo").

    For more details, see pathlib (https://docs.python.org/3/library/pathlib.html).

    Example, relative path:
        add_path("./../mydir")  # Add path from a sibling directory.
        add_path("../mydir")  # Same as above, current directory ./ is implied.
        import py_file_in_mydir  # Import works now.
        py_file_in_mydir.my_func()

    Example, absolute path:
        add_path("/home/username/mydir")
        import py_file_in_mydir  # Import works now.
        py_file_in_mydir.my_func()

    Example, Windows path (note: Unix-like paths work on Windows):
        add_path("C:\\Users\\myuser\\Desktop\\mydir", allow_backslashes=True)
        import py_file_in_mydir  # Import works now.
        py_file_in_mydir.my_func()

    Args:
        new_path (str): The path to be added.
        allow_backslashes=False (bool): Allow backslashes in path. Only use this if you
            are certain you need backslashes. Unix-style paths work on Windows.

    Returns:
        str: The resolved path which was added to sys.path or and empty string if the
            given path was already in sys.path.

    Raises:
        TypeError: If new_path or allow_backslashes has wrong type.
        ValueError: If new_path does not resolve to a valid directory.
        FileNotFoundError: If the caller's filepath can not be determined.
        RuntimeError: For unexpected exceptions.
    """
    if type(new_path) is not str or new_path == "":
        raise ValueError("new_path must be non-empty string. Try print(add_path('.')).")
    if type(allow_backslashes) is not bool:
        raise TypeError(f"allow_backslashes must be bool, not {type(new_path)}.")
    if "\\" in new_path and not allow_backslashes:  # "\\" is single backslash.
        raise ValueError("Found backslash in new_path but allow_backslashes was False.")

    try:  # Using caller's frame to get caller's __file__ as a base for relative path.
        caller_file = inspect.currentframe().f_globals["__file__"]
    except Exception:  # Can't find frame or __file__ not set. Use current working dir.
        caller_file = str(pathlib.Path(".").resolve())

    path_to_add = (pathlib.Path(caller_file).parent / new_path).resolve()

    if not path_to_add.is_dir():
        raise ValueError(f"{str(path_to_add)} is not an existing directory.")

    if str(path_to_add) not in sys.path:
        sys.path.append(str(path_to_add))
        return str(path_to_add)
    else:
        return ""
