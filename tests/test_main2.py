from src.main import div

def test_div():
    assert div(10, 2) == 5
    assert div(-6, 3) == -2
    assert div(0, 5) == 0
