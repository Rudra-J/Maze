import os,time,random, numpy as np
from matrix_gen import percolate
    
class node():
    pos=None
    parent=None
    traverse_flag=False
    dist=None
    cost=None
    def __init__(self,i,j) -> None:
        self.pos=[i,j]
    
def nq(e,q):
    for i in (1,len(q)):q[i]=q[i-1]
    q[0]=e
    return q

def dq(q):
    if len(q)==1:return q[0],[]
    new_q=[]
    for i in range(1,len(q)):new_q.append(q[i])
    return q[0],new_q

def graph(i,j):return node(i,j)
   
def move_plus(maze,moves,up,down,left,right,i,j):
    if up and maze[i-1][j]==1:moves.append(graph(i-1,j))
    if down and maze[i+1][j]==1:moves.append(graph(i+1,j))
    if right and maze[i][j+1]==1:moves.append(graph(i,j+1))
    if left and maze[i][j-1]==1:moves.append(graph(i,j-1))
    return moves

def get_moves(maze,ob,n):
    i=ob.pos[0]
    j=ob.pos[1]
    moves=[]
    if i==0:
        if j==0:moves=move_plus(maze,moves,0,1,0,1,i,j)
        elif j==n-1:moves=move_plus(maze,moves,0,1,1,0,i,j)
        else:moves=move_plus(maze,moves,0,1,1,1,i,j)
    elif i==n-1:
        if j==0:moves=move_plus(maze,moves,1,0,0,1,i,j)
        elif j==n-1:moves=move_plus(maze,moves,1,0,1,0,i,j)
        else:moves=move_plus(maze,moves,1,0,1,1,i,j)
    else:
        if j==0:moves=move_plus(maze,moves,1,1,0,1,i,j)
        elif j==n-1:moves=move_plus(maze,moves,1,1,1,0,i,j)
        else:moves=move_plus(maze,moves,1,1,1,1,i,j)
    return moves

def backtrack(ob,st):
    if ob.parent==None: 
        s=''
        for i in ob.pos:
            s+=str(i)+','
        s=s[0:len(s)-1]
        s+=''
        return st+s
    else:
        s=''
        for i in ob.pos:
            s+=str(i)+','
        s=s[0:len(s)-1]
        s+=''
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
    print(i)
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j]==0: print("█",end=" ")
            elif [i,j] in sol: print("*",end=" ")
            else: print(" ",end=" ")
        print()

def traversed(nodes,n):
    for i in nodes:
        if n.pos==i.pos: return True
    return False

def  maze_runner(maze,n):
    start_points=[]
    for i in range(len(maze)):
        if maze[0][i]==1: start_points.append([0,i])
    sts={}
    for z in start_points:
        q=[graph(z[0],z[1])]
        # print()
        nodes=[graph(z[0],z[1])]
        goal=False
        while not goal:
            if len(q)==0: break
            e,q=dq(q)            
            moves=get_moves(maze,e,n)
            
            for i in moves:
                i.parent=e
                if not traversed(nodes,i):
                    q.append(i)
                    nodes.append(i)
            
            for i in moves:
                if i.pos[0]==n-1:
                    sol=backtrack(i,'')
                    goal=True        
  
        if goal:sts[f'{z[0]},{z[1]}']=sol
        else:sts[f'{z[0]},{z[1]}']="-"
        
    for i in sts:
        if sts[i]!='-':sol_prnt(maze,sts[i])
        else: print("No viable sol")
        time.sleep(1.5)
    return sts

mz=percolate()
maze=mz.main(int(input("Enter n: ")),1)
maze_runner(maze,len(maze))