def myfunc(n):
    return lambda a : a*n

mydoubler = myfunc(2)    # n = 2
print(mydoubler(3))      # a = 3 대입
mytripler = myfunc(3)    # n = 3대입
print(mytripler(3))      # a = 3
