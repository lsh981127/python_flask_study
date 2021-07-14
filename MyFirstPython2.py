x = "awesome"
print("2017112197 이승훈")
def myfunc1():
    x = "cool"      #지역변수
    print("1. Computer is " + x)

def myfunc2():
    global y        #전역변수 선언
    y = "fantastic"
    print("2. Computer is " + x)

myfunc1()
myfunc2()
print("3. Computer is " + y)
