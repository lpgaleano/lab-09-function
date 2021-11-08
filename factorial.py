def factorial(n):
    # an iterative exmple
    total = 1
    for i in range(0, n):
        # i < n ensures that i will never reach n
        total = total * (n - i)
        print("current i is:" + str(i))
        print("current vaule of total is:" + str(total))
    return total

userstring = input("numer please ")
usernum = int(userstring)

print(str(usernum) + "! is " + factorial(usernum))
