N = int(input())
start = 2
line = 3

if N == 1:
  print(1)
else:
  while True:
    if N < start + 6*(line-2):
      print(line-1)
      break
    else:
      start += 6*(line-2)
      line += 1