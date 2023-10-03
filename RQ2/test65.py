import pytest
from problem65 import code65
def test1():
        s = "0"
        assert code65(s) == True

def test2():
        s = "e"
        assert code65(s) == False
def test3():
        s = ""
        assert code65(s) == False
def test4():
        s = "."
        assert code65(s) == False

def test5():
        s = "123"
        assert code65(s) == True
#partitions with exponentials
def test6():
        s = "123e45"
        assert code65(s) == True

def test7():
        s = "0.123"
        assert code65(s) == True
def test8():
        s = "0.12.3"
        assert code65(s) == False
