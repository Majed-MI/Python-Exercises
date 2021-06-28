# Healthy programmer
#Drinking Water 3.5 l Daily (Reminder: water.mp3)
#Eyes rest every 30 minutes (eyes.mp3)
#Physical activity (physical.mp3)

# pygame,datetime,time modules
from pygame import mixer
from datetime import datetime
from time import time

# musiconloop function which takes two value, one:file and the other:value through which it will stop
def musiconloop(file,stopper):
    # initialize, music on through file, music play function call
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    # if the stopper value is right then stop the music
    while(True):
        input_of_user = input()
        # if stopper value match the input value then stop music
        if input_of_user == stopper:
            mixer.music.stop()
            break

# logs taken at file.txt when the work is done
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()} \n")

# only applicable when under the following functions
if __name__ == '__main__':
    # when water,eyes and exercise music on the time function will be counted
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    # giving times to the work
    waterSeconds = 5
    eyesSeconds = 10
    exerciseSeconds = 15

    while(True):
        # when time will be bigger than the given times then musiconloop starts untill the stopper is done
        if time() - init_water > waterSeconds:
            print("Water drinking time. Please enter 'drank' to stop the alarm")
            musiconloop("musics\water.mp3","drank")
            # again the time function is to be counted
            init_water = time()
            log_now("Drank water at")

        # when time will be bigger than the given times then musiconloop starts untill the stopper is done
        if time() - init_eyes > eyesSeconds:
            print("Eyes resting time. Please enter 'done' to stop the alarm")
            musiconloop("musics\eyes.mp3", "done")
            # again the time function is to be counted
            init_eyes = time()
            log_now("Eyes rest at")

        # when time will be bigger than the given times then musiconloop starts untill the stopper is done
        if time() - init_exercise > exerciseSeconds:
            print("Exercise doing time. Please enter 'ok' to stop the alarm")
            musiconloop("musics\physical.mp3","ok")
            # again the time function is to be counted
            init_exercise = time()
            log_now("Done Exercise at")
