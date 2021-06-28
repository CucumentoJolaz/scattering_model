import matplotlib.pyplot as plt
from numpy import exp, linspace, random, array, log, zeros_like, abs
import csv
from lmfit import Model

FILENAME = "Sheet1.csv"
NUM_OF_EXP = 3

ph_x = []
ph_y = []
dl_fl_x = []
dl_fl_y = []
Ka = [1.1, 5.5, 11]

for i in range(NUM_OF_EXP):
    ph_x.append([])
    ph_y.append([])
    dl_fl_x.append([])
    dl_fl_y.append([])

def phos_quench(t , Ka = 1, k = 1, ktt = 1, I0 = 1):
    o = 0.7 #theta_isc
    c = k/((1 - o) * ktt)
    a = o*Ka*I0
    b = - Ka
    e = exp( k*t )
    intens = c/(b*(e - 1)) * log(abs(((k + a*exp(b)) * e - a*exp(b))/((k + a) * e - a)))
    return intens

def dlfl_quench(t , Ka = 1, k = 1, ktt = 1, I0 = 1):

    o = 0.7 #theta_isc
    c = k/((1 - o) * ktt)
    a = o*Ka*I0
    b = - Ka
    e = exp( k*t )

    intens = (c/(b * (a * e - 1) ** 2)
              * (log(abs(((a*e - a)*exp(b) + k*e)/((a*e - a) + k*e)))
                 + (a*e - 1 - a * e * exp(b) + exp(b))/(((a*e - a)*exp(b)
                                                         + k*e)*(( a*e - a) + k*e))))
    return intens

with open(FILENAME) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count = 0
    # чтение CSV файла в массив
    for row in readCSV:
        if count >= 0:
            dl_fl_index = 0
            for col in range(NUM_OF_EXP * 2, NUM_OF_EXP * 4, 1):
                if (row[col]):
                    if col % 2:
                        dl_fl_y[dl_fl_index].append(float(row[col]))
                        dl_fl_index += 1
                    else:
                        dl_fl_x[dl_fl_index].append(float(row[col]))

            ph_index = 0
            for col in range(0, NUM_OF_EXP * 2, 1):
                if (row[col]):
                    if col % 2:
                        ph_y[ph_index].append(float(row[col]))
                        ph_index += 1
                    else:
                        ph_x[ph_index].append(float(row[col]))
        count += 1

# создание модели для фитинга
result_dlfl = []
result_ph = []
params = ['k' , 'ktt' , 'I0']
dlfl_model = Model(dlfl_quench)
phos_model = Model(phos_quench)

dlfl_model.set_param_hint('k', value=1, min=0.1, max=300)
phos_model.set_param_hint('k', value=1, min=0.1, max=300)
dlfl_model.set_param_hint('ktt', value=1, min=0.001, max=300)
phos_model.set_param_hint('ktt', value=1, min=0.001, max=300)
#dlfl_model.set_param_hint('I0', value=0.0000015, min=0.000001, max=0.000002)
#phos_model.set_param_hint('I0', value=0.0000015, min=0.000001, max=0.000002)

for i in range(NUM_OF_EXP):
    dlfl_model.set_param_hint('Ka', value=Ka[i], min=Ka[i] - 0.01, max=Ka[i] + 0.01)
    result_dlfl.append(dlfl_model.fit(dl_fl_y[i],
                                      t=dl_fl_x[i],
                                      ))
    phos_model.set_param_hint('Ka', value=Ka[i], min=Ka[i] - 0.01, max=Ka[i] + 0.01)
    result_ph.append(phos_model.fit(ph_y[i],
                                    t=ph_x[i],
                                    ))

ph_x_lin = linspace(0, 10, 10000)
ph_y_lin = []
for i in range(NUM_OF_EXP):
    ph_y_lin.append([])

dl_fl_x_lin = linspace(0, 6, 6000)
dl_fl_y_lin = []
for i in range(NUM_OF_EXP):
    dl_fl_y_lin.append([])

for j in range(NUM_OF_EXP):
    for i in dl_fl_x_lin:
        dl_fl_y_lin[j].append(result_dlfl[j].eval(t=i))

    for i in dl_fl_x_lin:
        ph_y_lin[j].append(result_ph[j].eval(t=i))

a = plt.figure(1)
axe = a.add_subplot(111)
axe.spines['right'].set_visible(False)
axe.spines['top'].set_visible(False)
#plt.title("Delayed fluorescence")
plt.plot([], [], ' ', label="Соотношение\n(моль нафталина)\n/(моль циклодекстрина)")
plt.axis([0, 6, 0, 90])
for i in range(NUM_OF_EXP):
    plt.plot(dl_fl_x[i], dl_fl_y[i],  linewidth=1,)
    plt.plot(dl_fl_x_lin, dl_fl_y_lin[i],  label = "фиттинг", linewidth=0.8)
plt.xlabel("Время, с", fontsize = 'x-large')
plt.title("Интенсивность, отн. ед.",
           loc = 'left',
          fontsize = 'x-large')
#plt.legend(loc='upper right', fontsize = 'x-large', frameon=False)
filename = "Delayed fluorescence 2" + ".png"
plt.show()