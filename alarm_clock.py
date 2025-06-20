#python alarm clock

import time
import datetime

import pygame

sound_file = "E:\\python\\projects\\Webdriver Torso.mp3"

def set_alarm(alarm_time):
    print(f"alarm set for {alarm_time}")


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS) : ")
    set_alarm(alarm_time)
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("wake up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)