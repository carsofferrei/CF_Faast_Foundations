"""Tests for the main module"""
import pandas as pd

from life_expectancy.cleaning import main
from . import OUTPUT_DIR


def test_main():
    """Run the `clean_data` function and compare the output to the expected output"""

    pt_life_expectancy_test = main()

    pt_life_expectancy_actual = pd.read_csv(OUTPUT_DIR / "pt_life_expectancy.csv")

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_test
    )
