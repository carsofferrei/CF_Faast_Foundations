"""Pytest configuration file"""
import pandas as pd
import pytest
from life_expectancy.cleaning import clean_data 
from . import FIXTURES_DIR, OUTPUT_DIR


# Fixture that read the expected results from applying clean_data() and filter the region 'PT'
@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")


# Fixture that read raw information after normalize columns
@pytest.fixture(scope="session")
def eu_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv")


# Fixture that read raw information
@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> pd.DataFrame:
    """Fixture to load the raw initial data for testing"""
    eu_life_expectancy_raw = pd.read_csv(OUTPUT_DIR / "eu_life_expectancy_raw.tsv", sep="[\t]", engine = "python")
    return eu_life_expectancy_raw


# DataFrame that results from applying clean_data() to the raw information
@pytest.fixture(scope="session")
def eu_life_expectancy_PT_CLEAN(eu_life_expectancy_raw: pd.DataFrame) -> pd.DataFrame:
    """Fixture to load the raw initial data for testing"""
    eu_life_expectancy_PT_CLEAN = clean_data(eu_life_expectancy_raw, "PT").reset_index(drop=True)
    return eu_life_expectancy_PT_CLEAN

