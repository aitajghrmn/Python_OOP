#!/usr/bin/python3
import doctest

def maili_temizle(email):
    """
    Bu funksiya emailin əvvəlindəki və sonundakı boşluqları silir.
    
    Bax belə yazılmalıdır (funksiyanın adı ilə):
    >>> maili_temizle("  aytac@gmail.com ")
    'aytac@gmail.com'
    """
    return email.strip()

# verbose=True qoyaq ki, terminalda testin uğurla keçdiyini gözünlə görəsən:
doctest.testmod(verbose=True)

# Sənin yazdığın print-i də bura əlavə edirəm (gəl funksiya ilə çağıraq ki, boşluğu silsin):
print(maili_temizle(" businessqehremanqizi@gmail.com"))