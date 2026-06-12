import speech_recognition as sr


def listen(timeout=5):

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        try:

            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=5
            )

            text = recognizer.recognize_google(audio)

            return text.lower()

        except:
            return None