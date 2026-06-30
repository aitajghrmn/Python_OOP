#!/usr/bin/python3
import doctest

def boyuk_herf(metn):
    """
    Bu funksiya daxil edilən mətndəki bütün hərfləri böyüdür.
    
    >>> boyuk_herf("aytac")
    'AYTAC'
    
    >>> boyuk_herf("python")
    'PYTHON'
    """
    # Funksiyanın real backend məntiqi:
    return metn.upper()

# Testləri işə salırıq:
doctest.testmod()

print(boyuk_herf("eli"))
print(boyuk_herf("Aisel"))
print(boyuk_herf("GUNEL"))