from lmfit import Model
import matplotlib.pyplot as plt
from numpy import exp, linspace, random, array

phi = 0.3
d = 0.71
alpha = 0.5
x = 0
Se = 1
Sa = 1

def phos_function(Ka, Kph = 1, I0 = 1, Sa = 1):
    beta = (Ka/(Ka + 2*Sa))**0.5
    Ra = (1 - beta)/(1 + beta)
    a =phi*Kph*I0*(1 - Ra)
    return a

def phos_exp(Ka, Kph = 1, Const2 = 1):
    return phi*Kph*(1 - exp(-Const2*Ka))

def phos_munk(Ka, Kph = 1, I0 = 1):
    return Se*x*((exp(-x*(Ka**2 + 2*Sa*Ka)**(1/2))*(exp(2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*((I0*Ka**2*Kph*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) - I0*Ka*Kph*phi + (2*I0*Ka*Kph*Sa*phi)/(Ka**2 + 2*Sa*Ka)**(1/2)) + I0*Ka*Kph*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + (I0*Ka**2*Kph*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0*Ka*Kph*Sa*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - Sa - Ka + Sa*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + (Ka**2 + 2*Sa*Ka)**(1/2)) - (2*I0*Kph*Se*phi*(Ka**2 + 2*Sa*Ka)**(1/2) - 4*I0*Ka*Kph*Sa*phi - 2*I0*Ka*Kph*Se*phi - 4*I0*Kph*Sa*Se*phi - I0*Ka*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Sa*phi*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Ka**2*Kph*phi + I0*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0*Ka**3*Kph*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + 2*I0*Ka**2*Kph*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + (2*I0*Ka**3*Kph*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + 4*I0*Ka*Kph*Sa*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0*Ka*Kph*Se*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 4*I0*Kph*Sa*Se*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0*Ka*Kph*phi*exp(d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - I0*Ka*Kph*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) + 4*I0*Kph*Sa*phi*exp(d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Sa*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - 4*I0*Kph*Se*phi*exp(d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + 2*I0*Kph*Se*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) - I0*Kph*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka*Kph*Sa**2*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka**2*Kph*Sa*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka*Kph*Sa**2*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka**2*Kph*Sa*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2))/(2*(Ka + 2*Sa)*(Se*d + 1)*(Ka*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - Sa - Ka + Sa*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + (Ka**2 + 2*Sa*Ka)**(1/2)))) - Se*(((exp(-x*(Ka**2 + 2*Sa*Ka)**(1/2))*(x*exp(2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*((2*I0*Ka**2*Kph*Se*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) - 2*I0*Ka*Kph*Se*phi + (4*I0*Ka*Kph*Sa*Se*phi)/(Ka**2 + 2*Sa*Ka)**(1/2)) - (exp(2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*(2*I0*Ka*Kph*Se*phi + 4*I0*Kph*Sa*Se*phi + I0*Ka*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2) + 2*I0*Kph*Sa*phi*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Se*phi*(Ka**2 + 2*Sa*Ka)**(1/2) - I0*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka + 2*Sa)))/2 + (exp(-x*(Ka**2 + 2*Sa*Ka)**(1/2))*((2*I0*Ka*Kph*Se*phi + 4*I0*Kph*Sa*Se*phi - I0*Ka*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Sa*phi*(Ka*(Ka + 2*Sa))**(1/2) + 2*I0*Kph*Se*phi*(Ka**2 + 2*Sa*Ka)**(1/2) - I0*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2))/(Ka + 2*Sa) + x*(2*I0*Ka*Kph*Se*phi + (2*I0*Ka**2*Kph*Se*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + (4*I0*Ka*Kph*Sa*Se*phi)/(Ka**2 + 2*Sa*Ka)**(1/2)))*(Sa*Se - Se*(Ka**2 + 2*Sa*Ka)**(1/2) + Ka*Se))/(2*(Sa*Se + Se*(Ka**2 + 2*Sa*Ka)**(1/2) + Ka*Se)))/(Se*(Ka**2 + 2*Sa*Ka)**(1/2) - Sa*Se - Ka*Se + Ka*Se*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + Sa*Se*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + Se*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2)) + (exp(-x*(Ka**2 + 2*Sa*Ka)**(1/2))*((2*I0*Ka*Kph*Se*phi + 4*I0*Kph*Sa*Se*phi - I0*Ka*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Sa*phi*(Ka*(Ka + 2*Sa))**(1/2) + 2*I0*Kph*Se*phi*(Ka**2 + 2*Sa*Ka)**(1/2) - I0*Kph*phi*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2))/(Ka + 2*Sa) + x*(2*I0*Ka*Kph*Se*phi + (2*I0*Ka**2*Kph*Se*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + (4*I0*Ka*Kph*Sa*Se*phi)/(Ka**2 + 2*Sa*Ka)**(1/2))))/(2*(Sa*Se + Se*(Ka**2 + 2*Sa*Ka)**(1/2) + Ka*Se)) - (4*I0*Kph*Se*phi*exp(d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) - 4*I0*Kph*Sa*phi*exp(d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Ka*Kph*phi*exp(d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Ka*Kph*Se**2*d*phi - 2*I0*Ka**2*Kph*Se*d*phi - 4*I0*Kph*Sa*Se**2*d*phi + 2*I0*Kph*Se**2*d*phi*(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0*Ka**3*Kph*Se*d*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + 2*I0*Ka*Kph*Se**2*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0*Ka**2*Kph*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 4*I0*Kph*Sa*Se**2*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0*Kph*Se**2*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) - 4*I0*Ka*Kph*Sa*Se*d*phi - I0*Ka*Kph*Se*d*phi*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Sa*Se*d*phi*(Ka*(Ka + 2*Sa))**(1/2) + I0*Kph*Se*d*phi*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2) + 4*I0*Ka*Kph*Sa*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - I0*Ka*Kph*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - 2*I0*Kph*Sa*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - I0*Kph*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka*Kph*Sa**2*Se*d*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka**2*Kph*Sa*Se*d*phi)/(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0*Ka**3*Kph*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka*Kph*Sa**2*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + (8*I0*Ka**2*Kph*Sa*Se*d*phi*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2))/(2*Se*(Ka + 2*Sa)*(Se*d + 1)*(Ka*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - Sa - Ka + Sa*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + (Ka**2 + 2*Sa*Ka)**(1/2))))

def dlfl_munk(Ka, Kdlfl = 1, I0 = 1):
    return (- Se*((exp(2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*(x**2*exp(-2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*(2*I0**2*Ka**3*Kdlfl*Sa*Se*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 4*I0**2*Ka**2*Kdlfl*Sa**2*Se*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))) - x*exp(-2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*(2*I0**2*Ka**3*Kdlfl*Sa*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 4*I0**2*Ka**2*Kdlfl*Sa**2*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))) - x*((I0**2*Ka**4*Kdlfl*Se*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2) - 2*I0**2*Ka**2*Kdlfl*Sa*Se*alpha - I0**2*Ka**3*Kdlfl*Se*alpha + (3*I0**2*Ka**3*Kdlfl*Sa*Se*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0**2*Ka**2*Kdlfl*Sa**2*Se*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2)) - (I0**2*Ka*Kdlfl*alpha*(Ka**2 + 2*Sa*Ka))/2 + (I0**2*Ka**2*Kdlfl*Se*alpha)/2 + (I0**2*Ka**2*Kdlfl*alpha*(Ka**2 + 2*Sa*Ka)**(1/2))/2 + (I0**2*Ka*Kdlfl*Sa*Se*alpha)/2 + (I0**2*Ka*Kdlfl*Sa*alpha*(Ka**2 + 2*Sa*Ka)**(1/2))/2 - (I0**2*Ka*Kdlfl*Se*alpha*(Ka**2 + 2*Sa*Ka)**(1/2))/2) - (exp(2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*(exp(-4*x*(Ka**2 + 2*Sa*Ka)**(1/2))*((I0**2*Ka**2*Kdlfl*Se*alpha)/2 - (I0**2*Ka**2*Kdlfl*alpha*(Ka*(Ka + 2*Sa))**(1/2))/2 + (I0**2*Ka*Kdlfl*Sa*Se*alpha)/2 - (I0**2*Ka*Kdlfl*Sa*alpha*(Ka*(Ka + 2*Sa))**(1/2))/2 + (I0**2*Ka*Kdlfl*Se*alpha*(Ka**2 + 2*Sa*Ka)**(1/2))/2 - (I0**2*Ka*Kdlfl*alpha*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2))/2) + x*exp(-4*x*(Ka**2 + 2*Sa*Ka)**(1/2))*(I0**2*Ka**3*Kdlfl*Se*alpha + 2*I0**2*Ka**2*Kdlfl*Sa*Se*alpha + (I0**2*Ka**4*Kdlfl*Se*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2) + (3*I0**2*Ka**3*Kdlfl*Sa*Se*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0**2*Ka**2*Kdlfl*Sa**2*Se*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2)))*(2*Ka**2*Se + Sa**2*Se + 4*Ka*Sa*Se - 2*Ka*Se*(Ka**2 + 2*Sa*Ka)**(1/2) - 2*Sa*Se*(Ka**2 + 2*Sa*Ka)**(1/2) - 2*Sa**2*Se*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))))/(2*Ka**2*Se + Sa**2*Se + 4*Ka*Sa*Se + 2*Ka*Se*(Ka**2 + 2*Sa*Ka)**(1/2) + 2*Sa*Se*(Ka**2 + 2*Sa*Ka)**(1/2)))/(2*Ka**2*Se + Sa**2*Se + 4*Ka*Sa*Se - 2*Ka*Se*(Ka**2 + 2*Sa*Ka)**(1/2) - 2*Sa*Se*(Ka**2 + 2*Sa*Ka)**(1/2) + 2*Ka**2*Se*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - 2*Sa**2*Se*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + Sa**2*Se*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 4*Ka*Sa*Se*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*Ka*Se*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + 2*Sa*Se*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2)) + (exp(2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*(exp(-4*x*(Ka**2 + 2*Sa*Ka)**(1/2))*((I0**2*Ka**2*Kdlfl*Se*alpha)/2 - (I0**2*Ka**2*Kdlfl*alpha*(Ka*(Ka + 2*Sa))**(1/2))/2 + (I0**2*Ka*Kdlfl*Sa*Se*alpha)/2 - (I0**2*Ka*Kdlfl*Sa*alpha*(Ka*(Ka + 2*Sa))**(1/2))/2 + (I0**2*Ka*Kdlfl*Se*alpha*(Ka**2 + 2*Sa*Ka)**(1/2))/2 - (I0**2*Ka*Kdlfl*alpha*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2))/2) + x*exp(-4*x*(Ka**2 + 2*Sa*Ka)**(1/2))*(I0**2*Ka**3*Kdlfl*Se*alpha + 2*I0**2*Ka**2*Kdlfl*Sa*Se*alpha + (I0**2*Ka**4*Kdlfl*Se*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2) + (3*I0**2*Ka**3*Kdlfl*Sa*Se*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0**2*Ka**2*Kdlfl*Sa**2*Se*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2))))/(2*Ka**2*Se + Sa**2*Se + 4*Ka*Sa*Se + 2*Ka*Se*(Ka**2 + 2*Sa*Ka)**(1/2) + 2*Sa*Se*(Ka**2 + 2*Sa*Ka)**(1/2)) - (I0**2*Ka**3*Kdlfl*Se*alpha*d - I0**2*Ka**3*Kdlfl*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - 2*I0**2*Ka**2*Kdlfl*Sa*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0**2*Ka**2*Kdlfl*Se*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - I0**2*Ka**2*Kdlfl*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) + I0**2*Ka**2*Kdlfl*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + I0**2*Ka**2*Kdlfl*Se**2*alpha*d - 8*I0**2*Ka**2*Kdlfl*Sa**2*alpha*d*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + I0**2*Ka**2*Kdlfl*Se**2*alpha*d*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0**2*Ka*Kdlfl*Sa*Se*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - I0**2*Ka*Kdlfl*Sa*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) + I0**2*Ka*Kdlfl*Sa*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) - I0**2*Ka*Kdlfl*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2) + I0**2*Ka*Kdlfl*Sa*Se**2*alpha*d + 2*I0**2*Ka**2*Kdlfl*Sa*Se*alpha*d - I0**2*Ka*Kdlfl*Se**2*alpha*d*(Ka**2 + 2*Sa*Ka)**(1/2) + I0**2*Ka**2*Kdlfl*Se*alpha*d*(Ka**2 + 2*Sa*Ka)**(1/2) - (2*I0**2*Ka**4*Kdlfl*Se*alpha*d)/(Ka**2 + 2*Sa*Ka)**(1/2) - 4*I0**2*Ka**3*Kdlfl*Sa*alpha*d*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0**2*Ka**3*Kdlfl*Se*alpha*d*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - I0**2*Ka**2*Kdlfl*Se*alpha*d*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) + I0**2*Ka*Kdlfl*Se**2*alpha*d*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0**2*Ka**4*Kdlfl*Se*alpha*d*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) - (4*I0**2*Ka**2*Kdlfl*Sa**2*Se*alpha*d)/(Ka**2 + 2*Sa*Ka)**(1/2) - 4*I0**2*Ka**3*Kdlfl*Sa*Se*alpha*d**2*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + I0**2*Ka*Kdlfl*Sa*Se*alpha*d*(Ka**2 + 2*Sa*Ka)**(1/2) - 8*I0**2*Ka**2*Kdlfl*Sa**2*Se*alpha*d**2*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - (6*I0**2*Ka**3*Kdlfl*Sa*Se*alpha*d)/(Ka**2 + 2*Sa*Ka)**(1/2) + I0**2*Ka*Kdlfl*Sa*Se**2*alpha*d*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 4*I0**2*Ka**2*Kdlfl*Sa*Se*alpha*d*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - I0**2*Ka*Kdlfl*Sa*Se*alpha*d*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - I0**2*Ka*Kdlfl*Se*alpha*d*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2) + (6*I0**2*Ka**3*Kdlfl*Sa*Se*alpha*d*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + (4*I0**2*Ka**2*Kdlfl*Sa**2*Se*alpha*d*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2))/(2*Se*(Se*d + 1)*(2*Ka**2*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - 2*Sa*(Ka**2 + 2*Sa*Ka)**(1/2) - 2*Ka*(Ka**2 + 2*Sa*Ka)**(1/2) - 2*Sa**2*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + Sa**2*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*Ka**2 + Sa**2 + 4*Ka*Sa + 4*Ka*Sa*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*Ka*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + 2*Sa*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2)))) - Se*x*((I0**2*Ka**3*Kdlfl*alpha + 2*I0**2*Ka**2*Kdlfl*Sa*alpha + I0**2*Ka**2*Kdlfl*Se*alpha + I0**2*Ka**2*Kdlfl*alpha*(Ka**2 + 2*Sa*Ka)**(1/2) - (2*I0**2*Ka**4*Kdlfl*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2) + I0**2*Ka**3*Kdlfl*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0**2*Ka**3*Kdlfl*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - (6*I0**2*Ka**3*Kdlfl*Sa*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2) + 2*I0**2*Ka**2*Kdlfl*Sa*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 4*I0**2*Ka**2*Kdlfl*Sa*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - 2*I0**2*Ka**2*Kdlfl*Se*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + I0**2*Ka**2*Kdlfl*Se*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + I0**2*Ka**2*Kdlfl*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - I0**2*Ka**2*Kdlfl*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - I0**2*Ka**2*Kdlfl*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0**2*Ka**4*Kdlfl*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) - (4*I0**2*Ka**2*Kdlfl*Sa**2*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2) + I0**2*Ka*Kdlfl*Sa*Se*alpha + I0**2*Ka*Kdlfl*Sa*alpha*(Ka**2 + 2*Sa*Ka)**(1/2) - I0**2*Ka*Kdlfl*Se*alpha*(Ka**2 + 2*Sa*Ka)**(1/2) + 8*I0**2*Ka**2*Kdlfl*Sa**2*alpha*d*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + (4*I0**2*Ka**2*Kdlfl*Sa**2*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) - 2*I0**2*Ka*Kdlfl*Sa*Se*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + I0**2*Ka*Kdlfl*Sa*Se*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + I0**2*Ka*Kdlfl*Sa*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - I0**2*Ka*Kdlfl*Sa*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2) - I0**2*Ka*Kdlfl*Sa*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + I0**2*Ka*Kdlfl*Se*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + I0**2*Ka*Kdlfl*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2) - I0**2*Ka*Kdlfl*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka*(Ka + 2*Sa))**(1/2)*(Ka**2 + 2*Sa*Ka)**(1/2) + 4*I0**2*Ka**3*Kdlfl*Sa*alpha*d*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + (6*I0**2*Ka**3*Kdlfl*Sa*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + 4*I0**2*Ka**3*Kdlfl*Sa*Se*alpha*d**2*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 8*I0**2*Ka**2*Kdlfl*Sa**2*Se*alpha*d**2*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(2*(Se*d + 1)*(2*Ka**2*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - 2*Sa*(Ka**2 + 2*Sa*Ka)**(1/2) - 2*Ka*(Ka**2 + 2*Sa*Ka)**(1/2) - 2*Sa**2*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + Sa**2*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*Ka**2 + Sa**2 + 4*Ka*Sa + 4*Ka*Sa*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*Ka*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + 2*Sa*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2))) - (exp(2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*(exp(-4*x*(Ka**2 + 2*Sa*Ka)**(1/2))*(I0**2*Ka**3*Kdlfl*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*I0**2*Ka**2*Kdlfl*Sa*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + (I0**2*Ka**4*Kdlfl*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + (2*I0**2*Ka**2*Kdlfl*Sa**2*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2) + (3*I0**2*Ka**3*Kdlfl*Sa*alpha*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)))/(Ka**2 + 2*Sa*Ka)**(1/2)) + x*exp(-2*x*(Ka**2 + 2*Sa*Ka)**(1/2))*(4*I0**2*Ka**3*Kdlfl*Sa*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 8*I0**2*Ka**2*Kdlfl*Sa**2*alpha*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2))) + I0**2*Ka**3*Kdlfl*alpha + 2*I0**2*Ka**2*Kdlfl*Sa*alpha - (I0**2*Ka**4*Kdlfl*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2) - (3*I0**2*Ka**3*Kdlfl*Sa*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2) - (2*I0**2*Ka**2*Kdlfl*Sa**2*alpha)/(Ka**2 + 2*Sa*Ka)**(1/2)))/(2*Ka**2*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) - 2*Sa*(Ka**2 + 2*Sa*Ka)**(1/2) - 2*Ka*(Ka**2 + 2*Sa*Ka)**(1/2) - 2*Sa**2*exp(2*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + Sa**2*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*Ka**2 + Sa**2 + 4*Ka*Sa + 4*Ka*Sa*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2)) + 2*Ka*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2) + 2*Sa*exp(4*d*(Ka**2 + 2*Sa*Ka)**(1/2))*(Ka**2 + 2*Sa*Ka)**(1/2))))

# def phos_no_back(Ka, Kph, ):
#     B1 = 1 + beta
#     B2 = 1 - beta
#     C3 = 1/(alpha**2) * (-1*(C1 * exp(alpha*d) + C2*exp(-alpha*d))

NUM_OF_EXP = 4
ph = array([385.0, 315.0, 290.0, 890.0, 890.0, 1180.5, 987.0, 1091.5, 1035.5, 1159.0, 1111.5, 1064.0, 1178.0])
Kaa = array([0.49833,0.49833,0.7475,1.66111,3.7375,6.64444,7.40099,8.125,9.96667,12.35537,22.31343,24.91667,27.18182])
dl_fl = array([0.39, 0.68, 0.71, 1.76, 2.5, 3.95, 2.495, 3.852, 3.952, 5.28, 5.28, 5.64267, 6.56])


Ka_model = linspace(0, 30, 30000);
phos_model = Model(phos_function)
phos_model_exp = Model(phos_munk)

phos_model.set_param_hint('Sa', value=0.3, min=0.0001, max=100)


#dlfl_model = Model(delflu_function)

phos_model_data=phos_model.fit(ph, Ka = Kaa)
phos_exp_data = phos_model_exp.fit(ph, Ka = Kaa)

#dlfl_model_data = dlfl_model.fit(dl_fl, Ka = Kaa, I0 = 1, Kph = 1)

Kph_best = phos_model_data.best_values['Kph']
I0_best = phos_model_data.best_values['I0']
Sa_best = phos_model_data.best_values['Sa']
ph_model = []
ph_exp = []
dlfl_munk_data = []

dlfl_model = Model(dlfl_munk)
#dlfl_model.set_param_hint('I0', value=I0_best, min=I0_best-0.001, max=I0_best+0.001)
#dlfl_model.set_param_hint('Sa', value=Sa_best, min=Sa_best-0.001, max=Sa_best+0.001)
dlfl_model_data = dlfl_model.fit(dl_fl, Ka = Kaa)

Kph_best2 = phos_exp_data.best_values['Kph']
I0_best2 = phos_exp_data.best_values['I0']

Kdlfl_best = dlfl_model_data.best_values['Kdlfl']
I0_best_munk = dlfl_model_data.best_values['I0']


for i in range(Ka_model.size):
    ph_model.append(phos_function(Ka_model[i], Kph = Kph_best, I0 = I0_best, Sa = Sa_best))
    ph_exp.append(phos_munk(Ka_model[i], Kph = Kph_best2, I0 = I0_best2))
    dlfl_munk_data.append(dlfl_munk(Ka_model[i], Kdlfl = Kdlfl_best, I0 = I0_best_munk))

a = plt.figure(1)
axe = a.add_subplot(111)
axe.spines['right'].set_visible(False)
axe.spines['top'].set_visible(False)

print(phos_exp_data.fit_report())

plt.plot(Kaa, ph, "ks", label="Экспериментальные данные")
#plt.plot(Ka_model, ph_model, "r--", label="Данные модели", linewidth=2)
plt.plot(Ka_model, ph_exp, "r-", label="Данные модели", linewidth=2)
plt.xlabel("Коэффициент оптического поглощения раствора, Ka, ", fontsize = 'x-large')
plt.ylabel("Интенсивность фосфоресценции, отн. ед.",
          fontsize = 'x-large')
plt.legend()
plt.show()
#

a = plt.figure(2)
axe = a.add_subplot(111)
axe.spines['right'].set_visible(False)
axe.spines['top'].set_visible(False)

plt.plot(Kaa, dl_fl, "ks", label="Экспериментальные данные")
plt.plot(Ka_model, dlfl_munk_data, "r-", label="Данные модели", linewidth=2)

plt.xlabel("Коэффициент оптического поглощения раствора, Ka, ", fontsize = 'x-large')
plt.ylabel("Интенсивность замедленной \n флуоресценции, отн. ед.",
          fontsize = 'x-large')
plt.legend()
plt.show()