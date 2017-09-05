from sympy.tensor.tensor import tensor_indices, tensorhead, TensorIndexType, TensorType
import sympy

d_index = TensorIndexType('d_index', dummy_fmt='L')
z_index = TensorIndexType('z_index', dummy_fmt='L')

P = tensorhead('P', [d_index, d_index, d_index], [[1],[1],[1]])
R = tensorhead('R', [d_index, d_index], [[1], [1]])
I = tensorhead('I', [d_index, d_index, d_index, d_index], [[1],[1],[1],[1]])

d_index.data = [1, 1, 1]

b0, b1, b2, b3, b4, b5= tensor_indices('b0:6', d_index)

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

#a,b,c,d,e,f,g,h,i = sympy.symbols('a b c d e f g h i')

R.data = [[ 1./9. for i in range(3)] for j in range(3)]  
#R.data = [[a,b,c],[d,e,f],[g,h,i]]  

beta.data = [-alpha, , alpha]
delta.data = [delta, , delta]

hwe1={q1^2,p1*q1,p1*q1,p1^2}
idev1={p1*q1*f1,-p1*q1*f1, -p1*q1*f1,p1*q1*f1}
freq1=Simplify[hwe1+idev1]

muz1=Simplify[z1.freq1]
zdev1=Simplify[z1-muz1]

freq=Flatten[Outer[Times,freq1,freq2]]
z=Flatten[Outer[Plus,z1-muz1,z2-muz2]]
zdev=Simplify[freq*z]

alpha1=(a1+d1*(q1-p1))



I.data = [[[[ float(i==k and j==k) for i in range(3)] for j in range(3)]  for k in range(3)] for l in range(3)]

#print h_index.data
#print P(b0,b1,b2)[0,0,0]##d_index.data
#print P(b0,b1,b2)[1,2,0]##d_index.data
#print ( R(b1,b2)*I(-b1, -b2, b3, b4) ).data
#print O.data
#print  ( G(-b1)*O(b3,b1,b2,b4)*G(-b2) ).data
print  ( G(b1)*G(b2)*R(-b1,-b2) ).data
#*R(b1,b2) ).data
#R.data-=0.5
#S=( R(b1,b2)*R(-b1,-b2) ).data
#R.data+=0.5
#print ( I ).data 
#print ( (R(b1,b2)*I(-b1,-b2, b3, b4) )*P(b0,-b3,-b4) ).data
print sympy.simplify( ( (R(b1,b2)*I(-b1,-b2, b3, b4) )*P(b0,-b3,-b4) ).data[0] )
print sympy.simplify( ( (R(b1,b2)*I(-b1,-b2, b3, b4) )*P(b0,-b3,-b4) ).data[1] )
print sympy.simplify( ( (R(b1,b2)*I(-b1,-b2, b3, b4) )*P(b0,-b3,-b4) ).data[2] )
M=( ( (R(b1,b2)*I(-b1,-b2, b3, b4) )*P(b0,-b3,-b4) ).data[2]+( (R(b1,b2)*I(-b1,-b2, b3, b4) )*P(b0,-b3,-b4) ).data[1]/2)
M=M*(1-M)
print sympy.simplify( ( ( (R(b1,b2)*I(-b1,-b2, b3, b4) )*P(b0,-b3,-b4) ).data[2]-( ( (R(b1,b2)*I(-b1,-b2, b3, b4) )*P(b0,-b3,-b4) ).data[2]+( (R(b1,b2)*I(-b1,-b2, b3, b4) )*P(b0,-b3,-b4) ).data[1]/2)**2)/M )
#print ( P(a0,b0)*P(-a0,-b0) ).data
