import sys
sys.path.append("app")

from app import add

def test_add():
    assert add(2, 3) == 5
