import re
import pandas as pd
from pandas import DataFrame
from life_expectancy.region import Region

def clean_data(df: DataFrame, region: Region = Region.PT) -> DataFrame:
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
    df_cleaned = df_droped_nas[df_droped_nas['region'].str.lower() == region.value.lower()]

    return df_cleaned
    