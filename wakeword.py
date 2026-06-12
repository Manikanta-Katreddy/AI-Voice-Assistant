def is_wake_word(text):

    wake_words = [
        "hey apex",
        "apex",
        "hi apex",
        "hello apex",
        "okay apex",
        "hey alex",
        "apex assistant"
    ]

    if not text:
        return False

    text = text.lower()

    return any(
        word in text
        for word in wake_words
    )