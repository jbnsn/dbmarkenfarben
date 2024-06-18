"""Overview."""

import dbmarkenfarben as dbmf
import matplotlib.pyplot as plt
import pandas as pd

db_colors = dbmf.DeutscheBahnMarkenFarben()

# %% Plot

dbcolor_names = [
    'yellow', 'orange', 'red',
    'burgundy', 'pink', 'violet',
    'blue', 'cyan', 'turquoise',
    'green', 'light-green', 'warm-grey',
    'cool-grey'
    ]

dbcolor_shades = [
    800, 700,
    600, 500,
    400, 300,
    200, 100
    ]

df = pd.DataFrame(
    index=dbcolor_shades,
    columns=dbcolor_names
    )

# Populate dataframe
for name in dbcolor_names:
    for shade in dbcolor_shades:
        df.loc[shade, name] = db_colors.get(name, shade)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Loop through the DataFrame and plot each color as a rectangle
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        color = df.iloc[i, j]
        ax.add_patch(
            plt.Rectangle((j, df.shape[0] - 1 - i), 1, 1, color=color)
            )

# Set limits, ticks, and labels
ax.set_xlim(0, df.shape[1])
ax.set_ylim(0, df.shape[0])
ax.set_xticks([i+0.5 for i in range(df.shape[1])])
ax.set_yticks([j for j in [i+0.5 for i in range(df.shape[0])][::-1]])
ax.set_xticklabels(df.columns, rotation=90)
ax.set_yticklabels(df.index)

# Set the aspect ratio to be equal
ax.set_aspect('equal')

# Remove axis spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Remove tick marks
ax.tick_params(axis='both', which='both', length=0)

# Save the plot
plt.savefig('overview.png', bbox_inches='tight')

# Show the plot
plt.show()
