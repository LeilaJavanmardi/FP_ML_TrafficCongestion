import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error



def fill_with_previous_week(row, df):
    """
    Fill missing intensity values by replacing them with the intensity value 
    from the same weekday and time (hour and minute) in the previous week.

    Parameters:
        row (pandas.Series): A single row of the DataFrame containing intensity values.
        df (pandas.DataFrame): The DataFrame containing the intensity data.

    Returns:
        float or np.nan: The intensity value from the previous week if a match is found, 
                         otherwise np.nan.

    Notes:
        This function assumes that the index of the DataFrame 'df' is a datetime index.
        Missing intensity values are identified using pd.isna(row['intensity']).
        The function searches for a matching intensity value from the same weekday and time
        in the previous week and returns the intensity value if a match is found.
        If no match is found, np.nan is returned to indicate that the missing value could not be filled.
    """
    if pd.isna(row['intensity']):
        target_date = row.name
        print("Target Date:", target_date)  # Debug print

        #the previous week
        previous_week_start = target_date - pd.DateOffset(weeks=1)
        previous_week_end = previous_week_start + pd.DateOffset(days=6)

        # Filter the previous week + the same weekday
        previous_week_df = df[(df.index >= previous_week_start) & 
                              (df.index <= previous_week_end) &
                              (df.index.weekday == target_date.weekday())]
        
        match = previous_week_df[(previous_week_df.index.hour == target_date.hour) & 
                                 (previous_week_df.index.minute == target_date.minute)]

        print("Matches found:", len(match))  # Debug print
        
        if not match.empty:
            print("Intensity in Match:", match['intensity'].iloc[0])  # Print the intensity value in the match
            return match['intensity'].iloc[-1]  # Return the intensity from the last row of the match
        else:
            return np.nan
    else:
        return row['intensity']



def refill_with_previous_week(row, df,column):
    """
    Fill missing values in a specific column of a DataFrame row by replacing them with the corresponding 
    value from the same weekday and time (hour and minute) in the previous week.

    Parameters:
        row (pandas.Series): A single row of the DataFrame containing the data.
        df (pandas.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to fill with previous week's data.

    Returns:
        float or np.nan: The value from the previous week if a match is found, 
                         otherwise np.nan.

    Notes:
        This function assumes that the index of the DataFrame 'df' is a datetime index.
        Missing values are identified using pd.isna(row[column]).
        The function searches for a matching value from the same weekday and time
        in the previous week and returns the value if a match is found.
        If no match is found, np.nan is returned to indicate that the missing value could not be filled.
    """
    if pd.isna(row[column]):
        target_date = row.name
        print("Target Date:", target_date) 

        #the previous week
        previous_week_start = target_date - pd.DateOffset(weeks=1)
        previous_week_end = previous_week_start + pd.DateOffset(days=6)

        # Filter the previous week + the same weekday
        previous_week_df = df[(df.index >= previous_week_start) & 
                              (df.index <= previous_week_end) &
                              (df.index.weekday == target_date.weekday())]
        
        match = previous_week_df[(previous_week_df.index.hour == target_date.hour) & 
                                 (previous_week_df.index.minute == target_date.minute)]

        print("Matches found:", len(match))
        
        if not match.empty:
            return match[column].iloc[-1]
        else:
            return np.nan
    else:
        return row[column]



def calculate_mae(actual, predicted):
    """ Calculate Mean Absolute Error """
    mae = mean_absolute_error(actual, predicted)
    return mae


def calculate_mape(actual, predicted):
    """ Calculate Mean Absolute Percentage Error """
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    return mape

def calculate_mase(actual, predicted, training):
    """ Calculate Mean Absolute Scaled Error """
    # Naive forecast using training data
    naive_forecast = training.shift(1)
    mae_naive = mean_absolute_error(training[1:], naive_forecast.dropna())
    mae_model = mean_absolute_error(actual, predicted)
    mase = mae_model / mae_naive
    return mase

