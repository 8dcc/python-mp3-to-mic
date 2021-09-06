# https://stackoverflow.com/questions/37055745/playing-mp3-file-through-microphone-with-python

from pygame._sdl2 import get_num_audio_devices, get_audio_device_name
from pygame import mixer

def main():
    try:
        mixer.init()

        print("\nPrinting devices...")
        print("--------------------------------------------------")
        for x in range(get_num_audio_devices(0)):
            print(f"[{x}] {get_audio_device_name(x, 0).decode()}")
        print("--------------------------------------------------")
        selection = input("Device > ")
        selected_device = str(get_audio_device_name(int(selection), 0).decode())
        mixer.quit()
        mixer.init(devicename=selected_device)
        song = input("File path > ")
        print()
        mixer.music.load(song)
        while True:
            mixer.music.play()
            input("Press enter to stop...")
            mixer.music.stop()
            input("Press enter to play...")
    except KeyboardInterrupt:
        exit("\nCtrl+C detected. Exiting...")

main()
