# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 14:35:40 2016

@author: c476064  Christoph Haltiner , AXA Group Solutions Switzerland

Purpose: rumspielen mit Python
"""

# new print syntax
from __future__ import print_function

#from timeit import Timer
#import sys
import datetime
import pickle
import re

def hoch(x,y=1):
    """ x hoch y """
    return x ** y
    
def ref_demo(x):
    print ("x=",x," id=",id(x))
    x=42
    print ("x=",x," id=",id(x))


def arithmetic_mean(x, *l):
    """ The function calculates the arithmetic mean of a non-empty
        arbitrary number of numbers """
    sum = x
    for i in l:
        sum += i

    return sum / (1.0 + len(l))

def f(a,b,x,y):
    print(a,b,x,y)

def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
        		return f(x)
        else:
        		raise Exception('Argument is not an integer')
    return helper
    
@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
        
        
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
                
memo = {0:0, 1:1}

def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]
        
print (hoch (2,3))
print (hoch (2))

print (hoch.__doc__)

print (hoch (y=2,x=3))
print (hoch (x=2))

    
    
x = 9
ref_demo(x)

print (x) 

print (arithmetic_mean(4,7,9))

l=  [4,7,9]
print (arithmetic_mean(*l))

d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
f(**d)

d = {'b':'append', 'a':'block','x':'extract','y':'yes'}
f(**d)

print (fib(16))


print (fibm(56))



def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    
@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print (fib(56))
#fib = memoize(fib)
#
#class Memoize:
#    def __init__(self, fn):
#        self.fn = fn
#        self.memo = {}
#    def __call__(self, *args):
#        if args not in self.memo:
#				self.memo[args] = self.fn(*args)
#        return self.memo[args]

print (factorial (19))

try:
    print (factorial (-4))
except Exception as e:
    print ("Unexpected error:", e.args)
 
   
# copy of file --- rowwise with linenumber ;)
    
fobj_in  = open("C:\LocalData\crt_trdb_pgpd_gesch_beziehung.sql", "r")
fobj_out = open("C:\LocalData\daten_copy_hac.sql", "w")

i = 1
for line in fobj_in:
    print (line.rstrip())
    fobj_out.write(str(i) + ": " + line)
    i = i + 1
fobj_in.close()
fobj_out.close()



# copy of file  with linenumber ;)
    
FileIn   =  open("C:\LocalData\crt_trdb_pgpd_gesch_beziehung.sql").readlines()
fobj_out2 = open("C:\LocalData\daten_copy_hac2.sql", "w")

i = 1
for line in FileIn:
    print (line.rstrip())
    fobj_out2.write(str(i) + ": " + line)
    i = i + 1
    
fobj_out2.close()


#Daten auf File bunkern ;) rauspicklen
output = open('C:\LocalData\picklefirsttry.pkl', 'w')
pickle.dump(FileIn, output)
output.close()

# und wieder einlesen
picklefile = open('C:\LocalData\picklefirsttry.pkl')
FileData = pickle.load(picklefile)

print (FileData)

#print (sys.builtin_module_names)



print ( "\n \n  now its ..  " ,  datetime.datetime.now() , "\n \n  .... \n" )

# search all rows with  DATE  in  SQL File
for line in FileData:
    if re.search(r"DATE", line):
        i +=1
        print ("found at #", i, line.rstrip())