#MVM RECORD PROGRAMS 5-8
#Arivoli R XIA708

#5.Python program to find the L.C.M. of two input number

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

if a>b:
    small = a 
else:
    small = b
i = 1

while(i<=small):
    if(a%i==0 and b%i==0):
        hcf=i
    i = i+1

lcm = (a*b)//(hcf)
print(f"The LCM is {lcm}")
print(f"The GCD is {hcf}\n\n\n")


#6. 
 
print ("ax^2 + bx + c")
a = int(input("Enter co-efficient of x^2: "))
b = int(input("Enter co-efficient of x: "))
c = int(input("Enter value of c: "))
d = (b*b)-(4*a*c)

if (d==0):
    print("The roots are real and equal.\n\n\n")
    r1 = r2 = ((-1*b)/(2*a))
    print(f'The roots are = {r1} , {r2}\n\n\n')

elif (d>0):
    print("The roots are real and unequal.")
    r1 = ((-1*b+d)/(2*a))
    r2 = ((-1*b-d)/(2*a))
    print(f'The roots are = {r1} , {r2}\n\n\n')
else:
    print("The roots are imaginary.\n\n\n")





#7. Program to display the Fibonacci serjes

# first two terms
n1, n2, i = 0, 1, 2
n = int(input("Enter the number of terms: "))
print(n1)
print(n2)
while i<n:
    n3=n1+n2
    print(n3)
    n1 = n2
    n2 = n3
    i = i+1 
print("\n\n\n")



#8. Program to find sum of the series x - x**3/3! + x**5/5! - x**7/7! +.....

import math
x = float(input("Enter the value of variable x of the series: "))
n = float(input("Enter the number of terms in the series "))
i = 1 
sum = 0
while i<=n:
    fact = 1
    j = 1
    while j<=2*i-1:
        fact = fact*j
        j = j+1
    sum = (sum + (-1)**(i+1) * ((x**(2*i-1))/fact))
    i = i + 1 
print (sum)    