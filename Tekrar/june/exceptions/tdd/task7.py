#!/usr/bin/python3

def kesbek_hesabla(mebleg):
    """
    Bu funksiya məbləğin 5% keşbek bonusunu hesablayır.
    
    >>> kesbek_hesabla(100)
    5.0
    
    >>> kesbek_hesabla(200)
    10.0
    """
    # Bax, axtardığın return tam olaraq budur:
    return mebleg * 0.05

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)