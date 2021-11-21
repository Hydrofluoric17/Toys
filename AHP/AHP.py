import numpy as np
import matplotlib.pyplot as plt
#目标层：       评估化工安全事故造成损失的影响
#
#准则层：储量    防护穿透能力    影响范围    介入难度
#
#方案层：     火            爆          毒

def generateRandomMatrix(n):
#生成一个随机正互反矩阵
    #ref = [2,3,4,5,6,7,8,9,1,1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9,1]
    ref = [1,2,3,4,5,6,7,8,9,1/9,1/8,1/7,1/6,1/5,1/4,1/3,1/2,1]
    RDM = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            if i == j:
                RDM[i,j] = 1
            else:
                RDM[i,j] = ref[np.random.randint(0,17)]
    for i in range(n):
        for j in range(i+1,n):
            RDM[j,i] = 1/RDM[i,j]
    return RDM

def generateRI(n,loop=1000):
#生成n阶随机一致性指标
    RI = 0
    for num in range(loop):
        randomMatrix = generateRandomMatrix(n)
        eigenValues = np.linalg.eigvals(randomMatrix)
        maximum = max(eigenValues)
        summation = sum(eigenValues)
        CI = (maximum - summation)/(summation - 1)
        RI += CI
    return (RI/loop).real

refRI = [0,0.52,0.89,1.12,1.26,1.36,1.41,1.46,1.49,1.52,1.54,1.56,1.58,1.59]
testRI=[]
x = np.arange(2,16,1)
y = np.arange(2,40,1)
for i in range(2,40):
    if i < 16:
        testRI.append(generateRI(i,10000))
    else:
        testRI.append(generateRI(i,1000))
print(testRI)
plt.plot(x,refRI,color="r",marker="^",label="Reference")
plt.plot(y,testRI,color="b",marker="s",label="Experiment")
plt.legend(loc='lower right',frameon=True)
plt.show()