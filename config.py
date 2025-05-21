# Config script
# This script contains the configuration settings for the analysis of accelerometer data.
# Script created on 5/19/2025
# Last revision: 5/19/2025

# acceleration threshold value to signal sternal recumbency for initial filter
target_value: float = 9.0 
    
# variables for moving average filter
target_moving_avg: int = 10 # moving average window_size (originally set to 4)
    
# variables for Kalman filter
process_variance = 1e-5  # Q
measurement_variance = 1e-1  # R
estimated_measurement_variance = 1.0  # P   
    
# variables for ROI_Derivative method
factor: float = 8.0   # Factor to set jerk threshold (56.55)
percentile: float = 95.0    # Percentile to set jerk threshold  
jerk_threshold: float = 4.64e-07 #0.2e-06 #5.7209199129367875e-12  # Threshold for significant jerk
snap_threshold: float = 1  # Threshold for significant snap (needs re calibration)

# variables for ROI_SD method
# values that can be changed  to increase/ decrease sensitivity
window_size: int = 5000 # each cell is 5ms, 10000 cells represent 2secs, 2500 cells are 0.5secs
step_size: int = 1000 # 2000 cells are 400ms (0.4secs), 833 cells are 166.6ms (0.166secs)
threshold: float = 1e-08 # default value for SD threshold 1.5 (1.5e-08)