from statistics import mode
def stat(l, n):
    sum = 0
    l.sort()
    for i in range(0, n):
        sum = sum + l[i]
    print(sum/n)
    if n%2 == 0:
        median = (l[n//2 - 1] + l[n//2])/ 2
    else:
        median = l[n//2]
    print(median)
    print("%s" %(mode(l)))

n = int(input())
l = list(map(int, input().strip().split()))
stat(l, n)