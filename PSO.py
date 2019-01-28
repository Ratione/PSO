#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ======================================================================================
#
# Ian Minatrea
# Implementation of the Particle Swarm Optimization (PSO) Algorithm in Py3
# January, 2019
#
# ======================================================================================

__author__ = "Ian Minatrea"
__date__ = "01/23/2019"
__copyright__ = "Copyright 2019, The Helios Project"
__email__ = "Minatrea.Ian@gmail.com"
__version__ = "0.1.0"
__status__ = "Prototype"

# ======================================================================================
# Imports
# ======================================================================================

import math
import random
#import numpy as np
#import scipy as sp
#import matplotlib as plt

# =====================================================================================
# Cost Function - The Function we want to Minimize
# =====================================================================================


def cost(x):
    
    # A simple, if not the simplest cost function with any meaningful result. Arbitrary

    total = 0
    for i in range(len(x)):
        total += x[i] ** 2
    return total


# =====================================================================================
# Main
# =====================================================================================

class Swarm:
    """
    This Class contains all the particles from a given swarm, and by extension, their 
    properties.

    The point of these two classes being separate is purely a conceptual one, it could
    be much more efficient, but I feel that this way best illustraits the relationship
    between individual particle and the aggregate swarm.
    """
    def __init__(self):
        self.err_bg = -1  # best error for group
        self.pos_bg = [] # best position for group
        self.swarm = [] # array that holds all the Particle Objects
        
    def __iter__(self, costFunc, x0, bounds, partNum):
        self.cost = costFunc # The cost fuction feed into the swarm
        self.x0 = x0
        self.partNum = partNum
        self.bounds = bounds
        self.iter = 0
        # establish the swarm
        for i in range(0, self.partNum):
            self.swarm.append(Particle(self.x0))

    def __next__(self, maxIter):
        # begin optimization loop
        # cycle through particles in swarm and evaluate fitness

        #print(self.iter)
        self.iter += 1
        
        for i in range(0, len(self.swarm)):
            self.swarm[i].err_i = self.cost(self.swarm[i].pos_i)
            
            # check to see if the current position is an individual best
            if self.swarm[i].err_i < self.swarm[i].err_bi or self.swarm[i].err_bi == -1:
                self.swarm[i].pos_bi = self.swarm[i].pos_i
                self.swarm[i].err_bi = self.swarm[i].err_i

            if self.swarm[i].err_i < self.err_bg or self.err_bg == -1:
                self.pos_bg = list(self.swarm[i].pos_i)
                self.err_bg = float(self.swarm[i].err_i)
        
        # cycle through swarm and update velocities and position    
        for i in range(0, len(self.swarm)):
            self.swarm[i].vUpdate(self.pos_bg)
            self.swarm[i].xUpdate(self.bounds)

        if self.iter > maxIter:
            raise StopIteration
        else:
            return self


class Particle(Swarm):
    """
    A subclass of Swarm, these particles have little meaning outsite the greater
    context of the swarm, but nevertheless must contain their own individual 
    properties to be referenced by the fitness algorithm. None of their stats
    matter indiviually
    """
    def __init__(self, x0):
        self.pos_i = []  # particle position
        self.vel_i = []  # particle velocity
        self.pos_bi = []  # best position individual
        self.err_bi = -1  # best error individual
        self.err_i = -1 # error individual
        self.dimNum = len(x0)

        for i in range(0, self.dimNum):
            self.vel_i.append(random.uniform(-1,1))
            self.pos_i.append(x0[i])

    # update new particle velocity
    def vUpdate(self, pos_bg):
        w = 0.5  # constant inertia weight (how much to weigh the previous velocity)
        c1 = 1  # cognative constant
        c2 = 2  # social constant

        for i in range(0, self.dimNum):
            r1 = random.random()
            r2 = random.random()

            vCog = c1 * r1 * (self.pos_bi[i] - self.pos_i[i])
            vSoc = c2 * r2 * (pos_bg[i] - self.pos_i[i])
            self.vel_i[i] = w * self.vel_i[i] + vCog + vSoc

    # update the particle position based off new velocity updates
    def xUpdate(self, bounds):
        for i in range(0, self.dimNum):
            self.pos_i[i] = self.pos_i[i] + self.vel_i[i]

            # adjust maximum position if necessary
            if self.pos_i[i] > bounds[i][1]:
                self.pos_i[i] = bounds[i][1]

            # adjust minimum position if neseccary
            if self.pos_i[i] < bounds[i][0]:
                self.pos_i[i] = bounds[i][0]

x0 = [5, 5]  # initial starting location [x1,x2...]
bounds = [(-10, 10), (-10, 10)] # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
pso1 = Swarm()
pso1.__iter__(cost, x0, bounds, partNum = 15)
for i in range(30):
    pso1.__next__(30)
print("FINAL:")
print(pso1.pos_bg)
print(pso1.err_bg)

