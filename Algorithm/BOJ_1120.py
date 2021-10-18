A,B = input().split()
result = 50
for l in range(len(B)-len(A)+1):
  cnt = 0
  for j in range(len(A)):
    if A[j] != B[j+l]:
      cnt+=1
  result = min(result,cnt)
print(result)