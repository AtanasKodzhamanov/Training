# Suppose we have a dataset that contains information about the heights of a sample of 100 people, and we want to make inferences about the average height of the population. The data looks like this:


from scipy import stats
import pandas as pd
height
72
68
74

    # Load data
data = pd.read_csv('data.csv')

# Calculate the sample mean and standard deviation
sample_mean = data['height'].mean()
sample_std = data['height'].std()

# Calculate the 95% confidence interval for the population mean
n = len(data)
t = stats.t.ppf(0.975, n - 1)
se = sample_std / (n ** 0.5)
ci_lower = sample_mean - t * se
ci_upper = sample_mean + t * se

# Print the results
print('Sample Mean:', sample_mean)
print('Sample Standard Deviation:', sample_std)
print('95% Confidence Interval for Population Mean: [{:.2f}, {:.2f}]'.format(
    ci_lower, ci_upper))
