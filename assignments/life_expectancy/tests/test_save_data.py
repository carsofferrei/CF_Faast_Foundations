"""Tests for the save data module"""
import os
import pandas as pd
from pandas import DataFrame
from life_expectancy.cleaning import save_data, clean_data
from . import OUTPUT_DIR


def test_save_data(eu_life_expectancy_PT_CLEAN: DataFrame, pt_life_expectancy_expected: DataFrame) -> None:
    """
    Run unit test of function `save_data`.
    Need to run clean_data() to obtain the 
    : param eu_life_expectancy_cleaned (Fixture): result after running clean_data()
    : param pt_life_expectancy_expected (Fixture): expected data
    """
    save_data(eu_life_expectancy_PT_CLEAN, f'{OUTPUT_DIR}/eu_life_expectancy_cleaned.csv')
    print("Data saved!")

    assert os.path.isfile(f'{OUTPUT_DIR}/eu_life_expectancy_cleaned.csv') == True
    
    pd.testing.assert_frame_equal(
        eu_life_expectancy_PT_CLEAN, pt_life_expectancy_expected
    )
