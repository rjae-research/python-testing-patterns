import sys
from io import StringIO, TextIOBase

import pytest

from patterns.use_custom_mocks.console import Console


def test_write_must_write_message():
    stream = StringIO()
    with MockConsole(stream) as console:
        console.write("42")
        assert "42" in stream.getvalue()


class MockConsole(Console):

    def __init__(self, stream: TextIOBase):
        self._stream = sys.stdout
        sys.stdout = stream

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.close()
        sys.stdout = self._stream
