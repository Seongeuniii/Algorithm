import math

m, n = map(int,input().split(':'))
i = math.gcd(m,n)

print(str(m//i) + ':' + str(n//i))