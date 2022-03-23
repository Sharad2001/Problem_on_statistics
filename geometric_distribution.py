def geo_dis(n, p):
    return ((1-p)**(n-1))*p

a, b = list(map(int, input().split()))
n = int(input())
print("{:.3f}".format(geo_dis(n, a/b)))