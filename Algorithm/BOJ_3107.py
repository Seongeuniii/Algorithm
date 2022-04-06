import sys
input = sys.stdin.readline

IP = input().strip().split(':')
if not IP[0]: ip = IP[1:]
elif not IP[-1]: ip = IP[:len(IP)-1]
else: ip = IP

answer = ''
for i in ip:
  if not i:
    answer += '0000:'*(8-len(ip)+1)
  else:
    answer += ('0'*(4-len(i)) + i + ':')

print(answer[:-1])