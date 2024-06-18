# Deutsche Bahn Markenfarben
Get the html or rgb code of one of the [Deutsche Bahn AG brand colours](https://marketingportal.extranet.deutschebahn.com/marketingportal/Marke-und-Design/Basiselemente/Farbe).

`['blue', 'burgundy', 'cool-grey', 'cyan', 'green', 'light-green', 'orange', 'pink', 'red', 'turquoise', 'violet', 'warm-cyan', 'warm-grey', 'yellow']`

![Brand colours of Deutsche Bahn AG](https://marketingportal.extranet.deutschebahn.com/resource/blob/9688184/6b6042de4d93449f5546cdd01ca94ebe/Bild_1-data.png)

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

db_colors.print_colors()  # Prints and returns a list of available colours.

db_colors.colors  # Returns a dictionary of available colours.

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
        Name of the brand colour of Deutsche Bahn AG.
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