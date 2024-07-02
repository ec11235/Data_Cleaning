import pandas as pd
import webbrowser
import os

FILE_PATH = "data/netflix_data.csv"

uncleaned_df = pd.read_csv(FILE_PATH)

# Setting to display full dataframes in terminal
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def display_uncleaned_df_info(uc_df):
    print("\nMissing values from each column: ")
    print(uc_df.isna().sum())
    print("\nData types of each column: ")
    print(uc_df.dtypes)
    print("\nNumber of duplicate rows:")
    print(uc_df.duplicated().sum())

def dataframe_to_html_and_open(df, filename="dataframe.html"):
    html_path = os.path.abspath(filename)
    df.to_html(html_path, index=False)
    webbrowser.open(f'file://{html_path}')

def change_column_dtypes(df):
    possible_dtypes = ['int', 'float', 'str', 'datetime']
    
    print("\nCurrent data types of each column:")
    print(df.dtypes)
    print("\nWould you like to change the data types of any columns? (y/n)")
    user_choice = input().lower().strip()
    
    if user_choice == 'y':
        finished = False
        while not finished:
            print("Which column would you like to change the data type of?", df.columns.tolist())
            column_choice = input()
            if column_choice in df.columns:
                print(f"Possible data types: {', '.join(possible_dtypes)}")
                print(f"What data type would you like to change '{column_choice}' to? (e.g., int, float, str, datetime)")
                dtype_choice = input().lower().strip()
                if dtype_choice in possible_dtypes:
                    try:
                        if dtype_choice == 'datetime':
                            df[column_choice] = pd.to_datetime(df[column_choice],format='mixed')
                        else:
                            df[column_choice] = df[column_choice].astype(dtype_choice)
                        print(f"Data type of '{column_choice}' changed to {dtype_choice}")
                    except Exception as e:
                        print(f"Error changing data type of '{column_choice}' to {dtype_choice}: {e}")
                else:
                    print(f"Invalid data type '{dtype_choice}'. Please choose from {', '.join(possible_dtypes)}")
                print("\nAre you finished changing data types? (y or n)")
                finished_input = input().lower().strip()
                if finished_input == 'y':
                    finished = True
            else:
                print(f"Column '{column_choice}' does not exist. Please choose a valid column.")
    else:
        print("No data type changes will be made.")
    
    return df

def df_replace(uc_df):
    print("Would you like to replace all missing values with the same value, or different values for each column? (all, individual)")
    second_user_choice = input().lower().strip()

    if second_user_choice == 'all':
        print("What would you like to replace all missing values with? (e.g., 'Not given')")
        replace_value = input()
        uc_df.fillna(replace_value, inplace=True)
    
    elif second_user_choice == 'individual':
        finished = False
        while not finished:
            print("What column would you like to work on?", uc_df.columns.tolist())
            working_column = input()
            
            if working_column in uc_df.columns:
                print(f"What would you like to replace missing values in '{working_column}' with? (e.g., 'Not given')")
                replace_value = input()
                uc_df[working_column] = uc_df[working_column].fillna(replace_value)
                print(f"Missing values in '{working_column}' changed to '{replace_value}'")
                print("\nAre you finished? (y or n)")
                fin = input().lower()
                
                if fin == 'y':
                    finished = True
            else:
                print(f"Column '{working_column}' does not exist. Please choose a valid column.")
    return uc_df

def df_remove(uc_df):
    print("Would you like to remove all rows with any missing values or only rows where a specified column has missing values? (all, column)")
    second_user_choice = input().lower().strip()

    if second_user_choice == 'all':
        uc_df = uc_df.dropna()
    elif second_user_choice == 'column':
        print("Which column would you like to remove rows based on missing values?", uc_df.columns.tolist())
        column_choice = input()
        if column_choice in uc_df.columns:
            uc_df = uc_df.dropna(subset=[column_choice])
        else:
            print(f"Column '{column_choice}' does not exist. Please choose a valid column.")
    else:
        print("Invalid input, must be 'all' or 'column'")
    return uc_df

def display_and_clean(uc_df):
    
    display_uncleaned_df_info(uc_df)
    dataframe_with_missing_values = uc_df[uc_df.isna().any(axis=1)]
    dataframe_to_html_and_open(dataframe_with_missing_values, "missing_values.html")

    finished = False

    while finished != True:
        print("Would you like to replace missing values or remove the rows with missing values from the dataset? (replace,remove)")
        choice = None

        while choice not in ["replace", "remove"]:
            user_choice = input().lower().strip()
            if user_choice in ["replace", "remove"]:
                choice = user_choice
            else:
                print("Invalid input, must be 'replace' or 'remove'")

        if choice == "replace":
            uc_df = df_replace(uc_df)
        elif choice == "remove":
            uc_df = df_remove(uc_df)

        # Ask if user wants to change column data types
        uc_df = change_column_dtypes(uc_df)

        print("Are you finished working on dataframe? (y,n)")
        valid = False
        while valid != True:
            fin = input().lower()
            if fin == 'y':
                finished = True
                valid = True
            elif fin == 'n':
                valid = True
            else:
                print(f"{fin} is an invalid input, please put 'y' or 'n' ")
    
    print("Updated DataFrame now displaying in web browser...")
    dataframe_to_html_and_open(uc_df, "updated_dataframe.html")
    return uc_df

# Example usage
updated_df = display_and_clean(uncleaned_df)
print("done")
