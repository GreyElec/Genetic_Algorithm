# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 10:56:36 2018

@author: privacy
"""
import random

def Create(state):
    ps = [float('{:.1f}'.format(random.random())) for i in range(state)]
    s = float('{:.1f}'.format(sum(ps)))
    ps = list(map(lambda x:float('{:.1f}'.format(x)),[i/s for i in ps]))
    res = []
    res.append(state)
    for i in range(state):
        res.append(ps[i])
        for i in range(state):
            probtemp = [float('{:.1f}'.format(random.random())) for i in range(state)]
            m = sum(probtemp)
            probtemp = list(map(lambda x:float('{:.1f}'.format(x)),[i/m for i in probtemp]))
            res.extend(probtemp)
    #res = list(map(str,res))
    return res,ps

X,b = Create(5)