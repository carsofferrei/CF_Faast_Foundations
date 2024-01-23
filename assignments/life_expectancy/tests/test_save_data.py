"""Tests for the save data module"""
import os
from pandas import DataFrame
from life_expectancy.cleaning import save_data
from . import OUTPUT_DIR

#dataframe vazio e ver se salva

def test_save_data() -> None:
    """
    Run unit test of function `save_data`.
    Need to run clean_data() to obtain the 
    : param eu_life_expectancy_cleaned (Fixture): result after running clean_data()
    : param pt_life_expectancy_expected (Fixture): expected data
    """
    data = DataFrame()

    save_data(data, f'{OUTPUT_DIR}/SAVE_DATA_TEST.csv')
    print("Data saved!")

    assert os.path.isfile(f'{OUTPUT_DIR}/eu_life_expectancy_cleaned.csv') is True
