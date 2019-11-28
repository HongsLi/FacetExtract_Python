# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def get_heat_map(path):
    matrix = np.loadtxt(path)
    plt.pcolor(matrix)
    plt.colorbar()
    plt.grid()
    plt.show()





get_heat_map('../output/Data_structure/Algorithm/B_generateF/F.txt')