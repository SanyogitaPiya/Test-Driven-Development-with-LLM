import pytest
from problem187 import code187
#(Partition 1 - Short input, No repeated sequences
def test1():
        str = "ACGT"
        assert code187(str) == []

#Test Case 2 (Partition 2 - Exactly 10 characters, No repeated sequences):
def test2():
        str = "ACGTACGTAC"
        assert code187(str) == []
#Partition 3 - Long input, Contains repeated sequences
def test3():
        str = "ACGTACGTACGTACGTACGT"
        assert code187(str) == ["ACGTACGTAC","CGTACGTACG","GTACGTACGT","TACGTACGTA"]


def test4():
        str = "ACGTACGTACGTACGTACGTACGTACGTACGT"
        assert code187(str) == ["ACGTACGTAC","CGTACGTACG","GTACGTACGT","TACGTACGTA"]

def test6():
        str = "ACGTACGTACGTACGTACGTACGTA"
        assert code187(str) == ["ACGTACGTAC","CGTACGTACG","GTACGTACGT","TACGTACGTA"]


#Partition 3 - Long input, No repeated sequences
def test5():
        str = "ACGAATTCCGTA"
        assert code187(str) == []

