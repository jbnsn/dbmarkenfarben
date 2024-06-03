"""Deutsche Bahn Markenfarben."""


class DeutscheBahnMarkenFarben:
    """
    Brand colours of Deutsche Bahn AG.

    https://marketingportal.extranet.deutschebahn.com/marketingportal/Marke-und-Design/Basiselemente/Farbe

    Example usage:

        dbmf = DeutscheBahnMarkenFarben()

        dbmf.print_colors()  # Print and return a list of available colours.
        dbmf.get('red')  # Returns '#ec0016'
        dbmf.get('red', 200, 'rgb')  # Returns (252, 200, 195)

    """

    def __init__(self):
        self.colors = {

            # ---- Blue
            ('blue', 100): '#E0EFFB',
            ('blue', 200): '#B4D5F6',
            ('blue', 300): '#73AEF4',
            ('blue', 400): '#347DE0',
            ('blue', 500): '#1455C0',
            ('blue', 600): '#0C3992',
            ('blue', 700): '#0A1E6E',
            ('blue', 800): '#061350',

            # ---- Burgundy
            ('burgundy', 100): '#F4E8ED',
            ('burgundy', 200): '#EDCBD6',
            ('burgundy', 300): '#DA9AA8',
            ('burgundy', 400): '#C0687B',
            ('burgundy', 500): '#A9455D',
            ('burgundy', 600): '#8C2E46',
            ('burgundy', 700): '#641E32',
            ('burgundy', 800): '#4D0820',

            # ---- Cool gray
            ('cool-grey', 100): '#f0f3f5',
            ('cool-grey', 200): '#d7dce1',
            ('cool-grey', 300): '#afb4bb',
            ('cool-grey', 400): '#878c96',
            ('cool-grey', 500): '#646973',
            ('cool-grey', 600): '#3c414b',
            ('cool-grey', 700): '#282d37',
            ('cool-grey', 800): '#131821',

            # ---- Cyan
            ('cyan', 100): '#E5FAFF',
            ('cyan', 200): '#BBE6F8',
            ('cyan', 300): '#84CFEF',
            ('cyan', 400): '#55B9E6',
            ('cyan', 500): '#309FD1',
            ('cyan', 600): '#0087B9',
            ('cyan', 700): '#006A96',
            ('cyan', 800): '#004B6D',

            # ---- Green
            ('green', 100): '#E2F3E5',
            ('green', 200): '#BDDBB9',
            ('green', 300): '#8CBC80',
            ('green', 400): '#8CBC80',
            ('green', 500): '#408335',
            ('green', 600): '#2A7230',
            ('green', 700): '#165C27',
            ('green', 800): '#154A26',

            # ---- Light green
            ('light-green', 100): '#EBF7DD',
            ('light-green', 200): '#C9EB9E',
            ('light-green', 300): '#9FD45F',
            ('light-green', 400): '#78BE14',
            ('light-green', 500): '#63A615',
            ('light-green', 600): '#508B1B',
            ('light-green', 700): '#44741A',
            ('light-green', 800): '#375F15',

            # ---- Orange
            ('orange', 100): '#FFF4D8',
            ('orange', 200): '#FCE3B4',
            ('orange', 300): '#FACA7F',
            ('orange', 400): '#F8AB37',
            ('orange', 500): '#F39200',
            ('orange', 600): '#D77B00',
            ('orange', 700): '#C05E00',
            ('orange', 800): '#A24800',

            # ---- Pink
            ('pink', 100): '#FDEEF8',
            ('pink', 200): '#F9D2E5',
            ('pink', 300): '#F4AECE',
            ('pink', 400): '#EE7BAE',
            ('pink', 500): '#E93E8F',
            ('pink', 600): '#DB0078',
            ('pink', 700): '#B80065',
            ('pink', 800): '#970052',

            # ---- Red
            ('red', 100): '#fee6e6',
            ('red', 200): '#fcc8c3',
            ('red', 300): '#fa9090',
            ('red', 400): '#f75056',
            ('red', 500): '#ec0016',
            ('red', 600): '#C50014',
            ('red', 700): '#9B000E',
            ('red', 800): '#740009',

            # ---- Turquoise
            ('turquoise', 100): '#E3F5F4',
            ('turquoise', 200): '#BEE2E5',
            ('turquoise', 300): '#3CB5AE',
            ('turquoise', 400): '#3CB5AE',
            ('turquoise', 500): '#00A099',
            ('turquoise', 600): '#008984',
            ('turquoise', 700): '#006E6B',
            ('turquoise', 800): '#005752',

            # ---- Violet
            ('violet', 100): '#F4EEFA',
            ('violet', 200): '#E0CDE4',
            ('violet', 300): '#C2A1C7',
            ('violet', 400): '#9A6CA6',
            ('violet', 500): '#814997',
            ('violet', 600): '#6E368C',
            ('violet', 700): '#581D70',
            ('violet', 800): '#421857',

            # ---- Warm cyan
            ('warm-cyan', 800): '#004b6d',
            ('warm-cyan', 700): '#006a96',
            ('warm-cyan', 600): '#0087b9',
            ('warm-cyan', 500): '#309fd1',
            ('warm-cyan', 400): '#55b9e6',
            ('warm-cyan', 300): '#84cfef',
            ('warm-cyan', 200): '#bbe6f8',
            ('warm-cyan', 100): '#e5faff',

            # ---- Warm grey
            ('warm-grey', 100): '#f5f4f1',
            ('warm-grey', 200): '#ddded6',
            ('warm-grey', 300): '#bcbbb2',
            ('warm-grey', 400): '#9c9a8e',
            ('warm-grey', 500): '#858379',
            ('warm-grey', 600): '#747067',
            ('warm-grey', 700): '#4f4b41',
            ('warm-grey', 800): '#38342f',

            # ---- Yellow
            ('yellow', 100): '#FFFFDC',
            ('yellow', 200): '#FFFFAF',
            ('yellow', 300): '#FFF876',
            ('yellow', 400): '#FFF000',
            ('yellow', 500): '#FFD800',
            ('yellow', 600): '#FFBB00',
            ('yellow', 700): '#FF9B00',
            ('yellow', 800): '#FF7A00',

        }

    def html_to_rgb(self, hex_color):
        """Convert HTML colour code to RGB colour code."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def get(
            self,
            color_name='red',
            color_saturation=500,
            return_format='html'
            ):
        """
        Get the color code for the given color name.

        Parameters
        ----------
        color_name : str
            Name of the Deutsche Bahn AG brand colour.
            https://marketingportal.extranet.deutschebahn.com/marketingportal/Marke-und-Design/Basiselemente/Farbe
        color_saturation : int, optional
            100, 200, 300, 400, 500, 600, 700 or 800. The default is 500.
        return_format : str, optional
            Whether to return the html or rgb colour code.
            The default is 'html'.

        Raises
        ------
        ValueError
            If the `color_name` is not available.

        Returns
        -------
        Color code : str (html) OR tuple (rgb)

        """
        if (color_name.lower(), color_saturation) not in self.colors:
            raise ValueError("Invalid color name.")

        if return_format == 'html':
            return self.colors[(color_name.lower(), color_saturation)]

        elif return_format == 'rgb':
            return self.html_to_rgb(
                self.colors[(color_name.lower(), color_saturation)]
                )
        else:
            raise ValueError("Invalid return format. Choose 'html' or 'rgb'.")

    def print_colors(self):
        """Print and return a list of available colours."""
        colors = sorted(set([k[0] for k in self.colors.keys()]))
        print(colors)
        return colors
