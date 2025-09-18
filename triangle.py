from math import factorial
# def triangle(n):
#     for i in range(n):
#         for j in range(n):
#             if i==0 or j==0 or i== n-1 or j==n-1 or i==j or i+j == n-1:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# n=int(input("enter number: "))
# triangle(n)
def pascal_triangle(n):
    for i in range(n):
        print((n-i)*" ",end=" ")
        for j in range(i+1):
            temp = factorial(i)//(factorial(i-j)*factorial(j))
            print(temp,end=" ")
        print()
n=int(input("enter value: "))
pascal_triangle(n)