import os

import pytest

from anti_patterns.use_mocking_frameworks.file_utils import FileUtils


def test_delete_file_must_remove_file(mocker):
    mocker.patch("os.remove")
    remove = mocker.spy(os, "remove")
    FileUtils().delete_file("42")
    remove.assert_called_once_with("42")
