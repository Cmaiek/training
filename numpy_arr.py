import numpy

def arrays(arr):
    a = numpy.array(arr, float)
    numpy.flip(a)
    return(a)

arrays(str('1 2 3 4 -8 -10'))