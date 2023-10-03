import pytest
from problem32 import code32
def test1():
        s = "(()"
        assert code32(s) == 2

def test2():
        s = ")()())"
        assert code32(s) == 4
def test3():
        s = ""
        assert code32(s) == 0
def test4():
        s = "(((((("
        assert code32(s) == 0
def test4b():
        s =  "))))))"
        assert code32(s) == 0
def test5():
        s = "(()())"
        assert code32(s) == 6
def test6():
        s = "())(()"
        assert code32(s) == 2
def test7():
        s = "(())())(()"
        assert code32(s) == 6
