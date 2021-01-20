import schedule
from pynput.mouse import Controller, Button
import keyboard
from time import sleep


def join(subject):
    subject = str(subject)
    print("joined", subject)
    webbrowser.open(subject)
    sleep(10)
    mouse.position = (430, 272)
    mouse.press(button.left)
    mouse.release(button.left)
    sleep(0.1)
    keyboard.press('ctrl')
    sleep(0.1)
    keyboard.press('shift')
    sleep(0.1)
    keyboard.press('tab')
    sleep(0.1)
    keyboard.release('tab')
    sleep(0.1)
    keyboard.release('shift')
    sleep(0.1)
    keyboard.release('ctrl')
    sleep(0.1)
    keyboard.press_and_release('ctrl + w')
    sleep(0.1)


def make_schedule(classinfo):
    for i in range(len(classinfo)):
        cinfo = classinfo[i].split(' ')
        if cinfo[0] == "monday":
            schedule.every().monday.at(cinfo[1]).do(join, cinfo[2])
        if cinfo[0] == "tuesday":
            schedule.every().tuesday.at(cinfo[1]).do(join, cinfo[2])
        if cinfo[0] == "wednesday":
            schedule.every().wednesday.at(cinfo[1]).do(join, cinfo[2])
        if cinfo[0] == "thursday":
            schedule.every().thursday.at(cinfo[1]).do(join, cinfo[2])
        if cinfo[0] == "friday":
            schedule.every().friday.at(cinfo[1]).do(join, cinfo[2])
        # if cinfo[0] == "saturday":
            #schedule.every().saturday.at(cinfo[1]).do(join, cinfo[2])


info = open("classes joiner.txt", 'r+', encoding='ascii')
info = info.readlines()
infostr = ""
for p in range(len(info)):
    infostr += info[p]
info = infostr
info = info.split('\n')

make_schedule(info)

while True:
    schedule.run_pending()
