def gu (l):
    k = {}
    for i in range(1,l+1):
        k[i] = i**3
    return k
k = int(input("enter the number you whant to go cube : "))
ji = (gu(k))
print(f"your enter result is = {ji} ")
