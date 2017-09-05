from sympy.tensor.tensor import tensor_indices, tensorhead, TensorIndexType, TensorType
import sympy
import numpy

def f0(pa,pb,i,j,k,l):
        s=[0,0,0,0]
        m=[i,j,k,l]
        sign=(-1)**m.count(-1)
        for n in 0, 1:
                if m[n]<0:
                        s[n]=1
                elif m[n]==0:
                        s[n]=1-pb
                else :
                        s[n]=pb
        for n in 2, 3:
                if m[n]<0:
                        s[n]=1
                elif m[n]==0:
                        s[n]=1-pa
                else :
                        s[n]=pa
#       print sign
        return sign*s[0]*s[1]*s[2]*s[3]

def f2(pa, pb, a, b, c, d): 
        ret=[[0,0,0],[0,0,0],[0,0,0]]
        for i in 1,2:
                for j in 1,2:
                        for k in 1,2:
                                for l in 1,2:
                                        ret[i+j-2][k+l-2]+=(f0(pa,pb, min(-a*i,i-1), min(-b*j,j-1), min(-c*k,k-1), min(-d*l, l-1) ) ) 
	ret=sympy.Matrix(ret)
	return ret

a, d, p, f, fx, fy, t, g, d2, d4= sympy.symbols('a d p f fx fy t g d2 d4')

q=1-p

f=0

d_index = TensorIndexType('d_index', dummy_fmt='L')
z_index = TensorIndexType('z_index', dummy_fmt='L')

PJ=[1, 1, 1]

d_index.data = [ [PJ[0], 0, 0], [0, PJ[1], 0], [0, 0, PJ[2] ] ]
#d_index.data = [ [1, 0.5, 0], [0.5, 1, 0.5], [0, 0.5, 1 ] ]
print d_index.metric

P = tensorhead('P', [d_index, d_index, d_index], [[1],[1],[1]])
#R = tensorhead('R', [d_index, d_index], [[1], [1]])
R = tensorhead('R', [d_index, d_index, d_index, d_index], [[1], [1], [1], [1]])

S1 = tensorhead('S1', [d_index], [[1]])
S = tensorhead('S', [d_index, d_index], [[1], [1]])
#I = tensorhead('I', [d_index, d_index, d_index, d_index], [[1],[1],[1],[1]])

I = tensorhead('I', [d_index, d_index, d_index, d_index, d_index, d_index, d_index, d_index], [[1],[1],[1],[1], [1],[1],[1],[1]])

s = tensorhead('S', [d_index], [[1]])

T = tensorhead('T', [d_index, d_index], [[1], [1]])
G = tensorhead('G', [d_index, d_index], [[1], [1]])
Fy = tensorhead('Fy', [d_index, d_index], [[1], [1]])
Fx = tensorhead('Fx', [d_index, d_index], [[1], [1]])
D2 = tensorhead('D2', [d_index, d_index], [[1], [1]])
D4 = tensorhead('D4', [d_index, d_index], [[1], [1]])

beta=tensorhead('beta', [d_index], [[1]])
delta=tensorhead('delta', [d_index], [[1]])
delta2=tensorhead('delta2', [d_index], [[1]])


b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10= tensor_indices('b0:11', d_index)

#	    00   01   02 
#           10   11   12   
#           20   21   22 
P.data = [ [ [1.0, 0.5, 0.0],
             [0.5, .25, 0.0],   #=0
             [0.0, 0.0, 0.0] ],

	   [ [0.0, 0.5, 1.0],
             [0.5, 0.5, 0.5],   #=1
             [1.0, 0.5, 0.0] ], 

	   [ [0.0, 0.0, 0.0],
             [0.0, .25, 0.5],  #=2
             [0.0, 0.5, 1.0] ] ]




#
#I need a more tensor way of expressing these...
#

s.data=[q**2+p*q*f, 2*p*q*(1-f), p**2+p*q*f]

s2=p*q**2+q*(-p)**2
s3=p*q**3+q*(-p)**3
s4=p*q**4+q*(-p)**4

k=1/(1-p)+1/p-3

T.data = t*s2*(f2(p,p, 1, -1, 1, -1)+f2(p,p, 1, -1, -1, 1)+f2(p,p, -1, 1, 1, -1)+f2(p,p, -1, 1, -1, 1) )/2*(1+f)
Fy.data=fy*s2*(f2(p,p, 1, 1, -1, -1))
Fx.data=fx*s2*(f2(p,p, -1, -1, 1, 1))
G.data= (g*s3*(f2(p,p, -1, 1, 1, 1)+f2(p,p, 1, -1, 1, 1) )+g*s3*(f2(p,p, 1, 1, 1, -1)+f2(p,p, 1, 1, -1, 1) ) )*f
D2.data=d4*s2*s2*(f2(p,p, 1, 1, 1, 1) )
D4.data=d2*s4*(f2(p,p, 1, 1, 1, 1) )

alpha=( a+d*(q-p) )
mD=2*d*f*q*p

beta.data = [-2*alpha*p, alpha*(q-p) , 2*alpha*q]
delta.data = [-2*d*p**2+mD, 2*d*p*q+mD, -2*d*q**2+mD]
delta2.data = [(-2*d*p**2+mD)**2, (2*d*p*q+mD)**2, (-2*d*q**2+mD)**2]

#X=s(b1)*s(-b2)
#Y=delta(b1)*delta(-b2)

#var_delta=X(b1,-b1)*Y(-b1,b1)

#(b1,-b1)
#tk=1/p+1/(1-p)-3
#tf=1
var_delta=4*d**2*p*q*(p*q+f*(4*p**2-4*p+1)-f**2*p*q )#/(1-tf-tf**2+tf*tk)
var_beta =2*p*q*alpha**2*(1+f)
cov=4*alpha*d*(p**3*q-q**3*p)

#s_bb=sympy.simplify(s.beta*beta)
#s_bd=sympy.simplify(s.beta*delta)
#s_dd=sympy.simplify(s.delta*delta)

#
#------------------------------------------------
# 

R=( s(b1)*s(b2)*s(b3)*s(b4) )#+T(b1,b2)#+G(b1,b2)+D2(b1,b2)+D4(b1,b2)+Fx(b1,b2)+Fy(b1,b2) )
#R=(s(b1)*s(b2) )#+G(b1,b2)+D2(b1,b2)+D4(b1,b2)+Fx(b1,b2)+Fy(b1,b2) )

#I.data = [[[[ int(i==k and j==l) for i in range(3)] for j in range(3)]  for k in range(3)] for l in range(3)]

I.data = [[[[[[[[ int(i==m and j==n and k==o and l==p ) for i in range(3)] for j in range(3)]  for k in range(3)] for l in range(3)] for m in range(3)] for n in range(3)] for o in range (3)] for p in range(3)] 

#S.data = [[ 1. for i in range(3)] for j in range(3)] 
#R.data = [[ i*3+j for i in range(3)] for j in range(3)] 
#S1.data = [ 1. for i in range(3)] 


#for x in range(0, 3):
#	delta2.data[x] = delta.data[x]**2 
#print delta2.data
#var_delta2=(s(b1)*delta2(-b1) )
#print sympy.simplify(var_delta2.data)
#print var_delta
#print  sympy.simplify( sympy.simplify(var_delta2.data)/var_delta)
#print  sympy.simplify( var_delta2.data/var_delta)
#print  sympy.simplify( ( S(b1,b2)*R(-b1,-b2) ).data)


#print R(-b2,-b3) 
#print (I(b2,b3,-b4,-b5)*R(b4,b5) ).canon_bp()
J=( I(b0,b1,b2,b3,-b4,-b5,-b6,-b7)*R(b4,b5,b6,b7) )
#J=( P(b8,-b0,-b1)*P(b9,-b2,-b3)*I(b0,b1,b2,b3,-b4,-b5,-b6,-b7)*R(b4,b5,b6,b7) ).data

#print ( P(b5,-b1,-b2)*P(b6,-b3,-b4)*J(b1,b2,b3,b4) )
#print ( P(b5,-b1,-b2)*P(b6,-b3,-b4)*J(b1,b2,b3,b4) ).data
#print (S1(b1)*P(-b1,b2,b3)*J(-b2,-b3) )

#print sympy.simplify( (S1(b1)*P(-b1,b2,b3)*R(-b2,-b3) ).data )
#print sympy.simplify( (S1(b1)*P(-b1,b2,b3)*J(-b2,-b3) ).data )

#print sympy.simplify( (S1(b1)*P(-b1,b2,b3)*J(-b2,-b3) ).data )
#print sympy.simplify( (S(b2,b3)*J(-b2,-b3) ).data)

#print ( beta(-b5)*beta(-b6)*P(b5,-b1,-b2)*P(b6,-b3,-b4)*J(b1,b2,b3,b4)  ).data
print  sympy.simplify( ( beta(-b5)*beta(-b6)*P(b5,-b1,-b2)*P(b6,-b3,-b4)*J(b1,b2,b3,b4)  ).data/var_beta)
print  sympy.simplify( ( delta(-b5)*delta(-b6)*P(b5,-b1,-b2)*P(b6,-b3,-b4)*J(b1,b2,b3,b4) ).data/var_delta)
print  sympy.simplify( ( ( beta(-b5)*delta(-b6)+delta(-b5)*beta(-b6) )*P(b5,-b1,-b2)*P(b6,-b3,-b4)*J(b1,b2,b3,b4)  ).data/cov)
