# Deutsche Bahn Markenfarben
Get the html or rgb code of one of the [Deutsche Bahn AG brand colors](https://marketingportal.extranet.deutschebahn.com/marketingportal/Marke-und-Design/Basiselemente/Markenfarben).

**Application examples** *([full example](https://github.com/jbnsn/dbmarkenfarben?tab=readme-ov-file#example-usage)***):**
```Python
db_colors.get('red')  # Returns '#ec0016'
db_colors.get('red', 200)  # Returns '#fcc8c3'
db_colors.get('red', 200, 'rgb')  # Returns (252, 200, 195)
```

![Brand colors of Deutsche Bahn AG](overview/overview.png)

`['cold-black', 'db-red', 'ersatzverkehrs-purpur', 'grey', 'lilac', 's-bahn-green', 'service-rot', 'wegeleitung-blau', 'white']`

## Install and Update

*dbmarkenfarben* is available via [PyPi](https://pypi.org/project/dbmarkenfarben/).

### Install

```Python
pip install dbmarkenfarben
```

### Update

```Python
pip install --upgrade dbmarkenfarben
```
or
```
pip install -U dbmarkenfarben
```

## Example usage

```Python

import dbmarkenfarben as dbmf

db_colors = dbmf.DeutscheBahnMarkenFarben()

db_colors.print_colors()  # Prints and returns a list of available colors.

db_colors.colors  # Returns a dictionary of available colors.

db_colors.get('red')  # Returns '#ec0016'
db_colors.get('red', 200)  # Returns '#fcc8c3'
db_colors.get('red', 200, 'rgb')  # Returns (252, 200, 195)

```

## `get` function

```Python
get(
    color_name,
    color_saturation=500,
    return_format='html'
    ):
    """
    Get the color code for the given color name.

    Parameters
    ----------
    color_name : str
        Name of the brand color of Deutsche Bahn AG.
        https://marketingportal.extranet.deutschebahn.com/marketingportal/Marke-und-Design/Basiselemente/Farbe
    color_saturation : int, optional
        100, 200, 300, 400, 500, 600, 700 or 800. The default is 500.
    return_format : str, optional
        Whether the html or rgb color code shall be returnd.
        The default is 'html'.

    Raises
    ------
    ValueError
        Invalid return format.

    Returns
    -------
    Color code : str (html) OR tuple (rgb)

    """
```

# Quick and dirty
```Python
"""A quick and dirty code for the use of all the DB brand colors."""

import pandas as pd


class DeutscheBahnMarkenFarben:
    """Initiate `DeutscheBahnMarkenFarben` class."""

    def __init__(self):
        self.colors = (
            pd.DataFrame(
                {"grey": ["#C9CCD2", "#A3A8B2", "#848B9A", "#767E8F",
                          "#6B7282", "#596273", "#454D5D", "#262C38"],
                 "db-red": ["#FDB7BF", "#FC808C", "#FA4A59", "#FF002B",
                            "#EC0016", "#C20012", "#9E000F", "#5F0009"],
                 "lilac": ["#CCBEFF", "#AA99FF", "#8E80D4", "#8174BF",
                           "#7569AC", "#62588F", "#4E4770", "#2C283C"],
                 "s-bahn-green": ["#CCE7CC", "#BDDBB9", "#8CBC80", "#66A558",
                                  "#408335", "#2A7230", "#165C27", "#154A26"]},
                index=[100, 200, 300, 400, 500, 600, 700, 800]
                )
            )
        self.function_colors = {
            "wegeleitung-blau": "#21276B",
            "ersatzverkehrs-purpur": "#9B1B60",
            "service-rot": "#4D0820",
            "cold-black": "#090F1B",
            "white": "#FFFFFF",
            }

    def get(self, color_name='red', color_saturation=500):
        """Return the HEX code of a color."""
        if color_name in self.function_colors:
            return self.function_colors[color_name]
        try:
            return self.colors.T.loc[color_name, color_saturation]
        except KeyError:
            print(f"KeyError: '{color_name} {color_saturation}'"
                  " is not a valid color!")


db_colors = DeutscheBahnMarkenFarben()

db_colors.get('db-red')  # Equivalent to db_colors.get('db-red', 500); Returns '#EC0016';
db_colors.get('db-red', 400)  # Returns '#FF002B'
db_colors.get('white')  # Returns '#FFFFFF'

```
