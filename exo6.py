#!/usr/bin/env python3.10

from calendar import c


def convert(a):
    a = a*60
    return a
     

res = convert(1)
print ("resultat : ", str(res), "secondes")

res = convert(2)
print ("resultat: ", str(res), "secondes")

res = convert(6)
print ("resultat: ", str(res), "secondes")