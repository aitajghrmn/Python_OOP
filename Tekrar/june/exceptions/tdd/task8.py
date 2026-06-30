#!/usr/bin/python3

import doctest

def ilk_element(siyahi):
    """
    bu funsiya verilen siyahinin birinci elementini qaytarir

    >>>ilk_element(["Python", "Java", "C#"])
    'Python'

    >>>ilk_element([77, 88, 99])
    77


    """

    return siyahi[0]

print(ilk_element(["Holberton","BMU","AzTU"]))