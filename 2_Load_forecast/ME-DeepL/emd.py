import numpy as np
import pandas as pd
import pylab as plt

import os

#a = os.getcwd()


from PyEMD import EMD

# data loading

df_x = pd.read_excel('Treated_TMP_data_MemD.xlsx', header=None)
df_x.shape

array_x = df_x.to_numpy()

array_x.shape, type(array_x)

new_array_x = array_x.flatten()
new_array_x.shape

t = np.arange(1, 1197, 1)
t.shape

emd = EMD()
IMFs_TMP = emd.emd(new_array_x, t)

IMFs_TMP.shape

N = IMFs_TMP.shape[0]
N

# Plot results
plt.figure(figsize=(12, 10))
plt.subplot(N + 1, 1, 1)
plt.plot(t, new_array_x, 'r')
plt.ylabel("TMP", fontsize=16, weight='bold', fontname='Times new roman')
plt.yticks(fontsize=13, fontname='Times new roman')
plt.xticks(fontsize=13, fontname='Times new roman')

for n in range(N):
    plt.subplot(N + 1, 1, n + 2)
    plt.plot(t, IMFs_TMP[n], 'g')
    plt.ylabel("IMF %i" % (n + 1), fontsize=16, weight='bold', fontname='Times new roman')
    plt.yticks(fontsize=13, fontname='Times new roman')
    plt.xticks(fontsize=13, fontname='Times new roman')
    plt.locator_params(axis='y', nbins=5)

plt.xlabel("Time [s]", fontsize=16, weight='bold', fontname='Times new roman')
plt.tight_layout()
# plt.savefig('EMD TMP MemD', dpi=120)
plt.show()