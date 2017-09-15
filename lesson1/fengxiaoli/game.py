#!/usr/bin/env python
# coding: utf-8

import random

life = 4
gamelevel = 0

while gamelevel < 8:
    print "You see two gates." 
    choose_gate = raw_input("You choose gate:")
    rand_num = int(random.random()*100%2)
    if choose_gate == "left":
        if rand_num == 1:
            print "Hello my friend, give you ten gold and continue next level."
            gamelevel += 1
            if gamelevel == 8:
                print "Congratulation. You pass the Game."
                break
            else:
                print "Now you pass %d level.\n" % gamelevel
                continue
        else:
            print "Go to dead!! A person of a rapacious!"
            life -= 1
            print "Now you leave %d life.\n" % life
            if life == 0:
                print "You are dead. Game over!"
                break
    elif choose_gate == "right":
        if rand_num == 1:
            print "Hello my friend, give you ten gold and continue next level."
            gamelevel += 1
            if gamelevel == 8:
                print "Congratulation. You pass the Game."
                break
            else:
                print "Now you pass %d level.\n" % gamelevel
                continue
        else:
            print "Go to dead!! A person of a rapacious!"
            life -= 1
            print "Now you leave %d life.\n" % life
            if life == 0:
                print "You are dead. Game over!"
                break
    else:
        print "Choose the wrong gate. Resume to choose gate.\n"
            

