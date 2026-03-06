import numpy as np
X=np.array([[1,2,3],[7,4,5],[8,2,4]])
invmat=np.linalg.inv(X.T@X)
y=np.array([[3],[1],[4]])
transformed_transpose=X.T@y
print(invmat@transformed_transpose)
