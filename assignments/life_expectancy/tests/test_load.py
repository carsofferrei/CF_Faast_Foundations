"""Tests for the load module"""
import pandas as pd
from life_expectancy.cleaning import load_data
from . import FIXTURES_DIR

def test_load_data() -> None:
    """Compare the output of the "clean_data" function to the expected output
            actual_data (Fixture): dataset to be compared to the expected
            expected_data: Sample dataset for test load data
    """
    actual_data = load_data(FIXTURES_DIR / "test_dataset.tsv")
    expected_data = pd.DataFrame.from_dict(
        {
            "col_1,col_2,col_3": ["1,10,15", "1,5,10", "BG,PT,TT"],
            "2021": [79, 61, 70],
            "2020": [85, 60, 50],
        }
    )

    pd.testing.assert_frame_equal(actual_data, expected_data)