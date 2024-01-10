"""Tests for the main module"""
import pandas as pd
from pytest import MonkeyPatch
from life_expectancy.cleaning import main
from . import OUTPUT_DIR

input_path = "/workspaces/CF_Faast_Foundations/assignments/life_expectancy/data/eu_life_expectancy_raw.tsv"
region = 'PT'
output_path = '/workspaces/CF_Faast_Foundations/assignments/life_expectancy/data/pt_life_expectancy.csv'

def test_main(pt_life_expectancy_expected):
    """Run the `main` function and compare the output to the expected output
    Args:
        pt_life_expectancy_expected (Fixture) : load the expected output of the cleaning script
        monkeypatch (MonkeyPatch): pytest fixture that provides a way to modify the behavior of 
            functions or classes during tests.
    Returns:
    """
    # Call the main function and get the result
    pt_life_expectancy_actual = main(input_path, region, output_path).reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )