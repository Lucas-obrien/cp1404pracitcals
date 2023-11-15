class Band:

    def __init__(self, band_name=""):
        self.band_name = band_name
        self.band_lineup = []

    def add(self, musician):
        self.band_lineup.append(musician)

    def __str__(self):
        musician_list = []
        for musician in self.band_lineup:
            musician_list.append(str(musician))
        return f"{self.band_name} ({', '.join(musician_list)})"

        # pass

    def play(self):
        play_list = []
        for musician in self.band_lineup:
            play_list.append(musician.play())
        return '\n'.join(play_list)

    def __repr__(self):
        return f"{self.band_name} ({self.band_lineup})"
        # pass
