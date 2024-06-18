"""Tests."""

import src.dbmarkenfarben as dbmf

db_colors = dbmf.DeutscheBahnMarkenFarben()

db_colors.colors

db_colors.get('red')
db_colors.get('red', 200)
