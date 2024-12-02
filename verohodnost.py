import pandas as pd
import numpy as np
from scipy.optimize import minimize
from scipy.stats import chi2

# Load the Excel file
file_path = "Data_2024.xlsx"  # Update with the correct file path
sheet_name = "Data_věrohodnost"

# Read the sheet into a DataFrame
data_df = pd.read_excel(file_path, sheet_name=sheet_name)

# Extract relevant columns from the DataFrame
censored = data_df['censored']
employment_duration = data_df['doba práce v oboru [roky]']

# Create a data dictionary to match the second script's format
data = {
    "censored": censored.to_numpy(),
    "duration": employment_duration.to_numpy()
}

# Log-likelihood function for censored Weibull distribution
def weibull_log_likelihood(params, data):
    shape, scale = params
    censored = data["censored"]
    duration = data["duration"]

    # PDF and survival function
    pdf = (shape / scale) * (duration / scale) ** (shape - 1) * np.exp(- (duration / scale) ** shape)
    sf = np.exp(- (duration / scale) ** shape)

    # Log-likelihood with censoring
    log_likelihood = np.sum(censored * np.log(sf) + (1 - censored) * np.log(pdf))
    return -log_likelihood  # Negative for minimization

# Initial parameter guesses
initial_params = [1.0, 6.0]

# Maximize log-likelihood
result = minimize(weibull_log_likelihood, initial_params, args=(data), bounds=[(0.1, None), (0.1, None)])
shape_mle, scale_mle = result.x

# Hypothesis testing: Likelihood ratio test
# Null hypothesis: Shape = 1 (Exponential distribution)
def exponential_log_likelihood(scale, data):
    censored = data["censored"]
    duration = data["duration"]
    pdf = (1 / scale) * np.exp(-duration / scale)
    sf = np.exp(-duration / scale)
    log_likelihood = np.sum(censored * np.log(sf) + (1 - censored) * np.log(pdf))
    return log_likelihood

exp_scale_mle = np.mean(data["duration"])  # MLE for exponential scale parameter
log_likelihood_weibull = -result.fun
log_likelihood_exponential = exponential_log_likelihood(exp_scale_mle, data)

# Likelihood ratio statistic
lr_statistic = 2 * (log_likelihood_weibull - log_likelihood_exponential)

# p-value
p_value = 1 - chi2.cdf(lr_statistic, df=1)

# Mean and 10th percentile estimation
mean_weibull = scale_mle * np.exp(np.log(1 + 1 / shape_mle))
percentile_10_weibull = scale_mle * (-np.log(0.9)) ** (1 / shape_mle)

# Output
print("Shape (MLE):", shape_mle)
print("Scale (MLE):", scale_mle)
print("Likelihood ratio statistic:", lr_statistic)
print("p-value:", p_value)
print("Mean employment duration (years):", mean_weibull)
print("10% percentile of employment duration (years):", percentile_10_weibull)

