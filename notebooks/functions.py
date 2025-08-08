"""
Functions module for descriptive statistics exercises.

This module contains utility functions for processing movie data,
particularly for calculating title length features.
"""

import pandas as pd


def add_title_length_features(dataframe, title_column='title', length_column='title_length'):
    """
    Add title length features to a dataframe.
    
    Parameters:
    dataframe (pd.DataFrame): The dataframe containing movie titles
    title_column (str): Name of the column containing titles (default: 'title')
    length_column (str): Name of the new column to create (default: 'title_length')
    
    Returns:
    pd.DataFrame: The dataframe with the new title length column added
    
    Raises:
    ValueError: If the specified title_column doesn't exist in the dataframe
    TypeError: If dataframe is not a pandas DataFrame
    """
    # Type checking
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    # Check if title column exists
    if title_column not in dataframe.columns:
        raise ValueError(f"Column '{title_column}' not found in dataframe")
    
    # Create a copy to avoid modifying the original dataframe
    df_copy = dataframe.copy()
    
    # Calculate title length using str.len() method
    df_copy[length_column] = df_copy[title_column].str.len()
    
    return df_copy
