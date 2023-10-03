import pytest
from problem1787 import code1787
def test1():
        str = [1,2,0,3,0]
        k = 1
        assert code1787(str,k) == 3
def test2():
        str = [3,4,5,2,1,7,3,4,7]
        k = 3
        assert code1787(str,k) == 3
def test3():
        str = [1,2,4,1,2,5,1,2,6]
        k = 3
        assert code1787(str,k) == 3


def test4():
        str = [0]
        k = 1
        assert code1787(str,k) == 0

def test5():
        str = [0,0,0,0,0]
        k = 5
        assert code1787(str, k) == 0

def test6():
        str = [1,1,1,1,1]
        k = 1
        assert code1787(str, k) == 5