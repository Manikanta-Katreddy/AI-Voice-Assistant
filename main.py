import threading
import pyttsx3

from apex_gui import (
    app,
    run_gui,
    add_user_message,
    add_apex_message,
    update_status
)

from modules.voice import listen
from modules.wakeword import is_wake_word
from modules.brain import process_command

# ---------------------------
# TEXT TO SPEECH
# ---------------------------

def speak(text):

    update_status("🟢 Speaking")

    add_apex_message(text)

    engine = pyttsx3.init()

    engine.setProperty("rate", 170)

    engine.say(text)

    engine.runAndWait()

    engine.stop()

    update_status("🔵 Listening")


# ---------------------------
# APEX LOOP
# ---------------------------

def apex_loop():

    while True:

        update_status("🔴 Sleeping")

        text = listen(timeout=10)

        if not text:
            continue

        add_user_message(text)

        if is_wake_word(text):

            update_status("🔵 Listening")

            speak("Yes Boss")

            speak("How can I help you today")

            # -----------------
            # Conversation Mode
            # -----------------

            while True:

                command = listen(timeout=10)

                if command:

                    add_user_message(command)

                    # Sleep Commands

                    if command.lower() in [
                        "sleep",
                        "sleep apex",
                        "go to sleep",
                        "exit",
                        "stop"
                    ]:

                        speak("Going to sleep boss")

                        update_status("🔴 Sleeping")

                        break

                    # Process Command

                    response = process_command(command)

                    speak(response)

                    continue

                # -----------------
                # Reminder
                # -----------------

                speak("Anything else boss")

                command = listen(timeout=5)

                if command:

                    add_user_message(command)

                    if command.lower() in [
                        "sleep",
                        "sleep apex",
                        "go to sleep",
                        "exit",
                        "stop"
                    ]:

                        speak("Going to sleep boss")

                        update_status("🔴 Sleeping")

                        break

                    response = process_command(command)

                    speak(response)

                    continue

                # -----------------
                # Sleep Mode
                # -----------------

                speak("You are not saying anything")

                speak("I am going to sleep mode")

                speak("Call me when you need me boss")

                update_status("🔴 Sleeping")

                break


# ---------------------------
# START THREAD
# ---------------------------

voice_thread = threading.Thread(
    target=apex_loop,
    daemon=True
)

voice_thread.start()

# ---------------------------
# START GUI
# ---------------------------

run_gui()