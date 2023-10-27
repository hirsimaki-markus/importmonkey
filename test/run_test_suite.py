#!/usr/bin/env python3

"""Test suite for importmonkey. Run this file to run all tests."""

import sys
import pathlib
import unittest


class TestImportmonkey(unittest.TestCase):
    """Simple test suite with unittest."""

    def test_non_str_path(self):
        """Non-str path argument should raise."""
        with self.assertRaises(TypeError) as e:
            add_path(123)
        err_text = (
            "Was expecting the new_path argument to be a string."
            " Found <class 'int'> instead."
        )
        self.assertEqual(str(e.exception), err_text)

    def test_empty_str_path(self):
        """Empty path argument string should raise."""
        with self.assertRaises(ValueError) as e:
            add_path("")
        err_text = (
            "Was expecting new path to be a non-empty string. Got empty string"
            " instead. Try using './' to refer to your file's directory for"
            " example."
        )
        self.assertEqual(str(e.exception), err_text)

    def test_non_bool_allow_backslashes(self):
        """Non-bool allow_backslashes argument should raise."""
        with self.assertRaises(TypeError) as e:
            add_path("./foo/bar/baz/qux/quux", allow_backslashes=123)
        err_text = (
            "Was expecting the allow_backslashes argument to be a bool."
            " Found <class 'int'> instead."
        )
        self.assertEqual(str(e.exception), err_text)

    def test_backslash_without_allowing(self):
        """Using backslashes in path without specifying allow should raise."""
        with self.assertRaises(ValueError) as e:
            add_path("\\foo\\bar\\baz\\qux\\quux")
        err_text = (
            "Found a backslash character in the path. Use forward slashes"
            " instead for compatibility with windows and Unix paths. If you"
            " are certain that backslashes are needed, set the argument"
            " allow_backslashes to True."
        )
        self.assertEqual(str(e.exception), err_text)

    def test_happypath_with_relative_path(self):
        """Try adding a relative path that surely exists."""
        # Slice part of path with -29 since the start might change
        added_path = add_path("./../src/importmonkey")[-29:]
        self.assertEqual(added_path, "importmonkey/src/importmonkey")

    def test_happypath_wih_absolute_path(self):
        """Try adding filesystem root.

        No assertion of path is done since it will depend on OS, but the call
        should never raise. This test assumes the file is not placed at root.
        """
        add_path("/")

    def test_bad_path(self):
        """Try adding a non-existing path."""
        with self.assertRaises(ValueError) as e:
            add_path("./../foobarbazquxquuxspurdospärdewololoo")
        err_text = (
            "The path given ('/home/telkka/repos/importmonkey/foobarbazqux"
            "quuxspurdospärdewololoo') points to something else than an"
            " existing directory. Try checking the spelling. Relative paths"
            " start from the caller's file's directory."
        )
        # Slice last 100 characters since they should always be same. Path
        # could change depending on machine.
        self.assertEqual(str(e.exception)[-100:], err_text[-100:])

    def test_already_found_in_sys_path(self):
        """Should raise if path argument is already found in sys.path

        This test tries to add it's containing folder which is already in path
        since this file is running as main.
        """
        with self.assertRaises(ValueError) as e:
            add_path("./../test")
        err_text = (
            "The path '/home/username/git_repos/importmonkey/test' is already"
            " found in sys.path."
        )
        # Slice error texts with :9 from start and -29:-1 from end
        # since path will wary depending on machine.
        self.assertEqual(str(e.exception)[:9], err_text[:9])
        self.assertEqual(str(e.exception)[-29:-1], err_text[-29:-1])


if __name__ == "__main__":
    # Importmonkey can be used to add path to sys.path but it must itself be
    # loaded first so we do the sys.path stuff manually here. A project using
    # importmonkey would use the add_path function instead of the below line.
    sys.path.append(str(pathlib.Path(__file__, "./../../src").resolve()))
    from importmonkey import add_path

    # buffer=False to avoid capturing prints by tests in case of debugging.
    unittest.main(testRunner=unittest.TextTestRunner(buffer=False))
else:
    raise RuntimeError("Testing paths requires this file to run as main.")
