# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:11:36 2019

@author: littl
"""

import turtle
import numpy as np
import random
turtle.speed('slowest')
'''
x = 0
y = 0
for i in range(0,10000）:
    coin = random.randint(1,8)
    if coin == 1:
        x += 1
    if coin ==2:
        x -= 1
    if coin ==3:
        y += 1
    if coin ==4:
        y -= 1
    if coin ==5:
        x+=1
        y+=1
    if coin ==6:
        x += 1
        y -= 1
    if coin ==7:
        x -= 1
        y += 1
    if coin ==8:
        x -= 1
        y -=1
    turtle.goto(10*x,10*y)
'''
def random_walk_2D(np, ns):
    xpositions = numpy.zeros(np)
    ypositions = numpy.zeros(np)
    NORTH = 1; SOUTH = 2; WEST = 3; EAST = 4
    for step in range(ns):
        for i in range(len(xpositions)):
            direction = random.randint(1, 4)
            if direction == NORTH:
                ypositions[i] += 1
            elif direction == SOUTH:
                ypositions[i] -= 1
            elif direction == EAST:
                xpositions[i] += 1
            elif direction == WEST:
                xpositions[i] -= 1
    return xpositions, ypositions
for i in range(0,1000):
    