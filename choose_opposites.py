from opposites import opposites
from random import randrange

l = len(opposites)
op1 = opposites[randrange(l)]
op2 = opposites[randrange(l)]

ops1 = op1.partition(" - ")
ops2 = op2.partition(" - ")    

list = ["", ops1[0], ops1[2], ops2[0], ops2[2]]