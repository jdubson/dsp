# Matrix Algebra

import numpy as N

# Define matrices

A = N.array([[1, 2, 3], [2, 7, 4]])
B = N.array([[1, -1], [0, 1]])
C = N.array([[5, -1], [9, 1], [6, 0]])
D = N.array([[3, -2, -1], [1, 2, 3]])
u = N.array([[6, 2, -3, 5]])
v = N.array([[3, 5, -1, 4]])
w = N.array([[1], [8], [0], [5]])

num = 6

## 2. Matrix Dimensions
# 1.1) A; 2 x 3
print A.shape

# 1.2) B; 2 x 2
print B.shape

# 1.3) C; 3 x 2
print C.shape

# 1.4) D; 2 x 3
print D.shape

# 1.5) u; 1 x 4
print u.shape

#1.6) w; 4 x 1
print w.shape

## 2. Vector Operations
# 2.1) [9 7 -4 9]
print u + v

#2.2) [3 -3 -2 1]
print u - v

#2.3) [36 12 -18 30]
print num * u

#2.4) 51
print N.vdot(u, v)

#2.5) ~ 8.6
print N.linalg.norm(u)

## 3. Matrix Operations
#3.1) A + C; not defined
try:
    print A + C
except ValueError:
    print 'Not defined'

#3.2) A - C^T; [[-4 7 -3], [3 6 4]]
print A - N.transpose(C)

#3.3) C^T + 3D; [[14 3 3], [2 7 9]]
print N.transpose(C) + (3 * D)

#3.4) BA; [[-1 -5 -1], [2 7 4]]
print N.dot(B, A)

#3.5 BA^T
try:
    print N.dot(B, N.transpose(A))
except ValueError:
    print 'Not defined'
