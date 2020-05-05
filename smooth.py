import numpy as np
import scipy.optimize as opt

def moving_average(xs):
    n=len(xs)
    ys=np.zeros(n)
    ys[0]=0.5*(xs[0]+xs[1])
    ys[-1]=0.5*(xs[-1]+xs[-2])
    for i in range(1,n-1):
        ys[i]=(xs[i-1]+xs[i]+xs[i+1])/3.0
    return ys

def epi_smooth_dx(xs):
    n=len(xs)
    
    a0vars=range(0,n-2)
    a1vars=range(n-2,2*(n-2))
    a2vars=range(2*(n-2),3*(n-2))
    yvars=range(3*(n-2),3*(n-2)+n)
    dx=3*(n-2)+n
    
    nvars=len(a0vars)+len(a1vars)+len(a2vars)+len(yvars)+1
    lb=np.zeros(nvars)
    ub=np.zeros(nvars)
    for i in a0vars:
        lb[i]=0.0
        ub[i]=1.0
    for i in a1vars:
        lb[i]=0.0
        ub[i]=1.0
    for i in a2vars:
        lb[i]=0.0
        ub[i]=1.0
    for i in yvars:
        lb[i]=min(xs)
        ub[i]=max(xs)
    lb[dx]=0.0
    ub[dx]=100000.0
        
    #Fix the starting and ending values
    lb[yvars[0]]=min(xs)
    ub[yvars[0]]=min(xs)
    lb[yvars[-1]]=min(xs)
    ub[yvars[-1]]=max(xs)
        
    Aub=np.zeros((2*(n-1),nvars))
    bub=np.zeros(2*(n-1))
    for j,i in enumerate(yvars[:-1]):
        Aub[j,i]=-1.0
        Aub[j,i+1]=1.0
        Aub[j,dx]=-1.0
        Aub[n-1+j,i]=1.0
        Aub[n-1+j,i+1]=-1.0
        Aub[n-1+j,dx]=-1.0
        

    aeq=range(0,n-2)
    yeq=range(n-2,2*(n-2))
    neq=len(aeq)+len(yeq)+1
    Aeq=np.zeros((neq,nvars))
    beq=np.zeros(neq)
    

    for k,i in enumerate(aeq):
        a0=min(a0vars)+k
        a1=min(a1vars)+k
        a2=min(a2vars)+k
        Aeq[i,a0]=1.0
        Aeq[i,a1]=1.0
        Aeq[i,a2]=1.0
        beq[i]=1.0
    for k,i in enumerate(yeq):
        x=k+1
        y=min(yvars)+k+1
        a0=min(a0vars)+k
        a1=min(a1vars)+k
        a2=min(a2vars)+k
        Aeq[i,y]=1.0
        Aeq[i,a0]=-xs[x-1]
        Aeq[i,a1]=-xs[x]
        Aeq[i,a2]=-xs[x+1]
        beq[i]=0.0
    for i in yvars:
        Aeq[neq-1,i]=1.0
    beq[neq-1]=sum(xs)
    
    
    c=np.zeros(nvars)
    c[dx]=1.0
    result=opt.linprog(c,Aub,bub,Aeq,beq,list(zip(lb,ub)))
    
    return np.array([result.x[y] for y in yvars])
