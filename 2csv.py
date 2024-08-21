"""
Save a dataframe of all Deutsche Bahn brand colours as a CSV file.

db_colors = pd.read_csv(
    "https://github.com/jbnsn/dbmarkenfarben/blob/main/overview/colors.csv?raw=true",
    )

"""

import dbmarkenfarben as dbmf
import pandas as pd

db_colors = dbmf.DeutscheBahnMarkenFarben()

df = (
      pd.Series(
          db_colors.colors.values(),
          index=db_colors.colors.keys()
          )
      .unstack(level=0)
      .transpose()
      )

df.to_csv("./overview/colors.csv", index=False)
