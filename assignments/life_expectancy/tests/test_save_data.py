"""Tests for the save data module"""

import os
from unittest.mock import patch
from pandas import DataFrame
from life_expectancy.strategy import save_data
from . import OUTPUT_DIR

def test_save_data() -> None:
    """
    Run unit test of function `save_data` and evaluate by mock Module if the function to_csv is called at least once.
    """
    with patch("pandas.DataFrame.to_csv") as to_csv_mock:
        # Raise an exception when a mock is called. Is this case, if the side_effect wasn't correct here
        # will be raised an exception. 
        to_csv_mock.side_effect = print("\nTesting save_data")

        # Saving a empty dataframe in a file.
        save_data(DataFrame, 
                  f'{OUTPUT_DIR}/SAVE_DATA_MOCK.csv')

        # Evaluate if the mock is called at least once. This is really evaluating if to_csv is working and 
        # if the save_data function is achieving it goal.
        to_csv_mock.assert_called_once()


def test_data_folder() -> None:
    """
    Run unit test of function `save_data` and test if the fuction save a file in expected folder
    """
    data = DataFrame()
    save_data(data, f'{OUTPUT_DIR}/SAVE_DATA_FOLDER.csv')
    assert os.path.isfile(f'{OUTPUT_DIR}/SAVE_DATA_FOLDER.csv') is True