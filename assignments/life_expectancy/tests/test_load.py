"""Tests for the load module"""
import pandas as pd
from life_expectancy.cleaning import load_data
from . import FIXTURES_DIR

def test_load_data() -> None:
    """Compare the output of the "clean_data" function to the expected output
        Args:
            eu_life_expectancy_raw (Fixture): load the expected raw data 
            pt_life_expectancy_expected (Fixture): load the expected output of the cleaning script
        Returns:
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