"""Tests for the cleaning module"""
from pathlib import Path
import pandas as pd

from life_expectancy.cleaning import clean_data
from . import OUTPUT_DIR

input_path: Path = OUTPUT_DIR / "eu_life_expectancy_raw.tsv"
output_path: Path = OUTPUT_DIR / 'pt_life_expectancy.csv'

def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    clean_data(input_path, output_path, 'PT')
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
