"""Different ways to store all the DB brand colours in a dataframe."""

import dbmarkenfarben as dbmf
import pandas as pd
import io

# ---- Variant 1

db_colors = pd.read_csv(
    io.StringIO(
        """
        100,200,300,400,500,600,700,800
        #E0EFFB,#B4D5F6,#73AEF4,#347DE0,#1455C0,#0C3992,#0A1E6E,#061350
        #F4E8ED,#EDCBD6,#DA9AA8,#C0687B,#A9455D,#8C2E46,#641E32,#4D0820
        #f0f3f5,#d7dce1,#afb4bb,#878c96,#646973,#3c414b,#282d37,#131821
        #E5FAFF,#BBE6F8,#84CFEF,#55B9E6,#309FD1,#0087B9,#006A96,#004B6D
        #E2F3E5,#BDDBB9,#8CBC80,#66A558,#408335,#2A7230,#165C27,#154A26
        #EBF7DD,#C9EB9E,#9FD45F,#78BE14,#63A615,#508B1B,#44741A,#375F15
        #FFF4D8,#FCE3B4,#FACA7F,#F8AB37,#F39200,#D77B00,#C05E00,#A24800
        #FDEEF8,#F9D2E5,#F4AECE,#EE7BAE,#E93E8F,#DB0078,#B80065,#970052
        #fee6e6,#fcc8c3,#fa9090,#f75056,#ec0016,#C50014,#9B000E,#740009
        #E3F5F4,#BEE2E5,#83CACA,#3CB5AE,#00A099,#008984,#006E6B,#005752
        #F4EEFA,#E0CDE4,#C2A1C7,#9A6CA6,#814997,#6E368C,#581D70,#421857
        #e5faff,#bbe6f8,#84cfef,#55b9e6,#309fd1,#0087b9,#006a96,#004b6d
        #f5f4f1,#ddded6,#bcbbb2,#9c9a8e,#858379,#747067,#4f4b41,#38342f
        #FFFFDC,#FFFFAF,#FFF876,#FFF000,#FFD800,#FFBB00,#FF9B00,#FF7A00
        """
        .strip()
        )
    )

# ---- Variant 2

db_colors = dbmf.DeutscheBahnMarkenFarben()

db_colors = (
      pd.Series(
          db_colors.colors.values(),
          index=db_colors.colors.keys()
          )
      .unstack(level=0)
      .transpose()
      )

# ---- Variant 3

db_colors = pd.read_csv(
    "https://github.com/jbnsn/dbmarkenfarben/blob/main/overview/colors.csv?raw=true",
    )

# ---- Save

# db_colors.to_csv("./overview/colors.csv", index=False)
