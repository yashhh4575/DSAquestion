import tkinter as tk
from tkinter import scrolledtext\

from openai import OpenAI

import pyttsx3
import speech_recognition as sr

import threading
import os
import json
from datetime import datetime


# =====================================================
# OPENAI
# =====================================================

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY is not set. "
        "Please set your OpenAI API key as an environment variable."
    )

client = OpenAI(api_key=api_key)


# =====================================================
# TEXT TO SPEECH
# =====================================================

speaker = pyttsx3.init()

speaker.setProperty("rate", 165)
speaker.setProperty("volume", 1.0)


def speak(text):
    try:
        speaker.say(text)
        speaker.runAndWait()
    except Exception:
        pass


# =====================================================
# CHAT MEMORY
# =====================================================

MEMORY_FILE = "mimi_memory.json"

conversation = []


def load_memory():

    global conversation

    try:

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            conversation = json.load(file)

    except:

        conversation = []


def save_memory():

    try:

        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                conversation,
                file,
                indent=4,
                ensure_ascii=False
            )

    except Exception:
        pass


# Load previous memory
load_memory()


# =====================================================
# AI RESPONSE
# =====================================================

def get_ai_response(user_message):

    try:

        # Add user message to memory
        conversation.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        # Keep recent messages
        recent_messages = conversation[-20:]

        response = client.responses.create(

            model="gpt-5-mini",

            instructions="""
You are Mimi, a friendly personal AI assistant.

Your personality:
- Friendly
- Helpful
- Simple
- Clear
- Slightly fun

You help users with:
- Programming
- Python
- DSA
- College studies
- General questions
- Everyday tasks

Remember the conversation context provided to you.
If the user asks about something discussed earlier,
use the previous messages to understand the context.

Do not claim to have abilities that you don't have.
""",

            input=recent_messages
        )

        answer = response.output_text

        # Add Mimi response to memory
        conversation.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        save_memory()

        return answer

    except Exception as e:

        return (
            "Sorry 😔, I couldn't connect to the AI right now."
        )


# =====================================================
# SEND MESSAGE
# =====================================================

def send_message(event=None):

    message = entry.get().strip()

    if message == "":
        return

    entry.delete(
        0,
        tk.END
    )

    add_message(
        "You",
        message,
        "user"
    )

    status_label.config(
        text="🟡 Mimi is thinking..."
    )

    send_button.config(
        state=tk.DISABLED
    )

    voice_button.config(
        state=tk.DISABLED
    )

    threading.Thread(
        target=process_message,
        args=(message,),
        daemon=True
    ).start()


# =====================================================
# PROCESS AI
# =====================================================

def process_message(message):

    answer = get_ai_response(
        message
    )

    root.after(
        0,
        show_mimi_response,
        answer
    )


# =====================================================
# SHOW MIMI RESPONSE
# =====================================================

def show_mimi_response(answer):

    add_message(
        "Mimi",
        answer,
        "mimi"
    )

    status_label.config(
        text="🟢 Mimi is online"
    )

    send_button.config(
        state=tk.NORMAL
    )

    voice_button.config(
        state=tk.NORMAL
    )

    # Speak answer
    threading.Thread(
        target=speak,
        args=(answer,),
        daemon=True
    ).start()


# =====================================================
# ADD MESSAGE TO UI
# =====================================================

def add_message(sender, message, tag):

    chat_area.config(
        state=tk.NORMAL
    )

    time = datetime.now().strftime(
        "%I:%M %p"
    )

    if sender == "You":

        chat_area.insert(
            tk.END,
            f"\nYou  •  {time}\n",
            "user_name"
        )

        chat_area.insert(
            tk.END,
            f"{message}\n",
            "user_message"
        )

    else:

        chat_area.insert(
            tk.END,
            f"\n🤖 Mimi  •  {time}\n",
            "mimi_name"
        )

        chat_area.insert(
            tk.END,
            f"{message}\n",
            "mimi_message"
        )

    chat_area.config(
        state=tk.DISABLED
    )

    chat_area.see(
        tk.END
    )


# =====================================================
# VOICE INPUT
# =====================================================

def listen_voice():

    recognizer = sr.Recognizer()

    try:

        status_label.config(
            text="🎤 Listening..."
        )

        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        status_label.config(
            text="🔄 Converting speech..."
        )

        text = recognizer.recognize_google(
            audio
        )

        root.after(
            0,
            voice_received,
            text
        )

    except sr.WaitTimeoutError:

        root.after(
            0,
            lambda: status_label.config(
                text="⏱️ No speech detected"
            )
        )

    except sr.UnknownValueError:

        root.after(
            0,
            lambda: status_label.config(
                text="❌ Couldn't understand"
            )
        )

    except sr.RequestError:

        root.after(
            0,
            lambda: status_label.config(
                text="❌ Speech service unavailable"
            )
        )

    except Exception:

        root.after(
            0,
            lambda: status_label.config(
                text="❌ Microphone error"
            )
        )

    finally:

        root.after(
            0,
            lambda: voice_button.config(
                state=tk.NORMAL
            )
        )


# =====================================================
# VOICE MESSAGE RECEIVED
# =====================================================

def voice_received(text):

    entry.delete(
        0,
        tk.END
    )

    entry.insert(
        0,
        text
    )

    send_message()


# =====================================================
# START VOICE INPUT
# =====================================================

def start_voice():

    voice_button.config(
        state=tk.DISABLED
    )

    threading.Thread(
        target=listen_voice,
        daemon=True
    ).start()


# =====================================================
# CLEAR CHAT
# =====================================================

def clear_chat():

    global conversation

    conversation = []

    save_memory()

    chat_area.config(
        state=tk.NORMAL
    )

    chat_area.delete(
        "1.0",
        tk.END
    )

    chat_area.config(
        state=tk.DISABLED
    )

    add_message(
        "Mimi",
        "Hello! 👋 I'm Mimi. "
        "How can I help you today?",
        "mimi"
    )


# =====================================================
# GUI
# =====================================================

root = tk.Tk()

root.title(
    "Mimi AI Assistant"
)

root.geometry(
    "850x750"
)

root.minsize(
    700,
    600
)

root.configure(
    bg="#101114"
)


# =====================================================
# HEADER
# =====================================================

header = tk.Frame(
    root,
    bg="#181a1f",
    height=80
)

header.pack(
    fill="x"
)

header.pack_propagate(
    False
)


title = tk.Label(
    header,
    text="🤖 Mimi",
    font=("Segoe UI", 25, "bold"),
    bg="#181a1f",
    fg="white"
)

title.pack(
    side="left",
    padx=25,
    pady=15
)


status_label = tk.Label(
    header,
    text="🟢 Mimi is online",
    font=("Segoe UI", 10),
    bg="#181a1f",
    fg="#9aa0aa"
)

status_label.pack(
    side="left"
)


# =====================================================
# CHAT AREA
# =====================================================

chat_frame = tk.Frame(
    root,
    bg="#101114"
)

chat_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=15
)


chat_area = scrolledtext.ScrolledText(
    chat_frame,
    font=("Segoe UI", 12),
    bg="#15171c",
    fg="#e8e8e8",
    insertbackground="white",
    relief="flat",
    borderwidth=0,
    wrap=tk.WORD,
    padx=15,
    pady=15
)

chat_area.pack(
    fill="both",
    expand=True
)


# =====================================================
# MESSAGE STYLES
# =====================================================

chat_area.tag_config(
    "user_name",
    foreground="#5ab0ff",
    font=("Segoe UI", 11, "bold")
)

chat_area.tag_config(
    "user_message",
    foreground="#ffffff",
    font=("Segoe UI", 12)
)

chat_area.tag_config(
    "mimi_name",
    foreground="#9b7cff",
    font=("Segoe UI", 11, "bold")
)

chat_area.tag_config(
    "mimi_message",
    foreground="#eeeeee",
    font=("Segoe UI", 12)
)


chat_area.config(
    state=tk.DISABLED
)


# =====================================================
# INPUT AREA
# =====================================================

bottom = tk.Frame(
    root,
    bg="#101114"
)

bottom.pack(
    fill="x",
    padx=20,
    pady=(0, 15)
)


entry = tk.Entry(
    bottom,
    font=("Segoe UI", 13),
    bg="#1c1f26",
    fg="white",
    insertbackground="white",
    relief="flat"
)

entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=12,
    padx=(0, 8)
)


send_button = tk.Button(
    bottom,
    text="➤ Send",
    font=("Segoe UI", 11, "bold"),
    bg="#6c5ce7",
    fg="white",
    activebackground="#5848d8",
    activeforeground="white",
    relief="flat",
    padx=18,
    pady=10,
    command=send_message
)

send_button.pack(
    side="left",
    padx=4
)


voice_button = tk.Button(
    bottom,
    text="🎤",
    font=("Segoe UI", 14),
    bg="#242832",
    fg="white",
    activebackground="#303540",
    relief="flat",
    padx=14,
    pady=7,
    command=start_voice
)

voice_button.pack(
    side="left",
    padx=4
)


clear_button = tk.Button(
    bottom,
    text="🗑",
    font=("Segoe UI", 12),
    bg="#242832",
    fg="white",
    activebackground="#303540",
    relief="flat",
    padx=14,
    pady=9,
    command=clear_chat
)

clear_button.pack(
    side="left",
    padx=4
)


# =====================================================
# ENTER KEY
# =====================================================

root.bind(
    "<Return>",
    send_message
)


# =====================================================
# WELCOME MESSAGE
# =====================================================

add_message(
    "Mimi",
    "Hello! 👋 I'm Mimi.\n"
    "You can type or press 🎤 to talk to me.",
    "mimi"
)


# =====================================================
# START APP
# =====================================================

root.mainloop()