
import numpy as np
from lmfit import Model
import matplotlib.pyplot as plt
from math import exp

phi = 0.3
Sa = 0.3
Se = Sa
d = 0.71
x = 0

def phos_function(Ka, Kph = 1, I0 = 1):

    a =(Se*x*((exp(-x*(Ka**2 + 2*Sa*Ka)**(1/2))*(exp(2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*((I0*Ka**2*Kph*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) - I0*Ka*Kph*phi + (2*I0*Ka*Kph*Sa*phi)/(Ka**2 + 2*Sa*Ka)**(1/2)) + I0*Ka*Kph*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + (I0*Ka**2*Kph*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0*Ka*Kph*Sa*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - Sa - Ka + Sa*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + (Ka**2 + 2*Sa*Ka)**(1/2)) - (2*I0*Kph*Se*phi*(Ka**2 + 2*Sa*Ka)**(1/2) - 4*I0*Ka*Kph*Sa*phi - 2*I0*Ka*Kph*Se*phi - 4*I0*Kph*Sa*Se*phi - I0*Ka*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Sa*phi*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Ka**2*Kph*phi + I0*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0*Ka**3*Kph*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + 2*I0*Ka**2*Kph*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + (2*I0*Ka**3*Kph*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + 4*I0*Ka*Kph*Sa*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0*Ka*Kph*Se*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 4*I0*Kph*Sa*Se*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0*Ka*Kph*phi*exp(d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - I0*Ka*Kph*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) + 4*I0*Kph*Sa*phi*exp(d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Sa*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - 4*I0*Kph*Se*phi*exp(d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + 2*I0*Kph*Se*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) - I0*Kph*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka*Kph*Sa**2*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka**2*Kph*Sa*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka*Kph*Sa**2*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka**2*Kph*Sa*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2))/(2*(Ka + 2*Sa)*(Se*d + 1)*(Ka*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - Sa - Ka + Sa*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + (Ka**2 + 2*Sa*Ka)**(1/2)))) - Se*(((exp(-x*(Ka**2 + 2*Sa*Ka)**(1/2))*(x*exp(2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*((2*I0*Ka**2*Kph*Se*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) - 2*I0*Ka*Kph*Se*phi + (4*I0*Ka*Kph*Sa*Se*phi)/(Ka**2 + 2*Sa*Ka)**(1/2)) - (exp(2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*(2*I0*Ka*Kph*Se*phi + 4*I0*Kph*Sa*Se*phi + I0*Ka*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2) + 2*I0*Kph*Sa*phi*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Se*phi*(Ka**2 + 2*Sa*Ka)**(1/2) - I0*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka + 2*Sa)))/2 + (exp(-x*(Ka**2 + 2*Sa*Ka)**(1/2))*((2*I0*Ka*Kph*Se*phi + 4*I0*Kph*Sa*Se*phi - I0*Ka*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Sa*phi*(Ka*(Ka + 2*Sa))**(1/2) + 2*I0*Kph*Se*phi*(Ka**2 + 2*Sa*Ka)**(1/2) - I0*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2))/(Ka + 2*Sa) + x*(2*I0*Ka*Kph*Se*phi + (2*I0*Ka**2*Kph*Se*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + (4*I0*Ka*Kph*Sa*Se*phi)/(Ka**2 + 2*Sa*Ka)**(1/2)))*(Sa*Se - Se*(Ka**2 + 2*Sa*Ka)**(1/2) + Ka*Se))/(2*(Sa*Se + Se*(Ka**2 + 2*Sa*Ka)**(1/2) + Ka*Se)))/(Se*(Ka**2 + 2*Sa*Ka)**(1/2) - Sa*Se - Ka*Se + Ka*Se*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + Sa*Se*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + Se*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2)) + (exp(-x*(Ka**2 + 2*Sa*Ka)**(1/2))*((2*I0*Ka*Kph*Se*phi + 4*I0*Kph*Sa*Se*phi - I0*Ka*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Sa*phi*(Ka*(Ka + 2*Sa))**(1/2) + 2*I0*Kph*Se*phi*(Ka**2 + 2*Sa*Ka)**(1/2) - I0*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2))/(Ka + 2*Sa) + x*(2*I0*Ka*Kph*Se*phi + (2*I0*Ka**2*Kph*Se*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + (4*I0*Ka*Kph*Sa*Se*phi)/(Ka**2 + 2*Sa*Ka)**(1/2))))/(2*(Sa*Se + Se*(Ka**2 + 2*Sa*Ka)**(1/2) + Ka*Se)) - (4*I0*Kph*Se*phi*exp(d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) - 4*I0*Kph*Sa*phi*exp(d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Ka*Kph*phi*exp(d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Ka*Kph*Se**2*d*phi - 2*I0*Ka**2*Kph*Se*d*phi - 4*I0*Kph*Sa*Se**2*d*phi + 2*I0*Kph*Se**2*d*phi*(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0*Ka**3*Kph*Se*d*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + 2*I0*Ka*Kph*Se**2*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0*Ka**2*Kph*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 4*I0*Kph*Sa*Se**2*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0*Kph*Se**2*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) - 4*I0*Ka*Kph*Sa*Se*d*phi - I0*Ka*Kph*Se*d*phi*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Sa*Se*d*phi*(Ka*(Ka + 2*Sa))**(1/2) + I0*Kph*Se*d*phi*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2) + 4*I0*Ka*Kph*Sa*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - I0*Ka*Kph*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Sa*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - I0*Kph*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka*Kph*Sa**2*Se*d*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka**2*Kph*Sa*Se*d*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0*Ka**3*Kph*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka*Kph*Sa**2*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka**2*Kph*Sa*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2))/(2*Se*(Ka + 2*Sa)*(Se*d + 1)*(Ka*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - Sa - Ka + Sa*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + (Ka**2 + 2*Sa*Ka)**(1/2)))))
    return a

class outputs:
    par_out = False

    def param_out(self, inf_src, titles_arr, iter_num=0, head="------"):
        if iter_num != 0:
            iter_num_in_func = iter_num
        else:
            iter_num_in_func = len(inf_src)

        if outputs.par_out:  # определение способа вывода данныцх  в файл
            par_out_mode = 'a'
        else:
            par_out_mode = 'w'

        with open('parameters.csv', par_out_mode) as myfile:
            myfile.write(head + '\n')
            for x in range(iter_num_in_func):
                myfile.write(titles_arr[x])
                for key, value in inf_src[x].best_values.items():
                    str_to_file = "{0} = {1:.2f}, ".format(key, value)
                    myfile.write(str_to_file)
                myfile.write("chisqr = {0:.2f}".format(inf_src[x].chisqr))
                myfile.write('\n')

            outputs.par_out = True  # если в ходе программы данная функция была выхвана хоть один раз, и при этом был создан файл с параметрами, то в дальнейшем параметры будут вноситься в этот файл с концеа, а не перезаписываться
        myfile.close()



NUM_OF_EXP = 4
ph = np.array([385.0, 315.0, 290.0, 890.0, 890.0, 1180.5, 987.0, 1091.5, 1035.5, 1159.0, 1111.5, 1064.0, 1178.0])
conc = np.array([3.33333E-5, 3.33333E-5, 5E-5, 1.11111E-4, 2.5E-4, 4.44444E-4, 4.9505E-4, 5.43478E-4, 6.66667E-4, 8.26446E-4, 0.00149, 0.00167, 0.00182]);
dl_fl = np.array([0.39, 0.68, 0.71, 1.76, 2.5, 3.95, 2.495, 3.852, 3.952, 5.28, 5.28, 5.64267, 6.56])
Kaa = np.array([0.49833,0.49833,0.7475,1.66111,3.7375,6.64444,7.40099,8.125,9.96667,12.35537,22.31343,24.91667,27.18182])
Ka_model = np.linspace(0, 30, 30000);


# создание модели для фитинга
phos_model = Model(phos_function)
delflu_model = Model(phos_function)


phos_model_data=phos_model.fit(ph, Ka = Kaa, I0 = 1, Kph = 1)

Kph_best = phos_model_data.best_values['Kph']
I0_best = phos_model_data.best_values['I0']
ph_model = []

for i in Ka_model:
    ph_model.append(phos_function(Ka_model[i], Kph = Kph_best, I0 = I0_best))

a = plt.figure(1)
axe = a.add_subplot(111)
axe.spines['right'].set_visible(False)
axe.spines['top'].set_visible(False)

plt.plot(Kaa, ph, "o", label="Экспериментальные данные")
plt.plot(Ka_model, ph_model, "k--", label="Данные модели", linewidth=1)

plt.xlabel("Коэффициент оптического поглощения, Ka, ", fontsize = 'x-large')
plt.title("Интенсивность, отн. ед.",
           loc = 'left',
          fontsize = 'x-large')