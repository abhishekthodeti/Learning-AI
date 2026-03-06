import numpy as np
X=np.array([[1,2,3],
           [7,5,2],
           [12,4,3]])
y=np.array([[1],[4],[23]])
XTX_inv = np.linalg.inv(X.T @ X)
weights = XTX_inv @ X.T @ y
predictions=X@weights
mse=np.mean((predictions-y)**2)
print("predictions",predictions)
print("mean square error:",mse)
