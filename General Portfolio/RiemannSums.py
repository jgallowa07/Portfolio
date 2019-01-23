'''
Reimann Sums for Estimating Integrals
Author(s): Jared Galloway
This Program Uses two seperate Methods for Reimann Sums, Trapazoidal Rule, as well
as Simpson's Rule, To estimate the area under a givin funtion from  integrated
from point A to point B
'''

import math

def f(x):
    
    #enter funtion desired to integrate.
    output = (x**(-6))
    
    return(output)


def func(p):
    return (p**51) * (p**69)


def trap_rule(num_slices,From_a,To_b):
    """
    (num,num,num) - > float
    
    Trapzoidal rule by n-number of trap slices, integrated from A to B,
    
    This funtion takes in the number of slices you want to cut, them uses indexing
    to give the above function, f(), an input value x, for which it will return
    the value of the height of the two walls of that trapazoidal slice, which it
    will use to find the are of that trap, ((a + b) / 2) * width
    add it to a sum variable until all slices are accounted for and return the
    sum value of all the slices. AKA the estimated area under that funtion.

    """
    
    slice_width = ((To_b)-(From_a))/num_slices
    sum_of_slices = 0
    counter = 0
    index = From_a
    
    while counter < num_slices:
        
        a = func(index+(counter*slice_width))
        b = func(index+((counter+1)*slice_width))
        sum_of_slices += ((a+b)/2)*slice_width
        counter += 1      

    return(sum_of_slices)
    

def simpsons_rule(n,A,B):
    
    '''Simspsons rule by n-number of parabolic slices, integrated from A to B'''
    
    w = (B-A)/n
    s = 0
    counter = 0
    index = A
    
    while counter < n:
        
        a = f(index+(counter*w))
        b = f(index+((counter+1)*w))
        c = f(index+((counter+2)*w))
        s += ((a+(4*b)+c)/3)*w
        counter += 2      

    return(s)



