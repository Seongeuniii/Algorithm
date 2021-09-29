import sys
R,C = map(int,sys.stdin.readline().split())
graph = []
nowfire = [] # 현재 불의 위치
for i in range(R):
    li = list(sys.stdin.readline().strip())
    graph.append(li)
    if 'J' in li:
        jx,jy = i,li.index('J')
    if 'F' in li:
        fx,fy = i,li.index('F')
        nowfire.append((fx,fy))
nowj = [(jx,jy)] # 현재 지훈이 위치
dx,dy = [0,0,1,-1], [1,-1,0,0]
def fire(li):
    newfire = []
    while li:
        x,y = li.pop()
        for j in range(4):
            newfx,newfy = x+dx[j],y+dy[j]
            if newfx>=R or newfx<0 or newfy>=C or newfy<0:
                continue
            if graph[newfx][newfy] =='.' or graph[newfx][newfy] == 'J':
                graph[newfx][newfy] = 'F' # 불로 바꿔줌
                newfire.append((newfx,newfy)) # 그 다음 불
    return newfire
def escape(li):
    global move,cnt
    newj = []
    while li:
        x,y = li.pop()
        for j in range(4):
            newjx,newjy = x+dx[j],y+dy[j]
            if newjx>=R or newjx<0 or newjy>=C or newjy<0:
                continue
            if graph[newjx][newjy] =='.':
                if newjx==R-1 or newjx==0 or newjy==C-1 or newjy==0:
                    print(cnt+2)
                    sys.exit()
                move = True
                graph[newjx][newjy] = 'J'
                newj.append((newjx,newjy)) # 그 다음 지훈이 위치
    cnt += 1
    return newj
cnt = 0
move = True
if jx==R-1 or jx==0 or jy==C-1 or jy==0: # 처음부터 벽에 붙어있으면 1
    print(1)
    sys.exit()
while move==True:
    nowfire = fire(nowfire)
    move = False
    nowj = escape(nowj)
print('IMPOSSIBLE')