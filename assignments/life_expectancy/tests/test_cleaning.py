"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import clean_data
from life_expectancy.region import Region


def test_clean_data(eu_life_expectancy_raw, pt_life_expectancy_expected) -> None:
    """Compare the output of the "clean_data" function to the expected output
        Args:
            eu_life_expectancy_raw (Fixture): load the expected raw data 
            pt_life_expectancy_expected (Fixture): load the expected output of the cleaning script
        Returns:
    """
    pt_life_expectancy_actual = clean_data(
        eu_life_expectancy_raw, region = Region.PT
    ).reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
