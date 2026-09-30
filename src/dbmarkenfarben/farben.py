"""Deutsche Bahn Markenfarben."""

import logging

logger = logging.getLogger(__name__)


class DeutscheBahnMarkenFarben:
    """
    Brand colours of Deutsche Bahn AG.

    https://marketingportal.extranet.deutschebahn.com/marketingportal/Marke-und-Design/Basiselemente/Markenfarben

    Example usage:

        dbmf = DeutscheBahnMarkenFarben()

        dbmf.print_colors()  # Print and return a list of available colours.
        dbmf.get('red')  # Returns '#ec0016'
        dbmf.get('red', 200, 'rgb')  # Returns (252, 200, 195)

        html_color_palette = [dbmf.get(i) for i in dbmf.print_colors()]

    """

    def __init__(self):
        self.colors = {

            # ---- Grey

            ('grey', 25): '#F4F4F6',
            ('grey', 50): '#E0E1E4',
            ('grey', 100): '#C9CCD2',
            ('grey', 200): '#A3A8B2',
            ('grey', 300): '#848B9A',
            ('grey', 400): '#767E8F',
            ('grey', 500): '#6B7282',
            ('grey', 600): '#596273',
            ('grey', 700): '#454D5D',
            ('grey', 800): '#262C38',
            ('grey', 900): '#090F1B',

            # ---- DB Red

            ('db-red', 25): '#FEEFF0',
            ('db-red', 50): '#FFD7DC',
            ('db-red', 100): '#FDB7BF',
            ('db-red', 200): '#FC808C',
            ('db-red', 300): '#FA4A59',
            ('db-red', 400): '#FF002B',
            ('db-red', 500): '#EC0016',
            ('db-red', 600): '#C20012',
            ('db-red', 700): '#9E000F',
            ('db-red', 800): '#5F0009',
            ('db-red', 900): '#2A0000',

            # ---- Lilac

            ('lilac', 25): '#F5F2FF',
            ('lilac', 50): '#E4DBFF',
            ('lilac', 100): '#CCBEFF',
            ('lilac', 200): '#AA99FF',
            ('lilac', 300): '#8E80D4',
            ('lilac', 400): '#8174BF',
            ('lilac', 500): '#7569AC',
            ('lilac', 600): '#62588F',
            ('lilac', 700): '#4E4770',
            ('lilac', 800): '#2C283C',
            ('lilac', 900): '#100F15',

            # ---- S-Bahn Green

            ('s-bahn-green', 25): '#E2F3E5',
            ('s-bahn-green', 50): '#D8EEDA',
            ('s-bahn-green', 100): '#CCE7CC',
            ('s-bahn-green', 200): '#BDDBB9',
            ('s-bahn-green', 300): '#8CBC80',
            ('s-bahn-green', 400): '#66A558',
            ('s-bahn-green', 500): '#408335',
            ('s-bahn-green', 600): '#2A7230',
            ('s-bahn-green', 700): '#165C27',
            ('s-bahn-green', 800): '#154A26',
            ('s-bahn-green', 900): '#0C3B1B',

            # ---------------------------- #
            # Funktionale Identitätsfarben #
            # ---------------------------- #

            ('wegeleitung-blau', None): '#21276B',  # Wegeleitung: RAL 5022 Nachtblau
            ('ersatzverkehrs-purpur', None): '#9B1B60',  # Ersatzverkehr: Verkehrspurpur
            ('service-rot', None): '#4D0820',  # Service-Rot: Port Royal
            ('cold-black', None): '#090F1B',  # Cold Black
            ('white', None): '#FFFFFF',  # White

            # ---------- #
            # DEPRECATED #
            # ---------- #

            # ---- Legacy Blue

            ('legacy-blue', 100): '#E0EFFB',
            ('legacy-blue', 200): '#B4D5F6',
            ('legacy-blue', 300): '#73AEF4',
            ('legacy-blue', 400): '#347DE0',
            ('legacy-blue', 500): '#1455C0',
            ('legacy-blue', 600): '#0C3992',
            ('legacy-blue', 700): '#0A1E6E',
            ('legacy-blue', 800): '#061350',

            # ---- Legacy Burgundy

            ('legacy-burgundy', 100): '#F4E8ED',
            ('legacy-burgundy', 200): '#EDCBD6',
            ('legacy-burgundy', 300): '#DA9AA8',
            ('legacy-burgundy', 400): '#C0687B',
            ('legacy-burgundy', 500): '#A9455D',
            ('legacy-burgundy', 600): '#8C2E46',
            ('legacy-burgundy', 700): '#641E32',
            ('legacy-burgundy', 800): '#4D0820',

            # ---- Legacy Cool gray

            ('legacy-cool-grey', 100): '#f0f3f5',
            ('legacy-cool-grey', 200): '#d7dce1',
            ('legacy-cool-grey', 300): '#afb4bb',
            ('legacy-cool-grey', 400): '#878c96',
            ('legacy-cool-grey', 500): '#646973',
            ('legacy-cool-grey', 600): '#3c414b',
            ('legacy-cool-grey', 700): '#282d37',
            ('legacy-cool-grey', 800): '#131821',

            # ---- Legacy Cyan

            ('legacy-cyan', 100): '#E5FAFF',
            ('legacy-cyan', 200): '#BBE6F8',
            ('legacy-cyan', 300): '#84CFEF',
            ('legacy-cyan', 400): '#55B9E6',
            ('legacy-cyan', 500): '#309FD1',
            ('legacy-cyan', 600): '#0087B9',
            ('legacy-cyan', 700): '#006A96',
            ('legacy-cyan', 800): '#004B6D',

            # ---- Legacy Green

            ('legacy-green', 100): '#E2F3E5',
            ('legacy-green', 200): '#BDDBB9',
            ('legacy-green', 300): '#8CBC80',
            ('legacy-green', 400): '#66A558',
            ('legacy-green', 500): '#408335',
            ('legacy-green', 600): '#2A7230',
            ('legacy-green', 700): '#165C27',
            ('legacy-green', 800): '#154A26',

            # ---- Legacy Light green

            ('legacy-light-green', 100): '#EBF7DD',
            ('legacy-light-green', 200): '#C9EB9E',
            ('legacy-light-green', 300): '#9FD45F',
            ('legacy-light-green', 400): '#78BE14',
            ('legacy-light-green', 500): '#63A615',
            ('legacy-light-green', 600): '#508B1B',
            ('legacy-light-green', 700): '#44741A',
            ('legacy-light-green', 800): '#375F15',

            # ---- Legacy Orange

            ('legacy-orange', 100): '#FFF4D8',
            ('legacy-orange', 200): '#FCE3B4',
            ('legacy-orange', 300): '#FACA7F',
            ('legacy-orange', 400): '#F8AB37',
            ('legacy-orange', 500): '#F39200',
            ('legacy-orange', 600): '#D77B00',
            ('legacy-orange', 700): '#C05E00',
            ('legacy-orange', 800): '#A24800',

            # ---- Legacy Pink

            ('legacy-pink', 100): '#FDEEF8',
            ('legacy-pink', 200): '#F9D2E5',
            ('legacy-pink', 300): '#F4AECE',
            ('legacy-pink', 400): '#EE7BAE',
            ('legacy-pink', 500): '#E93E8F',
            ('legacy-pink', 600): '#DB0078',
            ('legacy-pink', 700): '#B80065',
            ('legacy-pink', 800): '#970052',

            # ---- Legacy Red

            ('legacy-red', 100): '#fee6e6',
            ('legacy-red', 200): '#fcc8c3',
            ('legacy-red', 300): '#fa9090',
            ('legacy-red', 400): '#f75056',
            ('legacy-red', 500): '#ec0016',
            ('legacy-red', 600): '#C50014',
            ('legacy-red', 700): '#9B000E',
            ('legacy-red', 800): '#740009',

            # ---- Legacy Turquoise

            ('legacy-turquoise', 100): '#E3F5F4',
            ('legacy-turquoise', 200): '#BEE2E5',
            ('legacy-turquoise', 300): '#83CACA',
            ('legacy-turquoise', 400): '#3CB5AE',
            ('legacy-turquoise', 500): '#00A099',
            ('legacy-turquoise', 600): '#008984',
            ('legacy-turquoise', 700): '#006E6B',
            ('legacy-turquoise', 800): '#005752',

            # ---- Legacy Violet

            ('legacy-violet', 100): '#F4EEFA',
            ('legacy-violet', 200): '#E0CDE4',
            ('legacy-violet', 300): '#C2A1C7',
            ('legacy-violet', 400): '#9A6CA6',
            ('legacy-violet', 500): '#814997',
            ('legacy-violet', 600): '#6E368C',
            ('legacy-violet', 700): '#581D70',
            ('legacy-violet', 800): '#421857',

            # ---- Legacy Warm grey

            ('legacy-warm-grey', 100): '#f5f4f1',
            ('legacy-warm-grey', 200): '#ddded6',
            ('legacy-warm-grey', 300): '#bcbbb2',
            ('legacy-warm-grey', 400): '#9c9a8e',
            ('legacy-warm-grey', 500): '#858379',
            ('legacy-warm-grey', 600): '#747067',
            ('legacy-warm-grey', 700): '#4f4b41',
            ('legacy-warm-grey', 800): '#38342f',

            # ---- Legacy Yellow

            ('legacy-yellow', 100): '#FFFFDC',
            ('legacy-yellow', 200): '#FFFFAF',
            ('legacy-yellow', 300): '#FFF876',
            ('legacy-yellow', 400): '#FFF000',
            ('legacy-yellow', 500): '#FFD800',
            ('legacy-yellow', 600): '#FFBB00',
            ('legacy-yellow', 700): '#FF9B00',
            ('legacy-yellow', 800): '#FF7A00',

        }

    def html_to_rgb(self, hex_color):
        """Convert HTML colour code to RGB colour code."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def get(
            self,
            color_name='red',
            color_saturation=None,
            return_format='html'
            ):
        """
        Get the color code for the given Deutsche Bahn brand color.

        Reference:
        https://marketingportal.extranet.deutschebahn.com/marketingportal/Marke-und-Design/Basiselemente/Farbe

        Parameters
        ----------
        color_name : str
            Name of the Deutsche Bahn AG brand colour.
        color_saturation : int, optional
            100, 200, 300, 400, 500, 600, 700 or 800. The default is None.
        return_format : str, optional
            Whether to return the html or rgb colour code.
            The default is 'html'.

        Returns
        -------
        Color code : str (html) OR tuple (rgb), or None if `color_name` is
        not available (logged as an error).

        """
        
        if (color_saturation is None
            and (color_name.lower(), None) not in self.colors):
            # Fall back to the standard saturation if no single-shade color exists
            color_saturation = 500

        if (color_name.lower(), color_saturation) not in self.colors:
            # Log the error without aborting the caller
            logger.error("Invalid color name: %r, color_saturation: %r", color_name, color_saturation)
            return None

        if 'legacy' in color_name.lower():
            _url = 'https://marketingportal.extranet.deutschebahn.com/marketingportal/Marke-und-Design/Basiselemente/Markenfarben'
            logger.warning("Legacy color. See '%s' for current colors.", _url)

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
        colors = [
            c for c in sorted(set([k[0] for k in self.colors.keys()]))
            if 'legacy' not in c
            ]

        print(colors)

        return colors

if __name__ == '__main__':

    db_colors = DeutscheBahnMarkenFarben()

    # Print and return a list of the names of the available colours.
    db_colors.print_colors()

    # Return a dictionary containing the names, shades
    # and html codes of the available colours.
    db_colors.colors

    [i for i in db_colors.colors if i[0] == 'db-red']  # ... only reds

    db_colors.get('db-red')  # Returns '#ec0016'
    db_colors.get('db-red', 200)  # Returns '#fcc8c3'
    db_colors.get('db-red', 200, 'rgb')  # Returns (252, 200, 195)
    db_colors.get('db-red', None)
    db_colors.get('wegeleitung-blau')
    db_colors.get('wegeleitung-blau', 500)
    db_colors.get('wegeleitung-blau', None)
