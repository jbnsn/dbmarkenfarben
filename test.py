"""Tests."""

import src.dbmarkenfarben as dbmf

db_colors = dbmf.DeutscheBahnMarkenFarben()

# Print and return a list of the names of the available colours.
db_colors.print_colors()

# Return a dictionary containing the names, shades
# and html codes of the available colours.
db_colors.colors

[i for i in db_colors.colors if i[0] == 'red']  # ... only reds

db_colors.get('red')  # Returns '#ec0016'
db_colors.get('red', 200)  # Returns '#fcc8c3'
db_colors.get('red', 200, 'rgb')  # Returns (252, 200, 195)
