import matplotlib.pyplot as plt
import numpy as np

years = range(2010, 2021)

yoy_inflation = [1.5, 3.2, 2.1, 1.5, 1.6, 0.1, 1.3, 2.1, 2.4, 2.3, 1.4]
qoq_inflation = [0.9, 1.2, 0.8, 0.4, 0.8, 0.6, 0.6, 0.8, 0.9, 0.6, 0.7, 0.5, 0.5, 0.8, 0.8, 0.9, 0.6, 0.9, 0.7, 0.8, 0.2, 0.4, 0.2, 0.1, 0.2, 0.3, 0.5, 0.5, 0.6, 0.8, 0.7, 0.6, 0.4, 0.5, 0.8, 0.9, 0.6, 0.6, 0.6, 0.5, 0.5, -1.0, 0.8, 0.4]
                
# Calculate cumulative values
yoy_cumulative = np.cumsum(yoy_inflation)
qoq_cumulative = np.cumsum(qoq_inflation)

# Plotting the data
plt.figure(figsize=(10, 6))

# Plotting year-over-year inflation
plt.bar(x=years, height=yoy_inflation, width=0.9, label='Year-over-Year Inflation', alpha=0.7)

# Plotting cumulative year-over-year inflation
plt.plot(years, yoy_cumulative, marker='o', linestyle='-', label='Cumulative Year-over-Year Inflation')

# Plotting quarter-over-quarter inflation
qoq_years = [year + i/4 for year in years for i in range(4)]
plt.bar(x=qoq_years, height=qoq_inflation, width=.25, label='Quarter-over-Quarter Inflation', alpha=0.7)

# Plotting cumulative quarter-over-quarter inflation
qoq_cumulative = np.cumsum(qoq_inflation)
plt.plot(qoq_years, qoq_cumulative, marker='o', linestyle='-', label='Cumulative Quarter-over-Quarter Inflation')

plt.xlabel('Year')
plt.ylabel('Inflation (%)')
plt.title('Year-over-Year vs Quarter-over-Quarter Inflation')
plt.legend()
plt.show()