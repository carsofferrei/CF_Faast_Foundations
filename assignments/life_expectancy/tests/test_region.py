"""Tests for the main module"""
from life_expectancy.class_region import Region

def test_obtain_countries_list(expected_regions) -> None:
    """Test that evaluate if the two lists are equals. If the response is positive, the test will pass.
        Args:
            expected_regions (Fixture): load the expected output of the function
    """
    valid_regions = Region.valid_regions()

    assert not set(valid_regions) ^ set(expected_regions)
    