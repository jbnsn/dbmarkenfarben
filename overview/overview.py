"""Create a graphical overview of all available colours."""

import sys
from pathlib import Path

# Ensure the local src package is imported instead of an installed one
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
for _mod in [m for m in sys.modules if m == "dbmarkenfarben" or m.startswith("dbmarkenfarben.")]:
    del sys.modules[_mod]

import dbmarkenfarben as dbmf
import matplotlib.pyplot as plt
import pandas as pd

assert dbmf.__file__ is not None and "src" in Path(dbmf.__file__).parts, (
    f"dbmarkenfarben imported from unexpected location: {dbmf.__file__}"
)

db_colors = dbmf.DeutscheBahnMarkenFarben()

dbcolor_names = [
    # 900 to 100
    'grey',
    'db-red',
    'lilac',
    's-bahn-green',
    # 500 only
    'cold-black',
    'ersatzverkehrs-purpur',
    'service-rot',
    'wegeleitung-blau',
    'white'
    ]

dbcolor_shades = [
    900,
    800, 700,
    600, 500,
    400, 300,
    200, 100,
    None
    ]

df = pd.DataFrame(
    index=[str(i) for i in dbcolor_shades],
    columns=dbcolor_names
    )

# Populate dataframe
for name in dbcolor_names:
    for shade in dbcolor_shades:
        print(name, shade)
        df.loc[str(shade), name] = db_colors.get(name, shade) or '#ffffff'

# %% Plot

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
ax.set_xlabel("Farbenname")
ax.set_ylabel("Shade")
ax.set_title("Übersicht Deutsche Bahn Markenfarben")

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
plt.savefig('overview.png', bbox_inches='tight', dpi=300)

# Show the plot
plt.show()
