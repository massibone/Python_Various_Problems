import random, math


random.seed(1)
        
def in_circle(x, origin = [0]*2):
    """
        This function determines if a two-dimensional point
        falls within the unit circle.
    """
    if len(x) != 2:
        return "x is not two-dimensional!"
    elif distance(x, origin) < 1:
        return True
    else:
        return False


print(in_circle((1,1)))
