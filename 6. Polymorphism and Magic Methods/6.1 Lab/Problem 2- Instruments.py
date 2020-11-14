

def play_instrument(instrument: 'Instrument'):
    return instrument.play()


class Guitar:

    @staticmethod
    def play():
        print("playing the guitar")


guitar = Guitar()
play_instrument(guitar)
