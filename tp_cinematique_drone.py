import numpy as np
""""
#1
R = np.array([[np.sqrt(2)/2, 0, np.sqrt(2)/2],[0, 1, 0], [-np.sqrt(2)/2, 0, np.sqrt(2)/2]])
detR = np.linalg.det(R)
print(detR)
print(R@R.T)

#2
R = np.array([[0.2120, 0.7743, 0.5963],[0.2120, -0.6321, 0.7454], [0.9540, -0.0316, -0.2981]])
detR = np.linalg.det(R)
print(detR)
print(R@R.T)

#3
R = np.array([[0.3835, 0.5730, 0.9287],[0.5710, 0.5919, -0.4119], [-1.3954, 0.0217, 1.1105]])
detR = np.linalg.det(R)
print(detR)
print(R@R.T)

#4
"""
R = np.array([[0.675, -0.1724, 0.7174], [0.2474, 0.9689, 0], [-0.6951, 0.1775, 0.6967]])
wb = np.array([[0, -1, 0.9689], [1, 0, -0.2474], [-0.9689, 0.2474, 0]])
dR = R@wb
print("dR = ", dR)
ws = dR@R.T
print("ws =", ws)
#4
R = np.array([[0.2919, 0.643, -0.7081], [-0.643, -0.4161, -0.643], [-0.7081, 0.643, 0.2919]])
cphi = (np.trace(R)-1)/2
phi = np.arccos(cphi)
print("Phi = ", phi)
u_hat = (1/(2*np.sin(phi)))*(R-R.T)
print("u_hat = ", u_hat)
