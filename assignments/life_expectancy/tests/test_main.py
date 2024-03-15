"""Tests for the main module"""
import pandas as pd
from life_expectancy.main import main
from life_expectancy.region import Region
from . import OUTPUT_DIR

input_path = f'{OUTPUT_DIR}/eu_life_expectancy_raw.tsv'
input_path_json = f'{OUTPUT_DIR}/eurostat_life_expect.zip'
output_path = f'{OUTPUT_DIR}/pt_life_expectancy.csv'

def test_main(pt_life_expectancy_expected):
    """Run the `main` function and compare the output to the expected output
    Args:
        pt_life_expectancy_expected (Fixture) : load the expected output of the main script
    Returns:
    """
    # Call the main function and get the result
    pt_life_expectancy_actual = main(input_path = input_path, output_path = output_path, region = Region.PT).reset_index(drop=True)

    # Call the main function and get the result
    pt_life_expectancy_actual_json = main(input_path = input_path_json, output_path = output_path, region = Region.PT).reset_index(drop=True)

 
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual_json, pt_life_expectancy_expected
    )

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_actual_json
    )
