'''Arbitray parameters (*args)'''

# def myfunc(a,b,c):
#   # returns 5% of the sum of a and b
#   print(sum((a,b,c)) *0.05)

# myfunc(40,60,10)

# ===============================================

# def myfunc(a,b,c,d=0,e=0,f=0):
#   # returns 5% of the sum of a and b
#   print(sum((a,b,c)) *0.05)

# myfunc(40,60,100,100,3,4)

# myfunc(40,60,100,100,3,4,50,90) # myfunc(40,60,100,100,3,4)

# ===============================================

# def myfunc(*args):
#   # returns 5% of the sum of a and b
#   print(sum((args)) *0.05)
#   print(args)

# myfunc(40,60,10,100)

# ===============================================

# def myfunc(*args):
#   for item in args:
#     print(item)

# myfunc(10,20,30,40,50,100)

# ===============================================

'''keyword parameters (**kwargs)'''

# def myfunc(**kwargs):
#   if 'fruit' in kwargs:
#     print('My fruit of choice is {}'.format(kwargs['fruit']))
#   else:
#     print('I did not find any fruit here')

# myfunc(fruit='apple', veggie='lettuce')

# ===============================================
''' *args & **kwargs'''

# def myfunc(*args, **kwargs):
#   print('I would like {} {}'.format(args[0],kwargs['food']))

# myfunc(10,20,30,fruit ='apple',food='eggs',animal='dog')