from time import sleep
from timer import Timer
import os
import pyfiglet


# time format = hh.mm.ss/mm
time = input('Enter time (in format hh.mm.ss or in mm): ')

if time.count('.') == 0:
    timer = Timer.from_minutes(int(time))
else:
    timer = Timer.from_string(time)

clear = os.system('cls')

while True:
    if timer.is_finished():
        os.system('cls')
        print(pyfiglet.figlet_format("    Time is up!", font="doh"))  # Printing- 'The time is up!'
        input()
        break

    os.system('cls')
    timer.pass_one_second()
    print(timer.time)

    sleep(1)
