import pytest
from python.calc import Calc

class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_add_1(self):
        result = self.calc.add(1,2)
        print(result)
        assert  3 == result

if __name__ == '__main__':
    pytest.main(['-vs','test_pytest.py::TestCalc::tet_div'])