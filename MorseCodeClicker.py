import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

def convert_to_morse(text):
    morse_text = ""
    for char in text:
        if char.upper() in morse_code:
            morse_text += morse_code[char.upper()] + " "
        else:
            morse_text += "/ "
    return morse_text

def click_morse_code(morse_text):
    time.sleep(2)
    for symbol in morse_text:
        if symbol == ".":
            # Reduced timing for dot length
            pyautogui.mouseDown()
            time.sleep(0.3)  
            pyautogui.mouseUp()
            time.sleep(0.2)
            
        elif symbol == "-":
            # Reduced timing for dash length
            pyautogui.mouseDown()
            time.sleep(0.6)  
            pyautogui.mouseUp()
            time.sleep(0.2)

        elif symbol == " ":
            # Reduced timing for space between characters
            time.sleep(0.4)  

        elif symbol == "/":
            # Reduced timing for space between words
            time.sleep(0.6)  


# Update Morse Label
def update_morse_label(event):
    text_to_convert = text_entry.get()
    morse_text = convert_to_morse(text_to_convert)
    morse_label.config(text="Morse Code: "+morse_text)


def start_conversion():
    text_to_convert = text_entry.get()
    morse_text = convert_to_morse(text_to_convert)
    print("Morse Code:", morse_text)
    click_morse_code(morse_text)

# Setting up the GUI
root = tk.Tk()
root.title("Morse Code Clicker")
root.iconbitmap('morseCode.ico')
root.geometry("400x200")

# Adding widgets
tk.Label(root, text="1. Enter text to convert to Morse code then click Convert and Execute.\n2. Place the cursor where you want to execute the click sequence.").pack(pady=10)
text_entry = tk.Entry(root, width=60)
text_entry.pack(pady=5)

text_entry.bind("<KeyRelease>", update_morse_label)
morse_label = tk.Label(root, text="Morse Code: ", fg="blue")
morse_label.pack(pady=10)

tk.Button(root, text="Convert and Execute", command=start_conversion).pack(pady=20)

# Running the GUI loop
root.mainloop()
