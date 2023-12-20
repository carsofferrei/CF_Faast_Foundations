import re
import argparse
from pathlib import Path
import pandas as pd


def load_data(input_path: str|Path, delimiter: str = "[\t]") -> pd.DataFrame:
    """Function that load the data
    :param df: local where the file is located. Search in __init__.py to find OUTPUT_DIR. Raw data.
    """
    if input_path is None: 
        raise ValueError ("The fuction requires one argument. Please define you're input_path to reach the file.")

    df = pd.read_csv(input_path, sep=f"{delimiter}", engine="python")
    return df


def clean_data(df: pd.DataFrame, region: str) -> pd.DataFrame:
    """Function that load the data
    :param df: file that was retrieved in load_data() function
    :param region: define the region the user wants to filter. Default value = 'PT'.
    :return df: dataframe after some data treatments as 
            1. define the default column
            2. remove special characters from the values
            3. rename columns
            4. convert some columns to a specific type and remove NaN rows from value
            5. filter the data by the region specified on the parameters.
    """
    if df is None: 
        raise ValueError ("The fuction requires a DataFrame as an argument.") 


    #Obtains the values from the first column - main objetive here is to get the country info
    df1 = df.iloc[:, 0]
    df1 = df1.str.split(',', n=4, expand=True)
    #rename columns
    new_columns = ["unit","sex","age","region"]
    df1 = df1.set_axis(new_columns, axis=1)

    #Obtain the year and values information of each country
    df2 = df.iloc[:,1:]
    #Remove the dots from the columns
    df2 = df2.replace(re.compile(r"\s*:\s*"),"")
    #Remove the letters from the columns
    df2 = df2.replace({r'([a-zA-Z]*)':""},regex=True)

    #Dataframe ready to unpivot
    df = pd.concat([df1,df2],axis=1)
    #Unpivot the data from the wide format to a load format
    table_col_names = ["unit", "sex", "age", "region"]
    df_unpivot = pd.melt(df,
                        id_vars=table_col_names,
                        value_vars=[i for i in df.columns if i not in table_col_names]
                        )

    # Final dataset
    new_columns = ["unit","sex","age","region","year","value"]
    df = df_unpivot.set_axis(new_columns, axis=1)

    #Convert data types and Clean nan
    df['year'] = df['year'].astype('int')
    df['value'] = pd.to_numeric(df['value'])
    df = df.dropna(subset=['value'])

    #Filer the final dataset
    df = df[df['region'] == region]

    return df

def save_data(df: pd.DataFrame, output_path: str|Path):
    """Fuction that save the data into the expercted folder.
    :param df: file that was retrieved in save_data() function. Cleaned information.
    :param output_path: local where the file is located. Search in __init__.py to find OUTPUT_DIR
    """
    if df is None: 
        raise ValueError ("The fuction requires a DataFrame as an argument.") 
    if output_path is None: 
        raise ValueError ("The fuction requires a path to save the file.") 

     #Export that file into the folder
    df.to_csv(output_path, index=False)
    print(f"Finish data cleaning The file was saved as csv in:\n{output_path}\n")



def main(): # pragma: no cover
    """
    Parser setup + call three functions defined above
    """
    parser = argparse.ArgumentParser()
    parser.prog = 'cleaning.py'
    parser.description = "This is where the command-line utility's description goes."
    parser.epilog = "This is where the command-line utility's epilog goes."
    parser.add_argument('-i', default = "/workspaces/CF_Faast_Foundations/assignments/life_expectancy/data/eu_life_expectancy_raw.tsv", help="You need to put here the path of the input file")
    parser.add_argument('-r', default= 'PT', help="Filter for the region you want to select.")
    parser.add_argument('-o', default = '/workspaces/CF_Faast_Foundations/assignments/life_expectancy/data/pt_life_expectancy.csv', help="You need to put here the path where you want to write the output file")
    args = parser.parse_args()
    # call and return the .csv data to the correct folder
    df = load_data(args.i)
    df = clean_data(df, args.r)
    save_data(df, args.o)

if __name__ == "__main__": # pragma: no cover
    main()
    