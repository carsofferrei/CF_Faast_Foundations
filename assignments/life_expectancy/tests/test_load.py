"""Tests for the load module"""
import pandas as pd
from life_expectancy.cleaning import load_data
from . import FIXTURES_DIR

def test_load_data():
    """
    Run unit test of function `load_data`.
    """
    actual_data = load_data(FIXTURES_DIR / "test_dataset.tsv")
    expected_data = pd.DataFrame.from_dict(
        {
            "col_1,col_2,col_3": ["1,10,15", "1,5,10", "x1,x2,x3"],
            "2021": [79, 61, 70],
            "2020": [85, 60, 50],
        }
    )

    pd.testing.assert_frame_equal(actual_data, expected_data)