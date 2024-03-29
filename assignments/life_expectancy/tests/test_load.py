"""Tests for the load module"""
import os
from unittest.mock import patch
from life_expectancy.strategy import JSONFilesStrategy, TSVCSVFilesStrategy
from . import OUTPUT_DIR

def test_load_csv(eu_life_expectancy_raw):
    """Verify the function can load the data from the fixture."""
    with patch("pandas.read_csv") as read_csv_mock:
        read_csv_mock.side_effect = [eu_life_expectancy_raw]
        
        # Call the method under test
        strategy = TSVCSVFilesStrategy()
        file_path = os.path.join(OUTPUT_DIR, "eu_life_expectancy_raw.tsv")
        strategy.load_file(file_path)
        
        # Assert that read_csv was called once
        read_csv_mock.assert_called_once()


def test_load_json(eurostat_json):
    """Verify if the read_json function is called once."""
    with patch("pandas.read_json") as read_json_mock:
        read_json_mock.side_effect = [eurostat_json]
        
        # Call the method under test
        strategy = JSONFilesStrategy()
        file_path = os.path.join(OUTPUT_DIR, "eurostat_life_expect.zip")
        strategy.load_file(file_path)
        
        # Assert that read_json was called once
        read_json_mock.assert_called_once()
        