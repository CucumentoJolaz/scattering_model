
import matplotlib.pyplot as plt
from numpy import exp, linspace, random, array, log, zeros_like

def phos_function(x, Ka = 1, I0 = 1):

    I = I0*exp(-Ka*x)
    return I

Ka = array([0.49833,0.49833,0.7475,1.66111,3.7375,6.64444,7.40099,8.125,9.96667,12.35537,22.31343,24.91667, 27.18182])

x = linspace(0, 1, 200)
I = []
x_max = []
for j in range(len(Ka)):
    I.append(zeros_like(x))
    for i in range(len(x)):
        I[j][i] = phos_function(x[i], Ka = Ka[j], I0 = 1)
        if I[j][i] < 0.01:
            x_max

a = plt.figure(3)
axe = a.add_subplot(111)
axe.spines['right'].set_visible(False)
axe.spines['top'].set_visible(False)


for j in range(len(Ka)):
    plt.plot(x,I[j], "-", label =r'$K_{a} = $' + str(Ka[j]), linewidth=1)

plt.xlabel("Длина оптического пути", fontsize = 'x-large')
plt.ylabel("Интенсивность света, отн. ед.",
          fontsize = 'x-large')
plt.legend()
plt.show()
