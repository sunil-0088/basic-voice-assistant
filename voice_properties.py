import pyttsx3

engine = pyttsx3.init()


def voice_rate(value):
    engine.setProperty('rate', value)


def voice_type(val):
    # 0 for male
    # 1 for female
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[val].id)


def volume(val):
    engine.setProperty('volume', val)  # between 0 to 1





