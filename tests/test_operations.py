from examplelib import operations

def test_add():
    assert operations.add(4, 5) == 9

def test_sub():
    assert operations.sub(4, 5) == -1

def test_mul():
    assert operations.mul(4, 5) == 20

def test_div():
    assert operations.div(6, 3) == 2

def test_rgbaExpansion():
    assert operations.rgbaExpansion(8,6,5) == "http://127.0.0.1:8000/?red=7&blue=5&green=4"

def test_convolute():
    assert operations.convolute(4) == "http://127.0.0.1:8000/convolute/edge/?band=3"
    