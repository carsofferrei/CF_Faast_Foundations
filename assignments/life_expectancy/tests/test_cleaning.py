"""Tests for the cleaning module"""
from pathlib import Path
import pandas as pd

from life_expectancy.cleaning import load_data
from life_expectancy.cleaning import clean_data
from life_expectancy.cleaning import save_data
from . import OUTPUT_DIR


input_path: Path = OUTPUT_DIR / "eu_life_expectancy_raw.tsv"
output_path: Path = OUTPUT_DIR / 'pt_life_expectancy.csv'

def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    df_loaded = load_data(input_path)
    df_cleaned = clean_data(df_loaded,'PT')
    save_data(df_cleaned, output_path)
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
