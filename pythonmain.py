#pyjokes library

import pyjokes
jokes = pyjokes.get_joke()
print(jokes)


#variables
#int
a=1
b=2
print(a+b)

#string
c = 'string'
print(c)

#floating point number

d = 1.4
print(d)


#boolean
e = True
f = False

#None

g = None #to mark nothing



#boolean
d = 1==1
print(d)



#logical operators

j = True or False
print(j)

k = True or True
print(k)

l = True and False
print(l)

m = False and False
print(m)


print("True and False is:", True and False)

print(not(False))

# function to check the type of variable
print(type(a))

#changing the type using type casting 
a = 1
b=float(a)
print(b)
print(type(b))
print(type(float(a)))

