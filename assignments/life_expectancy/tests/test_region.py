"""Tests for the main module"""
from life_expectancy.region import Region

def test_obtain_countries_list(expected_regions) -> None:
    """Test that evaluate if the two lists are equals. If the response is positive, the test will pass. Also, evaluate if # the elements are the same.
        Args:
            expected_regions (Fixture): load the expected output of the function
    """
    valid_regions = Region.valid_regions()


    # Evaluate if both lists have the same elements
    assert set(valid_regions) == set(expected_regions)
    
    # Evaluate if the size of both lists its the same
    assert len(valid_regions) == len(expected_regions)
    