import pytest
from problem135 import code135
# #Partition 1 - Empty array<- invalid test case
# def test1():
#         str = "ACGT"
#         assert code135(str) == []

#Partition 2 - Only one child, no order
def test1():
        r = [5]
        assert code135(r) == 1
#Partition 3,4 - multiple children, uniform rating
def test2():
        r = [3,3,3,3]
        assert code135(r) == 4

# Partition 3,5 - multiple children, ascending order
def test3():
        r = [1,2,3,4]
        assert code135(r) == 10
def test4():
        r = [1,2,2]
        assert code135(r) == 4

#Partition 3,6 - multiple children, descending order
def test5():
        r = [4,3,2,1]
        assert code135(r) == 10


#Partition 3,7 - multiple children, random order
def test6():
        r = [2,4,1,3]
        assert code135(r) ==  6

def test7():
        r = [1,0,2]
        assert code135(r) == 5

def test8():
        r = [1,5,2,6]
        assert code135(r) == 6



