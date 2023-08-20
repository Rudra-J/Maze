import os,time,random, numpy as np
from matrix_gen import percolate
    
class node():
    pos=None
    parent=None
    dist=None
    cost=None
    def __init__(self,i,j,dist,cost) -> None:
        self.pos=[i,j]
        self.dist=dist
        self.cost=cost
    
def enque(e,q):
    for i in (1,len(q)):q[i]=q[i-1]
    q[0]=e
    return q

def deque(q):
    if len(q)==1:return q[0],[]
    new_q=[]
    min=q[0].dist+q[0].cost
    mine=q[0]
    for i in q:
        if (i.dist+i.cost)<min:
            min= i.dist+i.cost
            mine=i
    for i in q:
        if i!=mine:
            new_q.append(i)
    return mine,new_q

def graph(i,j,dist,cost):
    return node(i,j,dist,cost)

def move_plus(maze,moves,up,down,left,right,i,j,en,cost):
    if up and maze[i-1][j]==1:moves.append(graph(i-1,j,get_man_dist([i-1,j],en),cost))
    if down and maze[i+1][j]==1:moves.append(graph(i+1,j,get_man_dist([i+1,j],en),cost))
    if right and maze[i][j+1]==1:moves.append(graph(i,j+1,get_man_dist([i,j+1],en),cost))
    if left and maze[i][j-1]==1:moves.append(graph(i,j-1,get_man_dist([i,j-1],en),cost))
    return moves

def get_moves(maze,ob,n,en,cost):
    i=ob.pos[0]
    j=ob.pos[1]
    moves=[]
    if i==0:
        if j==0:moves=move_plus(maze,moves,0,1,0,1,i,j,en,cost)
        elif j==n-1:moves=move_plus(maze,moves,0,1,1,0,i,j,en,cost)
        else:moves=move_plus(maze,moves,0,1,1,1,i,j,en,cost)
    elif i==n-1:
        if j==0:moves=move_plus(maze,moves,1,0,0,1,i,j,en,cost)
        elif j==n-1:moves=move_plus(maze,moves,1,0,1,0,i,j,en,cost)
        else:moves=move_plus(maze,moves,1,0,1,1,i,j,en,cost)
    else:
        if j==0:moves=move_plus(maze,moves,1,1,0,1,i,j,en,cost)
        elif j==n-1:moves=move_plus(maze,moves,1,1,1,0,i,j,en,cost)
        else:moves=move_plus(maze,moves,1,1,1,1,i,j,en,cost)
    return moves
   
def backtrack(ob,st):
    if ob.parent==None: 
        s=''
        for i in ob.pos:
            s+=str(i)+','
        s=s[0:len(s)-1]
        return st+s
    else:
        s=''
        for i in ob.pos:
            s+=str(i)+','
        s=s[0:len(s)-1]
        return backtrack(ob.parent,st+s+' ')
         
def sol_prnt(maze,sol):
    str_sol=sol.split(' ')
    sol=[]
    for k in str_sol:
        if len(k)<3: continue
        i=int(k.split(',')[0])
        j=int(k.split(',')[1])
        sol.append([i,j])
    os.system("cls")
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j]==0: print('█',end=" ")
            elif [i,j] in sol: print(".",end=" ")
            else: print(" ",end=" ")
        print()

def get_man_dist(z,en):return abs(z[0]-en[0])+abs(z[1]-en[1])

def traversed(nodes,n):
    for i in nodes:
        if n.pos==i.pos: return True
    return False

def  maze_runner(maze,n):
    start_points=[]
    for i in range(len(maze)):
        if maze[0][i]==1: start_points.append([0,i])
    
    st=start_points[len(start_points)//2]
    
    
    end_points=[]
    for i in range(len(maze)):
        if maze[len(maze)-1][i]==1: end_points.append([len(maze)-1,i])
    en=end_points[len(start_points)//2]
    
    
    q=[graph(st[0],st[1],get_man_dist([st[0],st[1]],en),0)]
    nodes=[graph(st[0],st[1],get_man_dist([st[0],st[1]],en),0)]
    goal=False
    while not goal:
        # time.sleep(1)
        if len(q)==0: break
        e,q=deque(q)          
        moves=get_moves(maze,e,n,en,e.cost+1)
        
        for i in moves:
            i.parent=e
            if not traversed(nodes,i):
                q.append(i)
                nodes.append(i)
        
        for i in moves:
            if i.pos==en:
                en_ob=graph(en[0],en[1],0,i.cost+1)
                en_ob.parent=i
                sol=backtrack(en_ob,'')
                goal=True        

    sol_prnt(maze,sol)
    print(st,'->',en)
    return sol

mz=percolate()
maze=mz.main(int(input("Enter n: ")),1)
maze_runner(maze,len(maze))