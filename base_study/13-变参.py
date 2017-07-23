sums = 0  
def sum_num(a,b,*args):
    print(args)
    sums = a+b
    for temp in args:
        global sums
        print(temp)
        sums = sums+temp
    return sums
sums_s = sum_num(1,2,3,4,5,6,7,8,9)
print(sums_s)

