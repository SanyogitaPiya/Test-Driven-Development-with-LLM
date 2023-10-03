import pytest
from problem273 import code273
def test1():
        s = 123
        assert code273(s) == "One Hundred Twenty Three"

def test2():
        s = 12345
        assert code273(s) == "Twelve Thousand Three Hundred Forty Five"
def test3():
        s = 1234567
        assert code273(s) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"