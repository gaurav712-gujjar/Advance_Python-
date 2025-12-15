import numpy as np
#4. Extract a 2×2 sub-matrix from a 3×3 matrix.

mat=np.arange(1,10).reshape(3,3)
print(mat[0:2,0:2])