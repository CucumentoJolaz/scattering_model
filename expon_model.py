from numpy import exp, linspace, random, array, log, zeros_like
from scipy.integrate import quad
import matplotlib.pyplot as plt
import statistics as st

tau_phos = 2
tau_sing = 120 * 10 ** (-9)
Kph = 1 / tau_phos * 0.3
kt = 1 / tau_phos
ks = 1 / tau_sing
theta = 0.7

def del_flu_model(x, Ka = 1, I0 = 1, ktt = 1):
    intens = ktt * Ka / (4*kt*ks) * (theta * I0)**2 *(1 - exp(-2*Ka*x))
    return intens

# def del_flu_model_x_def(intens, Ka = 1, I0 = 1, ktt = 1):
#     a = 1 - intens/(ktt * Ka / (4*kt*ks) * (theta * I0)**2)
#     x = 1 / (-2*Ka) * log(a)
#     return x

def del_flu_model_x_def(intens, Ka = 1, I0 = 1, ktt = 1):
     a = 1 - intens/(ktt * Ka / (4*kt*ks) * (theta * I0)**2)
     x = 1 / (-2*Ka) * log(a)
     return x
def phos_model(x, Ka = 1, I0 = 1):
    intens = theta * I0 / kt * (1 - exp(-Ka*x))
    return intens

def phos_model_x_def(intens, Ka = 1, I0 = 1):
    x = - 1 / Ka *log(1 - intens / (theta * I0 / kt))
    return x


ph = array([385.0, 315.0, 290.0, 890.0, 890.0, 1180.5, 987.0, 1091.5, 1035.5, 1159.0, 1111.5, 1064.0, 1178.0])
Ka = array([0.49833,0.49833,0.7475,1.66111,3.7375,6.64444,7.40099,8.125,9.96667,12.35537,22.31343,24.91667, 27.18182])
dl_fl = array([0.39, 0.68, 0.71, 1.76, 2.5, 3.95, 2.495, 3.852, 3.952, 5.28, 5.28, 5.64267, 6.56])

dlfl_func = zeros_like(ph)
Ka_theor = linspace(0, 30, 5000)


dlfl_theor = zeros_like(dl_fl)
ph_theor = zeros_like(dl_fl)
opt_way_by_dlfl = zeros_like(dl_fl)
opt_way_by_ph = zeros_like(ph)
#рассчёт опт. пути по замедленной флуоресценции
for i in range(len(opt_way_by_dlfl)):
    opt_way_by_dlfl[i] = del_flu_model_x_def(intens = dl_fl[i], Ka = Ka[i], I0 = 50000)
    dlfl_theor[i] = del_flu_model(x = opt_way_by_dlfl[i], Ka = Ka[i], I0 = 50000)
    ph_theor[i] = phos_model(x = opt_way_by_dlfl[i], Ka = Ka[i], I0 = 50000)

# рассчёт опт. пути через опт. плотность
# max_opt_dencity = phos_model_x_def(1150, Ka = 10, I0 = 50000)
# for i in range(len(opt_way_by_dlfl)):
#     dlfl_theor[i] = del_flu_model(x = max_opt_dencity/Ka[i], Ka = Ka[i], I0 = 50000)
#     if i > 4:
#         opt_way_by_ph[i] = max_opt_dencity / Ka[i]
#     elif i <=4:
#         opt_way_by_ph[i] = phos_model_x_def(ph[i], Ka = Ka[i], I0 = 50000)
#     ph_theor[i] = phos_model(opt_way_by_ph[i], Ka = Ka[i], I0 = 50000)

# рассчёт опт. пути по фосфоресценции
# for i in range(len(opt_way_by_dlfl)):
    # opt_way_by_ph[i] = phos_model_x_def(intens = ph[i], Ka = Ka[i], I0 = 50000)
    # dlfl_theor[i] = del_flu_model(x = opt_way_by_ph[i], Ka = Ka[i], I0 = 50000)
    # ph_theor[i] = phos_model(x = opt_way_by_ph[i], Ka = Ka[i], I0 = 50000)


a = plt.figure(2)
axe = a.add_subplot(111)
axe.spines['right'].set_visible(False)
axe.spines['top'].set_visible(False)
plt.plot(Ka, dl_fl, "s", label="Экспериментальные данные",MarkerSize= 10, MarkerFaceColor='tomato')
plt.plot(Ka, dlfl_theor, "-", label = r'$K_{A} = $', linewidth=1)
plt.xlabel("Коэффициент оптического поглощения, Ka, ", fontsize = 'x-large')
plt.ylabel("Интенсивность, отн. ед.",
          fontsize = 'x-large')
plt.legend()
plt.show()

a = plt.figure(3)
axe = a.add_subplot(111)
axe.spines['right'].set_visible(False)
axe.spines['top'].set_visible(False)
plt.plot(Ka, opt_way_by_dlfl, "s", label="оптический путь от Ка",MarkerSize= 10, MarkerFaceColor='tomato')
plt.xlabel("Коэффициент оптического поглощения, Ka, ", fontsize = 'x-large')
plt.ylabel("Оптический путь, см",
          fontsize = 'x-large')
plt.legend()
plt.show()

a = plt.figure(4)
axe = a.add_subplot(111)
axe.spines['right'].set_visible(False)
axe.spines['top'].set_visible(False)
plt.plot(Ka, ph, "s", label="Экспериментальные данные",MarkerSize= 10, MarkerFaceColor='tomato')
plt.plot(Ka, ph_theor, "-", label = r'$K_{A} = $', linewidth=1)
plt.xlabel("Коэффициент оптического поглощения, Ka, ", fontsize = 'x-large')
plt.ylabel("Интенсивность, отн. ед.",
          fontsize = 'x-large')
plt.legend()
plt.show()