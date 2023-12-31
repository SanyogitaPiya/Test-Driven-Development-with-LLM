def test1():
    assert code2612(5, 3, [], 2) == [3,2,1,0,1]
    assert code2612(7, 0, [], 3) == [0, -1, 1, -1, 2, -1, 3]

def test2():
    assert code2612(6, 1, [], 1) == [-1, 0, -1, -1, -1, -1]
    assert code2612(8, 2, [], 1) == [-1, -1, 0, -1, -1, -1, -1, -1]

def test3():
    assert code2612(5, 0, [3], 2) == [0, 1, 2, -1, -1]
    assert code2612(7, 2, [4, 6], 3) == [1, -1, 0, -1, -1, -1, -1]

def test4():
    assert code2612(4,0,[1,2],4) == [0,-1,-1,1]
    assert code2612(5,0,[2,4],3) == [0,-1,-1,-1,-1]
    assert code2612(6, 0, [1, 2], 1) == [0, -1, -1, -1, -1, -1]
    assert code2612(8, 3, [1, 5, 7], 1) == [-1, -1, -1, 0, -1, -1, -1, -1]

def test5():
    assert code2612(4,2,[0,1,3],1) == [-1,-1,0,-1]
    assert code2612(4, 2, [0, 1, 3], 2) == [-1, -1, 0, -1]
    assert code2612(6, 5, [0, 1, 2, 3, 4], 3) == [-1, -1, -1, -1, -1, 0]

def test6():
    assert code2612(5, 1, [0, 2, 3, 4], 1) == [-1, 0, -1, -1, -1]
    assert code2612(7, 4, [0, 1, 2, 3, 5, 6], 1) == [-1, -1, -1, -1, 0, -1, -1]