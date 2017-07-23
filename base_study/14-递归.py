'''
def jiecheng(i):
    sums = 1
    while i>0:
        sums = sums*i
        i-=1
    return sums
i = input()
sums = jiecheng(i)
print(sums)
'''
def chengfa(num):
    if num > 1:
         num= num* chengfa(num-1)
    return num
print(chengfa(5))
    
