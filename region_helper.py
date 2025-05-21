# Recovery Score Calculations: Calculation helper
# Script created  3/25/2024
# Last revision 12/13/2024

import pandas as pd

def extract_roi_values(df: pd.DataFrame, roi_indices, axes: list) -> pd.DataFrame:
    '''Extracts the values within each region of interest (ROI) for each specified axis from the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame containing the data.
        roi_indices (pd.DataFrame): DataFrame containing the indices of regions of interest.
        axes (list): List of axis names to extract values for (e.g., ['Acc_X', 'Acc_Y', 'Acc_Z']).

    Returns:
        pd.DataFrame: DataFrame containing the values within each ROI for each axis.
    '''
    roi_values = {axis: [] for axis in axes}
    roi_values['ROI_Index'] = []

    for index in roi_indices['ROI_Indices']:
        for axis in axes:
            roi_values[axis].append(df[axis].iloc[index])
        roi_values['ROI_Index'].append(index)

    return pd.DataFrame(roi_values)

def get_number_roi_sd(df: pd.DataFrame, regions_of_interest_sd: list, window_size: int, step_size: int)-> list:
    '''Provides number of regions_of_interest. DataFrames with the selected regions of interest
    
    Args:
        filtered_df: pd.DataFrame provided
        regions_of_interest_sd: list of tuples with the start and the end of each of the regions that have a standad deviation > set threshold
        window_size (int): size of each window
        step_size (int):step_size for the window
        
    Returns:
        list: list of DataFrames, each DataFrame contains a specific region of interest, 
               and three lists with maximum absolute values of AccX, AccY, and AccZ for each region.
               Selected_Data_list is a list with a dataframe with AccX, AccY and AccZ per event
    '''
    # Store data from each reion of interest
    selected_data_list: list = [] 
    
    # Loop through each region of interest (ROI)
    for i, roi in enumerate(regions_of_interest_sd):
        start_index:int = roi[0] * step_size
        end_index: int = start_index + window_size
        
        # Ensure the end index does not exceed the dataframe length
        if end_index > len(df):
            end_index: int = len(df)
            
        # Select rows using iloc and columns using column names
        selected_data: pd.DataFrame = df.iloc[start_index:end_index][['Acc_X', 'Acc_Y', 'Acc_Z']]
    
        selected_data_list.append(selected_data)
           
    return selected_data_list
