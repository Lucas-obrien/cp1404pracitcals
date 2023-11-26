"""
Band constructor

Estimation : 30 mins
Actual : 45 mins

"""


class Band:
    """Band object constructor."""

    def __init__(self, band_name=""):
        """Initialise a Band."""
        self.band_name = band_name
        self.band_lineup = []

    def add(self, musician):
        """Add a musician to the band."""
        self.band_lineup.append(musician)

    def __str__(self):
        """Construct a string representation of the band."""
        musician_list = []
        for musician in self.band_lineup:
            musician_list.append(str(musician))
        return f"{self.band_name} ({', '.join(musician_list)})"

        # pass

    def play(self):
        """Band plays a gig."""
        play_list = []
        for musician in self.band_lineup:
            play_list.append(musician.play())
        return '\n'.join(play_list)

    def __repr__(self):
        """Repr of band."""
        return f"{self.band_name} ({self.band_lineup})"
