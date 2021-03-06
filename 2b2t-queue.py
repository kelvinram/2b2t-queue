# 2b2t queue simulator
# kelvin is nerd

#import modules
import time
import random

server_restarting_chance = random.randint(1, 1000)
server_lost_chance = random.randint(1, 1000)
setup_status = 0
million_queue_chance = random.randint(1, 1000000)

def default_queue():
    position_in_queue = random.randint(729, 1787)
    position_on_restart = random.randint(374, 836)
    print("2b2t is full.")
    for i in range(1, position_in_queue):
        if server_restarting_chance < 13:
            if position_in_queue > 10:
                restart_queue()
        if server_lost_chance < 1:
            reconnect_queue()
        allow_queue = random.randint(0, 1)
        time = random.randint(6, 12)
        from time import sleep
        sleep(time)
        print("Position in queue:", position_in_queue)
        if allow_queue == 1:
            position_in_queue = position_in_queue - 1
        if allow_queue == 0:
            from time import sleep
            sleep(time)
            print("Position in queue:", position_in_queue)
        if position_in_queue == 1:
            print("Connecting to server...")

def restart_queue():
    print("Server restarting")
    default_queue()

def reconnect_queue():
    from time import sleep
    sleep(2)
    print("You have lost connection to the server.")
    from time import sleep
    sleep(2)
    print("Reconnecting...")
    default_queue()

def million_queue():
    print("What do you mean? Position in queue... is unlucky.")
    position_in_queue = random.randint(999637, 1000000)
    position_on_restart = random.randint(374, 836)
    for i in range(1, position_in_queue):
        if server_restarting_chance < 13:
            if position_in_queue < 109283:
                restart_queue()
        if server_lost_chance < 1:
            reconnect_queue()
        allow_queue = random.randint(0, 1)
        time = random.randint(6, 12)
        from time import sleep
        sleep(time)
        print("Position in queue: ", position_in_queue)
        if allow_queue == 1:
            position_in_queue = position_in_queue - 1
        if allow_queue == 0:
            from time import sleep
            sleep(time)
            print("Position in queue: ", position_in_queue)
        if position_in_queue == 1:
            print("Connecting to the server...")
            print("Are you fucking serious?")

def start_process():
    key = input(str("Enter any key to start: "))
    if key == "kelvinboy420ez":
        priority_queue()
    default_queue()
    
def priority_queue():
    print("Priority queue enabled!")
    from time import sleep
    sleep(4)
    position_in_queue = random.randint(60, 150)
    position_on_restart = random.randint(4, 37)
    print("2b2t is full.")
    for i in range(1, position_in_queue):
        if server_restarting_chance < 13:
            if position_in_queue > 10:
                restart_queue()
        if server_lost_chance < 1:
            reconnect_queue()
        allow_queue = random.randint(0, 1)
        time = random.randint(6, 12)
        from time import sleep
        sleep(time)
        print("Position in queue:", position_in_queue)
        if allow_queue == 1:
            position_in_queue = position_in_queue - 1
        if allow_queue == 0:
            from time import sleep
            sleep(time)
            print("Position in queue:", position_in_queue)
        if position_in_queue == 1:
            print("Connecting to server...")

start_process()

