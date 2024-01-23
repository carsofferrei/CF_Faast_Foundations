"""Pytest configuration file"""
import pandas as pd
import pytest
from . import FIXTURES_DIR, OUTPUT_DIR
from life_expectancy.class_region import Region


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

# Fixture that read regions
@pytest.fixture(scope="session")
def expected_regions() -> pd.DataFrame:
    """Fixture that read regions"""
    return [
        'AT','FI','ES','EL','EE','DK','DE','CZ','CY','CH','BG','BE','FX','SK','SI',\
        'SE','RO','PT','PL','NO','NL','LU','LT','IT','UK','IS','HU','IE','MT','MK','LI',\
        'FR','RS','HR','LV','UA','TR','ME','AL','AZ','GE','BY','AM','MD','SM','RU','XK'
    ]

