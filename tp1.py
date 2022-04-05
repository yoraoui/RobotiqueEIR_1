import  numpy as np
import  matplotlib.pyplot as plt

#Exercice 1
 # 1
angle = np.pi/6
Rx = np.array([[1,0,0],[0, np.cos(angle), -np.sin(angle)],\
               [0, np.sin(angle), np.cos(angle)]])
print("produit = ", Rx[:,1]@Rx[:,0])
print(Rx)
angle = np.pi/4
Ry = np.array([[np.cos(angle),0,np.sin(angle)],[0, 1, 0],\
               [-np.sin(angle),0 , np.cos(angle)]])
print(Ry)
angle = np.pi/2
Rz = np.array([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),\
                                                 np.cos(angle), 0],[0,0 , 1]])
print(Rz)
#3
def RotX(angle):
    Rx = np.array([[1,0,0],[0, np.cos(angle), -np.sin(angle)],\
               [0, np.sin(angle), np.cos(angle)]])
    return  Rx
def RotY(angle):
    Ry = np.array([[np.cos(angle), 0, np.sin(angle)], [0, 1, 0], \
                   [-np.sin(angle), 0, np.cos(angle)]])
    return  Ry
def RotZ(angle):
    Rz = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), \
                                                   np.cos(angle), 0], [0, 0, 1]])
    return  Rz

#4  
Ry = RotY(np.pi/4)
Ah = np.zeros((4,4))
Ah[0:3,0:3]= Ry
Ah[3,3] = 1
Ah[0:3,3] = np.array([2,4,1])
P = np.array([0,0,0,1]).T
Vt = Ah@P
print(Vt)
P = np.array([0,0,0,1])
Ah = np.zeros((4,4))
px = []
py = []
i = 0
Ah = np.zeros((4, 4))


#Exercice 2

def tcomp(x, A):
    tac =  x+ A[0:3, 0:3]@A[:3,3]
    return  tac

def motionModel(x, u):
    Ry = RotZ(u[2])
    Ah[0:3, 0:3] = Ry
    Ah[3, 3] = 1
    Ah[0:3, 3] = np.array([u[0], u[1], u[2]])
    xPred = tcomp(x, Ah)
    return  xPred

u = np.array([[3, 3, np.pi/2],[2, 1, np.pi/2], [1, 3, np.pi/2], [9, 2, np.pi/2]])
x = np.array([0,0,0])
print(u)
xt = []
yt = []
for i in range(u.shape[0]):
    x = motionModel(x, u[i])
    xt.append(x[0])
    yt.append(x[1])
plt.plot(xt, yt, "b")
plt.show()
