#!/usr/bin/python3
import doctest # Python-un öz daxili test modulu

def vurma(a, b):
    """
    İki ədədi bir-birinə vurur.
    
    >>> vurma(2, 5)
    10
    
    >>> vurma(4, 3)
    12
    """
    return a * b

# Bu sətir Python-a deyir ki, yuxarıdakı şərhlərin içinə bax və test et!
doctest.testmod()

print("Əgər yuxarıda səhv yoxdursa, terminal tərtəmiz olacaq!")