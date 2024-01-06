"""Tests for the save data module"""

import os
from unittest import mock
import pandas as pd

from life_expectancy.cleaning import save_data

from . import FIXTURES_DIR, OUTPUT_DIR
