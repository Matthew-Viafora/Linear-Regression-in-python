from sympy import *

x = Symbol('x')
size = [900*x, 1500*x, 2000*x]
price = [200, 300, 400]


def sum(x,y):
    return x+y

#predict 1000ft^2


#error function using recursion
def error(a, b):
    if a == []:
        return 0
    b = ((a[0]-b[0])**2) + error(a[1:], b[1:])
    return b

#error function
y = error(size, price)
#error function derivative in order to find mins
yprime = y.diff(x)


print ("Error fucntion: ", y)
print ("Derivative of error function: ", yprime)

#Find roots of the function
yroots = solveset(yprime, x)

####



##################### Turn set into a list so that you can find min
n=[]
for l in yroots:
    n= n + [l]
#####################
#####################Only works for functions with two critical points

#if the critical point is negative to the left of it, and then postitive to the right
#Then it is a minimum
#The reason for using the ".subs(I,0)" is because it is giving me an imaginary number
#when i am calcuating the critical point, and that gets rid of it
#Also note that this finds the maximum, which for this algorithm, we do not need the maximum
    
if (yprime.subs(x, (n[0].subs(I, 0)-1))) < 0 and (yprime.subs(x, (n[0].subs(I, 0)+1))) > 0:
    print(n[0], " is a Minimum")
elif (yprime.subs(x, (n[0].subs(I, 0)-1))) > 0 and (yprime.subs(x, (n[0].subs(I, 0)+1))) < 0:
    print(n[0], " is a Maximum")

#The more variables that you have,the more roots you will have, therefore we do not need this
#part unless there were to be more than one root
#if (yprime.subs(x, (n[1].subs(I, 0)-1))) < 0 and (yprime.subs(x, (n[1].subs(I, 0)+1))) > 0:
#    print(n[1], " is a Minimum")
#elif (yprime.subs(x, (n[1].subs(I, 0)-1))) > 0 and (yprime.subs(x, (n[1].subs(I, 0)+1))) < 0:
#    print(n[1], " is a Maximum")




#Calculate prediction based on linear regression fomrula y = ax
#Where a is the minimum of the error function and x is the prediction you are looking for from "size

#predict price of 1000ft^2
p = (n[0]*1000)
print("My prediction is (for 1000ft^2): ", float(p))




    




    
