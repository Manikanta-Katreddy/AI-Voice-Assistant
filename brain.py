from modules.ai_engine import ask_ai
from datetime import datetime
import os
import webbrowser


def process_command(command):

    command = command.lower()

    print("COMMAND RECEIVED:", command)

    # -----------------------
    # TIME
    # -----------------------

    if "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}"

    # -----------------------
    # DATE
    # -----------------------

    elif "date" in command:

        current_date = datetime.now().strftime("%d %B %Y")

        return f"Today's date is {current_date}"

    # -----------------------
    # GREETING
    # -----------------------

    elif "hello" in command:

        return "Hello boss. How are you today?"

    # -----------------------
    # OPEN GOOGLE
    # -----------------------

    elif "google" in command:

        webbrowser.open("https://www.google.com")

        return "Opening Google"

    # -----------------------
    # OPEN YOUTUBE
    # -----------------------

    elif "youtube" in command:

        webbrowser.open("https://www.youtube.com")

        return "Opening YouTube"

    # -----------------------
    # OPEN CHATGPT
    # -----------------------

    elif "chatgpt" in command:

        webbrowser.open("https://chatgpt.com")

        return "Opening ChatGPT"

    # -----------------------
    # OPEN GITHUB
    # -----------------------

    elif "github" in command:

        webbrowser.open("https://github.com")

        return "Opening GitHub"

    # -----------------------
    # OPEN LINKEDIN
    # -----------------------

    elif "linkedin" in command:

        webbrowser.open("https://linkedin.com")

        return "Opening LinkedIn"

    # -----------------------
    # OPEN CALCULATOR
    # -----------------------

    elif "calculator" in command:

        os.system("start calc")

        return "Opening Calculator"

    # -----------------------
    # OPEN NOTEPAD
    # -----------------------

    elif "notepad" in command:

        os.system("start notepad")

        return "Opening Notepad"

    # -----------------------
    # OPEN PAINT
    # -----------------------

    elif "paint" in command:

        os.system("start mspaint")

        return "Opening Paint"

    # -----------------------
    # OPEN FILE EXPLORER
    # -----------------------

    elif "file explorer" in command:

        os.system("explorer")

        return "Opening File Explorer"

    # -----------------------
    # DEFAULT
    # -----------------------

    else:

        return ask_ai(command)