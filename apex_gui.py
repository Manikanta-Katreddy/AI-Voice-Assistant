import customtkinter as ctk

# --------------------------------
# GUI SETTINGS
# --------------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --------------------------------
# MAIN WINDOW
# --------------------------------

app = ctk.CTk()

app.title("APEX AI Assistant")
app.geometry("1200x750")
app.configure(fg_color="#0B0F19")

# --------------------------------
# ANIMATION DATA
# --------------------------------

wave_frames = [
    "▁▂▃▄▅▆▇█",
    "▂▃▄▅▆▇█▇",
    "▃▄▅▆▇█▇▆",
    "▄▅▆▇█▇▆▅",
    "▅▆▇█▇▆▅▄",
    "▆▇█▇▆▅▄▃",
    "▇█▇▆▅▄▃▂",
    "█▇▆▅▄▃▂▁"
]

frame_index = 0

# --------------------------------
# HEADER
# --------------------------------

title = ctk.CTkLabel(
    app,
    text="⚡ APEX",
    font=("Arial", 42, "bold"),
    text_color="#00D4FF"
)
title.pack(pady=(15, 5))

# --------------------------------
# MICROPHONE
# --------------------------------

mic_label = ctk.CTkLabel(
    app,
    text="🎤",
    font=("Arial", 70)
)
mic_label.pack()

# --------------------------------
# WAVE ANIMATION
# --------------------------------

wave_label = ctk.CTkLabel(
    app,
    text=wave_frames[0],
    font=("Consolas", 28),
    text_color="#00D4FF"
)
wave_label.pack(pady=5)

# --------------------------------
# STATUS
# --------------------------------

status_label = ctk.CTkLabel(
    app,
    text="🔴 Sleeping",
    font=("Arial", 20, "bold"),
    text_color="red"
)
status_label.pack(pady=5)

# --------------------------------
# CHAT FRAME
# --------------------------------

chat_frame = ctk.CTkFrame(
    app,
    fg_color="#151B2D",
    corner_radius=15
)

chat_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

# --------------------------------
# CHAT BOX
# --------------------------------

chat_box = ctk.CTkTextbox(
    chat_frame,
    font=("Consolas", 15),
    fg_color="#151B2D",
    text_color="white"
)

chat_box.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

# --------------------------------
# FUNCTIONS
# --------------------------------

def add_user_message(text):
    chat_box.insert(
        "end",
        f"\n👤 USER : {text}\n"
    )
    chat_box.see("end")


def add_apex_message(text):
    chat_box.insert(
        "end",
        f"🤖 APEX : {text}\n"
    )
    chat_box.see("end")


def update_status(text):

    status_label.configure(text=text)

    if "Sleeping" in text:
        status_label.configure(text_color="red")
        mic_label.configure(text="🎤")

    elif "Listening" in text:
        status_label.configure(text_color="cyan")
        mic_label.configure(text="🎙️")

    elif "Processing" in text:
        status_label.configure(text_color="yellow")
        mic_label.configure(text="⚙️")

    elif "Speaking" in text:
        status_label.configure(text_color="green")
        mic_label.configure(text="🔊")


def clear_chat():

    chat_box.delete("1.0", "end")

    add_apex_message(
        "Chat cleared successfully."
    )


def animate_wave():

    global frame_index

    wave_label.configure(
        text=wave_frames[frame_index]
    )

    frame_index += 1

    if frame_index >= len(wave_frames):
        frame_index = 0

    app.after(200, animate_wave)


# --------------------------------
# BUTTON FRAME
# --------------------------------

button_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

button_frame.pack(pady=10)

# --------------------------------
# CLEAR BUTTON
# --------------------------------

clear_btn = ctk.CTkButton(
    button_frame,
    text="Clear Chat",
    width=150,
    command=clear_chat
)

clear_btn.pack(
    side="left",
    padx=10
)

# --------------------------------
# EXIT BUTTON
# --------------------------------

exit_btn = ctk.CTkButton(
    button_frame,
    text="Exit",
    width=150,
    command=app.destroy
)

exit_btn.pack(
    side="left",
    padx=10
)

# --------------------------------
# STARTUP MESSAGE
# --------------------------------

add_apex_message(
    "Apex Assistant Started Successfully."
)

# --------------------------------
# START ANIMATION
# --------------------------------

animate_wave()

# --------------------------------
# RUN APP
# --------------------------------
def run_gui():
    app.mainloop()


if __name__ == "__main__":
    run_gui()