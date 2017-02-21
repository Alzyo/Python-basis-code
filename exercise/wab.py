# -*- coding: utf-8 -*-
# math.sqrt() 开方

import math

def quadratic(a, b, c):
    d=b**2-4*a*c
    if a==0:
        x=-c/b
        return('%.2f' %(x))
    elif d<0:
        return('no answer')
    else:
        m = (-b+math.sqrt(d))/(2*a)
        n = (-b-math.sqrt(d))/(2*a)
        return(m,n)
print(quadratic(4,3,1))
