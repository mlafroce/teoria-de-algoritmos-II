import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import math

textSize = 4638690 # len texto
sigma = 4 # alfabeto

maxIt = int(math.log(textSize, 3))

# Armo las funciones
it = sp.symbols("it")
f_N = textSize * ((2./3) ** it)
f_N_numpy = sp.lambdify(it, f_N, "numpy")

s = sp.symbols("sigma")
f_sigma = sigma ** (3 * s)
f_sigma_numpy = sp.lambdify(s, f_sigma, "numpy")

its = np.linspace(0, maxIt ) # agrego un poco de espacio
sigmaSup = [f_sigma_numpy(val) for val in its if f_sigma_numpy(val) < f_N_numpy(val) * 4]

# Version normal
plt.subplot(211)
plt.plot(its, f_N_numpy(its), '--', linewidth=2)
plt.plot(its[0: len(sigmaSup)], sigmaSup, '--', linewidth=2)
plt.axvline(x=maxIt, color='r', linestyle='--')


# Vers logaritmica
plt.subplot(212)
plt.semilogy(its, f_N_numpy(its), '--', linewidth=2)
plt.semilogy(its[0: len(sigmaSup)], sigmaSup, '--', linewidth=2)
plt.axvline(x=maxIt, color='r', linestyle='--')

plt.show()

### Empirico con ecoli.dat

sigma_emp = [4, 65, 246554, 1364657, 912772, 609751, 407037, 271489]
values_emp = [4638690, 3092460, 2061640, 1374426, 916284, 610856, 407237, 271491]

plt.plot(sigma_emp, '--', linewidth=2)
plt.plot(values_emp, '--', linewidth=2)
plt.show()

'''

Iteration:  0
Alphabet size:  4
Values size:  4638690

Iteration:  1
Alphabet size:  65
Values size:  3092460

Iteration:  2
Alphabet size:  246554
Values size:  2061640

Iteration:  3
Alphabet size:  1364657
Values size:  1374426

Iteration:  4
Alphabet size:  912772
Values size:  916284

Iteration:  5
Alphabet size:  609751
Values size:  610856

Iteration:  6
Alphabet size:  407037
Values size:  407237

Iteration:  7
Alphabet size:  271489
Values size:  271491
'''