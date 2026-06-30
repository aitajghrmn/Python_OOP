def sebet_cemi(qiymetler):

    """
    Returns the total price of items in a shopping cart.
    
    >>>sebet_cemi([10,20,30])
    60

    >>>sebet_cemi([5,4])
    9
    
    """
    return sum(qiymetler)

print(sebet_cemi([10,20,30,40]))

