import pytest


@pytest.mark.usefixtures("dataload")
class Testexample2:
    def test_editProfile(self, dataload):
        print(dataload[0])
        print(dataload[2])
