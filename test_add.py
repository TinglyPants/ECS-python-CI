from add import add
import pytest
def test_add():
     assert add(2, 3) == 5
     assert add(-1, 1) == 0
def test_add_type_error():
    with pytest.raises(TypeError):
        add(2, 3.3)
