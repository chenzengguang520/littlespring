import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 计算时间函数
def ft(v,shite):
    return 10 / (v * np.cos(shite) * 2 + 50)
# 设置时间，角度，速度得初始值
ans = 1000
ans_v = 0
ans_ang = 0

X = []
Y = []
T = []
# print(T)
# 暴力循环求解
for shite in np.arange(0,np.pi / 2,0.01):
    for v in np.arange(0.2,0.6,0.01):
        t = ft(v,shite)
        flag = v * np.sin(shite) - 0.98 * t
        if np.abs(flag) <= 0.001:
            X.append(shite)
            Y.append(v)
            if ans > t:
                ans = ft(v,shite)
                ans_v = v
                ans_ang = shite
print("当发射速度为%.2f,角度为%.2f的时候时间最短为%.2f"%(ans_v,ans_ang,ans))

# 求解时间T的矩阵
for x in X:
    for y in Y:
        T.append(ft(y,x))
T = np.matrix(T)
# print(T.shape)
T = T.reshape((32,32))
# print(T.shape)
X = np.matrix(X)
Y = np.matrix(Y)

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter3D(ans_ang,ans_v, ans,color='Green')
ax.plot_surface(X,Y,T,)
ax.set_xlabel("角度（弧度制）",fontproperties = 'SimHei',fontsize = 20)
ax.set_ylabel("速度",fontproperties = 'SimHei',fontsize = 20)
ax.set_zlabel("时间",fontproperties = 'SimHei',fontsize = 20)

plt.show()