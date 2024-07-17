#!/usr/bin/env python3

"""Test suite for importmonkey. Run this file to run all tests."""

import sys
import unittest

import importmonkey


class TestImportmonkey(unittest.TestCase):
    """Simple test suite with unittest."""

    def test_empty_str_path(self):
        """Empty path argument string should raise."""
        with self.assertRaises(ValueError) as e:
            importmonkey.add_path("")
        err_text = "new_path must be non-empty string. Try print(add_path('.'))."
        self.assertEqual(str(e.exception), err_text)

    def test_non_bool_allow_backslashes(self):
        """Non-bool allow_backslashes argument should raise."""
        with self.assertRaises(TypeError) as e:
            importmonkey.add_path("./foo/bar/baz/qux/quux", allow_backslashes=123)
        err_text = "allow_backslashes must be bool, not <class 'str'>."
        self.assertEqual(str(e.exception), err_text)

    def test_backslash_without_allowing(self):
        """Using backslashes in path without specifying allow should raise."""
        with self.assertRaises(ValueError) as e:
            importmonkey.add_path("\\foo\\bar\\baz\\qux\\quux")
        err_text = "Found backslash in new_path but allow_backslashes was False."
        self.assertEqual(str(e.exception), err_text)

    def test_bad_path(self):
        """Try adding a relative path that surely exists."""
        # Slice part of path with -29 since the start might change
        with self.assertRaises(ValueError) as e:
            importmonkey.add_path("./../foobarbazquxquuxspurdospärdewololoo")
        assert str(e.exception).endswith(" is not an existing directory.")

    def test_happypath_wih_absolute_path(self):
        """Try adding filesystem root.

        No assertion of path is done since it will depend on OS, but the call
        should never raise. This test assumes the file is not placed at root.
        """
        importmonkey.add_path("/")

    def test_already_found_in_sys_path(self):
        """Empty string should be returned when path is already added."""
        self.assertEqual(importmonkey.add_path(sys.path[-1]), "")

if __name__ == "__main__":
    unittest.main(testRunner=unittest.TextTestRunner())
else:
    raise RuntimeError("Testing paths requires this file to run as main.")
