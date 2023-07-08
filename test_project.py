from project import get_constellation, compare_pair, final_result
import pytest


def test_get_constellation():
    assert get_constellation("Orion") == "Orion"
    with pytest.raises(SystemExit):
        get_constellation("Canopus")


def test_compare_pair():
    assert compare_pair("Rigel", "Orion") == "Correct"
    assert compare_pair("Rigel", "Lyra") == "Incorrect"


def test_final_result():
    assert final_result("Rigel") == "Orion"
