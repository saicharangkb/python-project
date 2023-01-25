# def addNumbers(number1,number2):#parameters
#     print(number1+number2)
# addNumbers(5,6)#arguments


# #positional arguments

# def function(a,b,c):
#     print(a,b,c)
# a=5
# b=10
# c=15
# function(b,a,c)

# #keyword arguments

# def function(a,b,c):
#     print(a,b,c)
# function(a=6,b=7,c=8)


#default argument

# def function1(a=7,b=8,c=0):
#     print(b,a,c)
# function1(a=10)
# function1()
# function1(1,5,3)

#variable length arguments

# def vls(*argst):
#     print(argst)
# vls(5,0,8,6)

# #key=value(dict)

# def vls1(**kargs):
#     print(kargs)
# vls1(a=10,b=5,c=8)

#lambda expression(anonymous)
# def squareN(number):
#     print(number**2)
# squareN(10)

#(lambda parameters: expression)(arguments)
# print((lambda number:number**2)(10))


# def iseven(number):
#     if number%2==0:
#         print("even")
#     else:
#         print("Not even")
# iseven(5)

#using lambda

(lambda number:print("even") if number %2==0 else print("not even"))(10)
