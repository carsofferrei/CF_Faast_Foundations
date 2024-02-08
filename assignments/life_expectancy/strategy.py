from typing import Any, Protocol
from pathlib import Path
import pandas as pd
from pandas import DataFrame
from life_expectancy.region import Region


class FileStrategy(Protocol):
    """Read and clean the file
       Common function to the strategy.
    """

    def load_file(self, input_path:Any):
        """
        Reads the file and returns the data as a pandas DataFrame
        Args:
            input_path (Any): file object to read
        """
    def clean_file(self, df:Any, region:Any):
        """
        Cleans data and returns the data as a pandas DataFrame
        Args:
            df (Any): file object to clean
            region (Any): region object to filter
        """

class TSVCSVFilesStrategy:
    """Reads the TSV/CSV File"""

    def load_file(self, input_path: str|Path) -> pd.DataFrame:
        """
        Reads a .CSV, .TXT file and returns the data as a pandas DataFrame
        Args:
            input_path (Any): path to the raw information
        Returns:
            pd.DataFrame: The data read from the .TSV, .CSV, .TXT file as a pandas DataFrame
        """
        return pd.read_csv(input_path, sep="[\t]", engine="python")


class JSONFilesStrategy:
    """Reads the TSV/CSV File"""

    def load_file(self, input_path: str|Path) -> pd.DataFrame:
        """
        Reads a JSON input_path and returns the data as a pandas DataFrame
        Args:
            input_path: path to the raw information
        Returns:
            pd.DataFrame: The data read from the ZIP file as a pandas DataFrame
        """

        return pd.read_json(input_path, compression='zip', encoding='utf-8')
    

    def clean_file(self, df: DataFrame, region: Region = Region.PT) -> DataFrame:
        """Function applied to load data if the file read is .json
        :param df_loaded: DataFrame that was retrieved in load_file() function
        :param region: define the region the user wants to filter. Default value = 'PT'.
        :return df_cleaned: dataframe after some data cleaning

        Notes: 
            1. The .json file was no NaN or Null values in renamed value column.
            2. Data don't need any much transformation besides column renaming and drop extra info.
        """
        df_renamed = df.rename(columns={"country": "region", "life_expectancy": "value"})

        df_remove_columns = df_renamed.drop(columns=["flag", "flag_detail"])

        df_cleaned = df_remove_columns[df_remove_columns['region'].str.lower() == region.value.lower()]

        return df_cleaned    
    


    
def save_data(df: pd.DataFrame, output_path: str|Path) -> None:
    """Fuction that save the data into the expected folder as .csv
    :param df: retrieved from data cleaning function applied. Cleaned information.
    :param output_path: path where the file is saved. Search in init.py to find OUTPUT_DIR.
    """
    #Export that file into the folder
    df.to_csv(output_path, index=False)
    print(f"Finish data cleaning The file was saved as csv in:\n{output_path}\n")
