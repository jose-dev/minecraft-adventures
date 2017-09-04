"""

    web resources:
        - https://pymotw.com/2/threading/
        - https://docs.python.org/2/library/threading.html

"""

import mcpi.minecraft as minecraft
import time
import threading
import random


def boom(mc, event_countdown, event_foundall, bombs=10, delay=1):
    name = threading.currentThread().getName()
    event_countdown.wait()
    if not event_foundall.wait(1):
        for i in range(0, bombs):
            mc.postToChat("({0}) BOOM!!!".format(name))
            time.sleep(delay)
    mc.postToChat("({0}) bye".format(name))


def object_quest(mc, event_foundall):
    name = threading.currentThread().getName()
    time.sleep(3)
    found_all = random.choice([True, True])
    if found_all:
        mc.postToChat("({0}) found all. It won't explode".format(name))
        event_foundall.set()
    else:
        mc.postToChat("({0}) NOT found all. It WILL explode".format(name))
    mc.postToChat("({0}) bye".format(name))


def countdown(mc, event_countdown, event_foundall, total=15, delay=5):
    name = threading.currentThread().getName()
    left = total
    while left > 0:
        mc.postToChat("({0}) time remaining: {1} seconds".format(name, str(left)))
        left -= delay
        has_found_all = event_foundall.wait(delay)
        if has_found_all:
            break
    if not has_found_all:
        mc.postToChat("({0}) TIME'S UP!!!".format(name))
        event_countdown.set()
    mc.postToChat("({0}) bye".format(name))


def where_i_am(mc, delay=1):
    name = threading.currentThread().getName()
    while not out_of_time:
        pos = mc.player.getTilePos()
        mc.postToChat("({0}) x: {1} y: {2} z: {3}".format(name,
                                                          str(pos.x),
                                                          str(pos.y),
                                                          str(pos.z)))
        time.sleep(delay)
    mc.postToChat("({0}) No more where I am.".format(name))
    mc.postToChat("({0}) bye".format(name))


out_of_time = False
mc = minecraft.Minecraft.create()

mc.postToChat("STARTING GAME")

# start threads
event_countdown = threading.Event()
event_foundall = threading.Event()
threads = [threading.Thread(name="countdown", target=countdown, args=(mc, event_countdown, event_foundall,)),
           threading.Thread(name="boom", target=boom, args=(mc, event_countdown, event_foundall,)),
           threading.Thread(name="object_quest", target=object_quest, args=(mc, event_foundall,)),
           threading.Thread(name="where_i_am", target=where_i_am, args=(mc,))]
for t in threads:
    t.start()

# main loop
for n in range(0, 3):
    mc.postToChat("IN MAIN LOOP")
    time.sleep(7)
out_of_time = True

time.sleep(7)
mc.postToChat("ENDING GAME")
