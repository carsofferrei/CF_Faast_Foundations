import re
import argparse
from pathlib import Path
import pandas as pd
from pandas import DataFrame
from life_expectancy.tests import OUTPUT_DIR

def load_data(input_path: str|Path, delimiter: str = "[\t]") -> DataFrame:
    """Function that load the .tsv data
    :param input_path: path where the data to be loaded is located. Search in init.py to find OUTPUT_DIR. Raw data.
    :param delimiter: pass the delimiter appropried when reading the input file
    :return DataFrame: Loaded dataframe
    """
    return pd.read_csv(input_path, sep=delimiter, engine="python")



def clean_data(df: DataFrame, region: str) -> DataFrame:
    """Function that load the data
    :param df_loaded: DataFrame that was retrieved in load_data() function
    :param region: define the region the user wants to filter. Default value = 'PT'.
    :return df_cleaned: dataframe after some data treatments as 
            1. define the default column
            2. remove special characters from the values
            3. rename columns
            4. convert some columns to a specific type and remove NaN rows from value
            5. filter the data by the region specified on the parameters.
    """
    #Obtains the values from the first column - main objetive here is to get the country info
    df_country = df.iloc[:, 0]
    df_country = df_country.str.split(',', n=4, expand=True)
    #rename columns
    new_columns = ["unit","sex","age","region"]
    df_country = df_country.set_axis(new_columns, axis=1)

    #Obtain the year and values information of each country
    df_year_values = df.iloc[:,1:]
    #Remove the dots from the columns
    df_cleaned_dots = df_year_values.replace(re.compile(r"\s*:\s*"),"")
    #Remove the letters from the columns
    df_cleaned_values = df_cleaned_dots.replace({r'([a-zA-Z]*)':""},regex=True)

    #Dataframe ready to unpivot
    df_concat = pd.concat([df_country,df_cleaned_values],axis=1)
    #Unpivot the data from the wide format to a load format
    table_col_names = ["unit", "sex", "age", "region"]
    df_unpivot = pd.melt(df_concat,
                        id_vars=table_col_names,
                        value_vars=[i for i in df_concat.columns if i not in table_col_names]
                        )

    # Final dataset
    new_columns_final = ["unit","sex","age","region","year","value"]
    df_col_renamed = df_unpivot.set_axis(new_columns_final, axis=1)

    #Convert data types and Clean nan
    df_col_renamed['year'] = df_col_renamed['year'].astype('int')
    df_col_renamed['value'] = pd.to_numeric(df_col_renamed['value'])
    df_droped_nas = df_col_renamed.dropna(subset=['value'])

    #Filter the final dataset
    df_cleaned = df_droped_nas[df_droped_nas['region'] == region]

    return df_cleaned


def save_data(df: pd.DataFrame, output_path: str|Path) -> None:
    """Fuction that save the data into the expected folder as .csv
    :param df: retrieved from clean_data() function. Cleaned information.
    :param output_path: path where the file is saved. Search in init.py to find OUTPUT_DIR.
    """
    #Export that file into the folder
    df.to_csv(output_path, index=False)
    print(f"Finish data cleaning The file was saved as csv in:\n{output_path}\n")



def main(input_path: str|Path,
         region: str,
         output_path: str|Path,
         delimiter: str = "[\t]"
        ) -> DataFrame:
    """
    call three functions defined above:
        load_data() -> data loaded from a file
        clean_data() -> data cleaned after several operations to the loaded data
        save_data() -> data saved as .csv
    """

    # call and return the .csv data to the correct folder
    df_loaded = load_data(input_path, delimiter)
    df_cleaned = clean_data(df_loaded, region)
    save_data(df_cleaned, output_path)

    return df_cleaned


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.prog = 'cleaning.py'
    parser.description = "This is where the command-line utility's description goes."
    parser.epilog = "This is where the command-line utility's epilog goes."
    parser.add_argument('-i', default = f'{OUTPUT_DIR}/eu_life_expectancy_raw.tsv', help="You need to put here the path of the input file")
    parser.add_argument('-d', default= "[\t]", help = "Delimiter.")
    parser.add_argument('-r', default= 'PT', help = "Filter for the region you want to select.")
    parser.add_argument('-o', default = f'{OUTPUT_DIR}/pt_life_expectancy.csv', help="You need to put here the path where you want to write the output file")
    args = parser.parse_args()
    
    main(input_path = args.i, region = args.r,  output_path = args.o, delimiter = args.d)
    