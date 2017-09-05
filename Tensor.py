from sympy.tensor.tensor import tensor_indices, tensorhead, TensorIndexType, TensorType
import sympy

d_index = TensorIndexType('d_index', dummy_fmt='L')
#z_index = TensorIndexType('z_index', dummy_fmt='L')

P = tensorhead('P', [d_index, d_index, d_index], [[1],[1],[1]])
R = tensorhead('R', [d_index, d_index, d_index, d_index], [[1], [1], [1], [1]])
#I = tensorhead('I', [z_index, z_index, z_index, z_index], [[1]])

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
p=0.5#sympy.Symbol('p')
q=1-p

R.data = [[[[ 1./81. for i in range(3)] for j in range(3)]  for k in range(3)]  for l in range(3)] 

G
#print h_index.data
#print P(b0,b1,b2)[0,0,0]##d_index.data
#print P(b0,b1,b2)[1,2,0]##d_index.data

print ( P(b0, -b1, -b2)*P(b3, -b4, -b5)*R(b1,b2,b4,b5) ).data
#print ( P(a0,b0)*P(-a0,-b0) ).data
