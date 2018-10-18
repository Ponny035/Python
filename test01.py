def Fac(x):
    y = x
    if(x==1):
        return 1
    def callMe(z):
        print(z)
        return Fac(z-1)
    return x *callMe(x)


print("Hello")
ans = Fac(5)
print(ans)
