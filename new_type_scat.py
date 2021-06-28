from numpy import exp, linspace, random, array, log, zeros_like
from scipy.integrate import quad
import matplotlib.pyplot as plt
import sympy as sym
import statistics as st

def del_flu_sym(x ,Ka = 1, Ktt = 0.5):

    tau_phos = 2
    tau_sing = 120*10**(-9)
    Ks = 1/tau_sing * 0.3
    epsi = 6500
    kt = 1/tau_phos
    ks = 1 /tau_sing
    #Ka = conc*epsi
    theta = 0.7
    T0 = theta*Ka*sym.exp(-Ka* x)
    a = kt/(kt + (1 - theta)*Ktt*T0)
    b = ((1 - theta)*Ktt*T0)/(kt + (1 - theta)*Ktt*T0)
    c = a**2 * Ktt/ks
    S1 = c/ (b**2 * kt) * (sym.log(sym.Abs(b - 1)) - b/( b - 1))
    intens = Ks * S1
    return intens

def del_flu(x, Ka = 1, Ktt = 0.5):

    tau_phos = 2
    tau_sing = 120*10**(-9)
    Ks = 1/tau_sing * 0.3
    kt = 1/tau_phos
    ks = 1/tau_sing
    theta = 0.7
    T0 = theta*Ka*exp(-Ka*x)

    b = ((1 - theta)*Ktt*T0)/(kt + (1 - theta)*Ktt*T0)

    S1 = 1/Ktt*kt/ks/0.09*(log(abs(b - 1)) - b/(b - 1))
    intens = Ks * S1
    return intens

def phos_exp(Ka, Kph = 1, Const2 = 1):
    return 0.3*Kph*(1 - exp(-Const2*Ka))

def phos_model(x, Ka = 1, Ktt = 0.5):

    tau_phos = 2
    tau_sing = 120*10**(-9)
    Kph = 1/tau_phos * 0.3
    kt = 1/tau_phos
    ks = 1/tau_sing
    theta = 0.7
    T0 = theta*Ka*exp(-Ka*x)
    b = ((1 - theta)*Ktt*T0)/(kt + (1 - theta)*Ktt*T0)
    intens = Kph * log(abs(b - 1))/((1 - theta)*Ktt)
    return intens

Ka = sym.Symbol('Ka')
Ks = sym.Symbol('Ks')
kt = sym.Symbol('kt')
theta = sym.Symbol('theta')
ks = sym.Symbol('ks')
Ktt = sym.Symbol('Ktt')
x = sym.Symbol('x')
#dlfl_function = sym.Function(Ks * kt/(kt + (1 - theta)*Ktt*theta*(1 - sym.exp(-Ka)))**2 *Ktt/ks * (sym.log(sym.Abs((1 - theta)*Ktt*theta*Ka*sym.exp(-Ka)/(kt + (1 - theta)*Ktt*theta*Ka*sym.exp(-Ka)) - 1))/((1 - theta)*Ktt*theta*Ka*sym.exp(-Ka)/(kt + (1 - theta)*Ktt*theta*Ka*sym.exp(-Ka))**2 * kt) - 1)/ ((1 - theta)*Ktt*theta*Ka*sym.exp(-Ka)/(kt + (1 - theta)*Ktt*theta*Ka*sym.exp(-Ka)) * kt * ((1 - theta)*Ktt*theta*Ka*sym.exp(-Ka)/(kt + (1 - theta)*Ktt*theta*Ka*sym.exp(-Ka)) - 1)))
#dlfl_integral = sym.integrate(del_flu_sym(x), (x, 0, 1))


ph = array([385.0, 315.0, 290.0, 890.0, 890.0, 1180.5, 987.0, 1091.5, 1035.5, 1159.0, 1111.5, 1064.0, 1178.0])
Ka = array([0.49833,0.49833,0.7475,1.66111,3.7375,6.64444,7.40099,8.125,9.96667,12.35537,22.31343,24.91667 , 27.18182])
dl_fl = array([0.39, 0.68, 0.71, 1.76, 2.5, 3.95, 2.495, 3.852, 3.952, 5.28, 5.28, 5.64267, 6.56])

dlfl_func = zeros_like(ph)
Ka_theor = linspace(0, 30, 5000)

ktt_base = [0.01, 0.05, 0.1, 0.5, 0.8, 1, 2]


#ktt_base2 = 0.3
dlfl_theor = []
ph_theor = []

for j in range(len(ktt_base)):
    dlfl_theor.append(zeros_like(Ka_theor))
    ph_theor.append(zeros_like(Ka_theor))
    for i in range(len(Ka_theor)):
    #     #dlfl_func[i] = del_flu(1, Ka[i], Ktt = ktt_base2)
        dlfl_theor[j][i] = quad(del_flu, 0, 1, args = (Ka_theor[i],ktt_base[j]))[0]
        ph_theor[j][i] = quad(phos_model, 0, 1, args = (Ka_theor[i],ktt_base[j]))[0]
    #     #print(quad(del_flu, 0, 1, args = (Ka[i],ktt_base)))


I0_dlfl = 1.3
I0_ph = 1.2

a = plt.figure(2)
axe = a.add_subplot(111)
axe.spines['right'].set_visible(False)
axe.spines['top'].set_visible(False)
plt.plot(Ka, dl_fl/st.mean(dl_fl), "s", label="Экспериментальные данные",MarkerSize= 10, MarkerFaceColor='tomato')

for j in range(len(ktt_base)):
    plt.plot(Ka_theor, I0_dlfl*dlfl_theor[j]/st.mean(dlfl_theor[j]), "-", label = r'$K_{t-t} = $' + str(ktt_base[j]), linewidth=1)


plt.xlabel("Коэффициент оптического поглощения раствора, Ka, ", fontsize = 'x-large')
plt.ylabel("Интенсивность замедленной \n флуоресценции, отн. ед.",
          fontsize = 'x-large')
plt.legend()
plt.show()

a = plt.figure(3)
axe = a.add_subplot(111)
axe.spines['right'].set_visible(False)
axe.spines['top'].set_visible(False)

plt.plot(Ka, ph/st.mean(ph), "s", label="Экспериментальные данные",MarkerSize= 10, MarkerFaceColor='tomato')

for j in range(len(ktt_base)):
    plt.plot(Ka_theor, I0_ph*ph_theor[j]/st.mean(ph_theor[j]), "-", label =r'$K_{t-t} = $' + str(ktt_base[j]), linewidth=1)

plt.xlabel("Коэффициент оптического поглощения раствора, Ka, ", fontsize = 'x-large')
plt.ylabel("Интенсивность фосфоресценции \n, отн. ед.",
          fontsize = 'x-large')
plt.legend()
plt.show()
