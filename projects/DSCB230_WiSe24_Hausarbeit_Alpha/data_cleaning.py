# Titanic Survivability Analysis
# Data Cleaning Module

# Author: Leon Gjinovci


# Import necessary libraries
import pandas as pd
import numpy as np

# Read CSV into data frame
df = pd.read_csv('data/titanic.csv')

# Function to clean the data
def drop_columns(df):
    """
    Drops unnecessary columns from the DataFrame.
    This function removes the columns 'PassengerId', 'Name', 'Ticket', 'Cabin', and 'Embarked' 
    from the provided DataFrame, as these columns are deemed unnecessary for the analysis.
    Parameters:
    df (pandas.DataFrame): The input DataFrame from which columns will be dropped.
    Returns:
    pandas.DataFrame: The DataFrame after dropping the specified columns.
    """

    # Dropping unnecessary columns as declared in the notebook
    df = df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'])
    return df

# Function to fill missing values in Age column
def fill_age_missing_values(df):
    """
    Fills missing values in the 'Age' column of the DataFrame based on the median age of each gender.
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the Titanic dataset with columns 'Age' and 'Sex'.
    Returns:
    pandas.DataFrame: The DataFrame with missing 'Age' values filled and ages rounded down to the nearest integer.
    """
    
    # Calculating the mean ages for each gender
    median_age_female = df[df['Sex'] == 'female']['Age'].median()
    median_age_male = df[df['Sex'] == 'male']['Age'].median()

    # Fill messing Age values based on the gender of the passenger
    df.loc[(df['Age'].isna()) & (df['Sex'] == 'female'), 'Age'] = median_age_female
    df.loc[(df['Age'].isna()) & (df['Sex'] == 'male'), 'Age'] = median_age_male

    # Rounding the age to nearest int
    df['Age'] = df['Age'].apply(np.floor)

    return df

# Apply functions for preprocessing
df = fill_age_missing_values(df)
df = drop_columns(df)

# Save the cleaned data to a new CSV file
df.to_csv('data/titanic_cleaned.csv', index=False)