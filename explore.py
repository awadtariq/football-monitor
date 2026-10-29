import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('data/daily_load.csv')

# Pick the first player column (skipping 'Date' at index 0)
player_col = df.columns[1]

# Convert the Date column to actual datetime objects for proper chronological plotting
df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y')

# Create the plot
plt.figure(figsize=(12, 5))
plt.plot(df['Date'], df[player_col], color='#1B4F72', linewidth=1.5, marker='.', markersize=4)

# Formatting the chart
plt.title(f'Daily Training Load Over Time: {player_col}', fontsize=11, fontweight='bold', pad=12)
plt.xlabel('Date', fontsize=10, fontweight='semibold')
plt.ylabel('Training Load (sRPE)', fontsize=10, fontweight='semibold')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Display the interactive window
plt.show()