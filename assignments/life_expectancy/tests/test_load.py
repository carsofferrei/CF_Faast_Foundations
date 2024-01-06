"""Tests for the load module"""
import pandas as pd

from life_expectancy.cleaning import load_data

from . import FIXTURES_DIR, OUTPUT_DIR


def test_load_data():
    """
    Run unit test of function `load_data`.
    """
    actual_data = load_data(FIXTURES_DIR/ "pt_life_expectancy_expected.csv")
    expected_data = load_data(FIXTURES_DIR / "eu_life_expectancy_expected.csv")

    pd.testing.assert_frame_equal(actual_data, expected_data)