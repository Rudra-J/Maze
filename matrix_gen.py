import os,time,random, numpy as np

class uf:
    id1=None
    def __init__(self,n):
        self.id1=np.arange(0,(n**2)+2)
                    
    def union(self, p,q):
        #t=time.time()
        r=self.id1[p]
        for i in range(len(self.id1)):
            if self.id1[i]==r: self.id1[i]=self.id1[q]
        #print(time.time()-t)
                                     
    def con(self,p,q):
        return self.id1[q]==self.id1[p]
    
class percolate:
    
    def prnt(self,bd,ob,n):
        os.system("cls")
        for i in range(n):
            for j in range(n):
                if bd[i][j]==1: 
                    if ob.con(0,self.num(i,j,n)): 
                        print(".",end=" ")
                        bd[i][j]=2
                    else:print(" ",end=" ")
                elif bd[i][j]==2: print(".",end=" ")
                else: print("█",end=" ")
            print()

    def purge(self,bd):
        for i in range(len(bd)):
            for j in range(len(bd)):
                if bd[i][j]==2:bd[i][j]=1
        return bd


    def num(self,i,j,n):
        return ((i*n)+j)+1

    def un(self,u,d,l,r,i,j,bd,ob,n):
        if u==1 and (bd[i-1][j]==1 or bd[i-1][j]==2) and bd[i][j]==1: ob.union(self.num(i,j,n),self.num(i-1,j,n))
        if d==1 and (bd[i+1][j]==1 or bd[i+1][j]==2) and bd[i][j]==1: ob.union(self.num(i,j,n),self.num(i+1,j,n))
        if l==1 and (bd[i][j-1]==1 or bd[i][j-1]==2) and bd[i][j]==1: ob.union(self.num(i,j,n),self.num(i,j-1,n))
        if r==1 and (bd[i][j+1]==1 or bd[i][j+1]==2) and bd[i][j]==1: ob.union(self.num(i,j,n),self.num(i,j+1,n))

    def perc(self,bd,ob,o,n):
        i=o//n
        j=o%n
        if i==0 :
            if   j==0:   self.un(0,1,0,1,i,j,bd,ob,n)
            elif j!=n-1: self.un(0,1,1,1,i,j,bd,ob,n)
            elif j==n-1: self.un(0,1,1,0,i,j,bd,ob,n)
            ob.union(o+1,0)
        elif i!=n-1:
            if   j==0:   self.un(1,1,0,1,i,j,bd,ob,n)
            elif j!=n-1: self.un(1,1,1,1,i,j,bd,ob,n)
            elif j==n-1: self.un(1,1,1,0,i,j,bd,ob,n)
        elif i==n-1:
            if   j==0:   self.un(1,0,0,1,i,j,bd,ob,n)
            elif j!=n-1: self.un(1,0,1,1,i,j,bd,ob,n)
            elif j==n-1: self.un(1,0,1,0,i,j,bd,ob,n)
            ob.union(o+1,n**2+1)
            
    def mat_make(sefl,bd,ind,n):
        i=random.choices(ind,k=1)[0]
        bd[i//n][i%n]=1
        ind.pop(ind.index(i))
        return i
                    
    def main(self,n,nu):
        s=0
        t=nu
        while(nu>0):
            bd=[[] for i in range(n)]
            for i in bd:
                for j in range(n): i.append(0)
            ob=uf(n)
            ind=list(np.arange(0,n**2))
            f=0
            c=0
            st=time.time()
            start=time.time()
            while(f==0 or c/(n**2)<=0.75):
                # print(c/(n**2)*100)
                c+=1
                o=self.mat_make(bd,ind,n)
                self.perc(bd,ob,o,n)
                self.prnt(bd,ob,n)
                if ob.con(0,n**2+1): f=1
                if c%1000==0: 
                    print(c,time.time()-start)
                    start=time.time()
            time.sleep(2)
            print(f"Total time: {time.time()-st}")
            nu-=1
        return self.purge(bd)