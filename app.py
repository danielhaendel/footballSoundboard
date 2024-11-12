from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


import pygame
import os
import random
from gpiozero import Button
from signal import pause

# Initialisiere den Mixer
pygame.mixer.init()

# Verzeichnis für die Sounds
BASE_DIR = "sounds"

# Funktion, um einen zufälligen Sound aus einem Ordner abzuspielen
def play_random_sound(category):
    folder_path = os.path.join(BASE_DIR, category)
    if not os.path.isdir(folder_path):
        print(f"Ordner {folder_path} existiert nicht.")
        return

    files = os.listdir(folder_path)
    sound_files = [f for f in files if f.endswith(".mp3")]

    if not sound_files:
        print(f"Keine Sounddateien in {folder_path}.")
        return

    # Wähle eine zufällige Datei
    sound_file = random.choice(sound_files)
    full_path = os.path.join(folder_path, sound_file)

    # Lade und spiele die Datei ab
    pygame.mixer.music.load(full_path)
    pygame.mixer.music.play()
    print(f"Abspiele {category} Sound: {sound_file}")

# GPIO-Pins für die Buttons festlegen
touchdown_button = Button(2)  # GPIO 2 für "Touchdown"
firstdown_button = Button(3)  # GPIO 3 für "First Down"
win_button = Button(4)        # GPIO 4 für "Win"
defense_button = Button(17)   # GPIO 17 für "Defense"

# Button-Ereignisse verknüpfen
touchdown_button.when_pressed = lambda: play_random_sound("touchdown")
firstdown_button.when_pressed = lambda: play_random_sound("firstdown")
win_button.when_pressed = lambda: play_random_sound("win")
defense_button.when_pressed = lambda: play_random_sound("defense")

print("Soundboard ist bereit. Drücke einen der Buttons.")

# Halte das Programm am Laufen
pause()
