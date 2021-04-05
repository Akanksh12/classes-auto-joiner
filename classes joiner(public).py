import schedule
import keyboard
from time import sleep
import pyautogui
import webbrowser
from datetime import datetime


path = __file__.replace('classes_joiner.py',
                        'classes joiner.txt')
print("using data from", path)


def join(subject):
    subject = str(subject)
    now = datetime.now().time()
    print("joined", subject, "at", now)
    if 'meet.google.com' in subject:
        webbrowser.open(subject)
        sleep(7)
        while True:
            try:
                if pyautogui.pixel(0, 90)[0] == 255:
                    keyboard.press_and_release('ctrl+r')
                    sleep(7)
                elif pyautogui.pixel(0, 90)[0] == 17:
                    break
            except:
                pass
    else:
        webbrowser.open(subject)


def join_once(subject):
    subject = str(subject)
    now = datetime.now().time()
    print("joined", subject, "at", now)
    if 'meet.google.com' in subject:
        webbrowser.open(subject)
        sleep(7)
        while True:
            try:
                if pyautogui.pixel(0, 90)[0] == 255:
                    keyboard.press_and_release('ctrl+r')
                    sleep(7)
                elif pyautogui.pixel(0, 90)[0] == 17:
                    break
            except:
                pass
    else:
        webbrowser.open(subject)
    return schedule.CancelJob


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
        if cinfo[0] == "saturday":
            schedule.every().saturday.at(cinfo[1]).do(join, cinfo[2])
        if cinfo[0] == 'everyday':
            schedule.every().day.at(cinfo[1]).do(join, cinfo[2])
        if cinfo[0] == 'once':
            schedule.every().day.at(cinfo[1]).do(join_once, cinfo[2])


print(path)
try:
    info = open(path, 'r+', encoding='ascii')
except:
    print('ensure "classes joiner.txt" is in the same directory as this python file and run again!')
info = info.readlines()
infostr = ""
for p in range(len(info)):
    infostr += info[p]
info = infostr
info = info.split('\n')
print('loaded info')

make_schedule(info)
print('schedule loaded')
print("Waiting for classes to start...")
print("""
'##::::'##::::'###::::'########::'########::::'########::'##:::'##:
 ###::'###:::'## ##::: ##.... ##: ##.....::::: ##.... ##:. ##:'##::
 ####'####::'##:. ##:: ##:::: ##: ##:::::::::: ##:::: ##::. ####:::
 ## ### ##:'##:::. ##: ##:::: ##: ######:::::: ########::::. ##::::
 ##. #: ##: #########: ##:::: ##: ##...::::::: ##.... ##:::: ##::::
 ##:.:: ##: ##.... ##: ##:::: ##: ##:::::::::: ##:::: ##:::: ##::::
 ##:::: ##: ##:::: ##: ########:: ########:::: ########::::: ##::::
..:::::..::..:::::..::........:::........:::::........::::::..:::::
:::'###::::'##:::'##::::'###::::'##::: ##:'##:::'##::'######::'##::::'##:
::'## ##::: ##::'##::::'## ##::: ###:: ##: ##::'##::'##... ##: ##:::: ##:
:'##:. ##:: ##:'##::::'##:. ##:: ####: ##: ##:'##::: ##:::..:: ##:::: ##:
'##:::. ##: #####::::'##:::. ##: ## ## ##: #####::::. ######:: #########:
 #########: ##. ##::: #########: ##. ####: ##. ##::::..... ##: ##.... ##:
 ##.... ##: ##:. ##:: ##.... ##: ##:. ###: ##:. ##::'##::: ##: ##:::: ##:
 ##:::: ##: ##::. ##: ##:::: ##: ##::. ##: ##::. ##:. ######:: ##:::: ##:
..:::::..::..::::..::..:::::..::..::::..::..::::..:::......:::..:::::..::
""")

pyautogui.alert('Waiting for classes to start')

while True:
    schedule.run_pending()
