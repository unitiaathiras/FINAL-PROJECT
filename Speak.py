import pyttsx3


def Say(Text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)

    print("   ")
    print(f"ADORA: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("   ")
