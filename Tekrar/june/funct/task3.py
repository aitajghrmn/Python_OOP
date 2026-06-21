#!/usr/bin/python3

def cemi_hesabla(list):
    cem = 0
    for i in list:
        cem += i
    return cem

print(cemi_hesabla([10, 20, 30]))