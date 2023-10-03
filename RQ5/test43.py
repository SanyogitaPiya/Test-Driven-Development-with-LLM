import pytest
from problem43 import code43
# #Partition 1 - Single digits only
def test1():
        num1 = "2"
        num2 = "3"
        assert code43(num1, num2) == "6"
def test1a():
        num1 = "5"
        num2 = "7"
        assert code43(num1, num2) == "35"


#Partition 2:Small numbers
def test2():
        num1 = "123"
        num2 = "456"
        assert code43(num1, num2) == "56088"
#Partition 3: large numbers
def test3():
        num1 = "1234567"
        num2 = "4567891"
        assert code43(num1, num2) == "5639367488197"


#Partition 4: Special case zero
def test4():
        num1 = "1234567"
        num2 = "0"
        assert code43(num1, num2) == "0"


