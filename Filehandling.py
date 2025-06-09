import numpy as np

# Opening the file using open()
with open("C:/Users/USER/Downloads/Loan_prediction_dataset.csv", "r") as file:
    # Loading only the numeric loan amount column, skipping the header row
    data = np.genfromtxt(file, delimiter=",", skip_header=1, usecols=7)

# To filter out any existing NaN values
new_data = data[~np.isnan(data)]

# Finding the mean
mean_value = np.mean(new_data)
print(f"Mean: {mean_value}")
# Finding the median
median_value = np.median(new_data)
print(f"Median: {median_value}")
# Finding the standard deviation
std_deviation = np.std(new_data)
print(f"Standard Deviation: {std_deviation}")






