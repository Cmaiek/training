import numpy

def arrays(arr):
    arr = arr.split(" ")
    a = numpy.array(numpy.flip(arr, 0), float)
    print(a)

arrays(str('1 2 3 4 -8 -10'))