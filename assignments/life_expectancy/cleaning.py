import re
import argparse
from pathlib import Path
import pandas as pd

def clean_data(input_path: str|Path, output_path: str|Path, region: str):
    """Function to clean data"""

    #load data from the file path
    df0 = pd.read_csv(input_path, sep="[\t]", engine="python")

    #Obtains the values from the first column - main objetive here is to get the country info
    df1 =  df0.iloc[:, 0]
    df1 = df1.str.split(',', n=4, expand=True)
    #rename columns
    new_columns = ["unit","sex","age","region"]
    df1 = df1.set_axis(new_columns, axis=1)

    #Obtain the year and values information of each country
    df2 =  df0.iloc[:,1:]
    #Remove the dots from the columns
    df2=df2.replace(re.compile(r"\s*:\s*"),"")
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
    df = df.dropna()

    #Filer the final dataset
    df = df[df['region'] == region]

    #Export that file into the folder
    df.to_csv(output_path, index=False)
    print(f"Finish data cleaning The file was saved as csv in:\n{output_path}\n")


def main():
    """
    Parser setup + call clean data function
    """
    parser = argparse.ArgumentParser()
    parser.prog = 'clean_data'
    parser.description = "This is where the command-line utility's description goes."
    parser.epilog = "This is where the command-line utility's epilog goes."
    parser.add_argument('-i', default = "/workspaces/CF_Faast_Foundations/assignments/life_expectancy/data/eu_life_expectancy_raw.tsv", help="You need to put here the path of the input file")
    parser.add_argument('-o', default = '/workspaces/CF_Faast_Foundations/assignments/life_expectancy/data/pt_life_expectancy.csv', help="You need to put here the path where you want to write the output file")
    parser.add_argument('-r', default= 'PT', help="Filter for the region you want to select.")
    args = parser.parse_args()

    # clean data and return the .csv data to the correct folder
    clean_data(args.i,args.o, args.r)

if __name__ == "__main__": # pragma: no cover
    main()
    