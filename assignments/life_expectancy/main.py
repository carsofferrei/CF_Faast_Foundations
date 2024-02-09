import argparse
from pathlib import Path
from pandas import DataFrame
from life_expectancy.tests import OUTPUT_DIR
from life_expectancy.region import Region
from life_expectancy.cleaning import clean_data
from life_expectancy.strategy import TSVCSVFilesStrategy, JSONFilesStrategy, save_data


def main(input_path: str|Path,
         output_path: str|Path,
         region: Region = Region.PT
        ) -> DataFrame:
    
    """
    Function that have different approaches given the extension of the input file
    """
    if input_path.lower().endswith(('.zip')):
        # if the extension is a .zip folder
        df_loaded = JSONFilesStrategy().load_file(input_path)
        df_cleaned = JSONFilesStrategy().clean_file(df_loaded, region)

    else:
        # if the extension is a .csv, .tsv, .txt
        df_loaded = TSVCSVFilesStrategy().load_file(input_path)
        df_cleaned = clean_data(df_loaded, region)
    
    save_data(df_cleaned, output_path)

    return df_cleaned


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.description = "This is where the command-line utility's description goes."
    parser.epilog = "This is where the command-line utility's epilog goes."
    parser.add_argument('-i', default = f'{OUTPUT_DIR}/eu_life_expectancy_raw.tsv', help="You need to put here the path of the input file")
    parser.add_argument('-r', type = Region, choices = Region, default = Region.PT, help = "Filter for the region you want to select.")
    parser.add_argument('-o', default = f'{OUTPUT_DIR}/{parser.parse_args().r.value.lower()}_life_expectancy.csv', help="You need to put here the path where you want to write the output file")
    args = parser.parse_args()
    
    main(input_path = args.i, region = args.r,  output_path = args.o)
    