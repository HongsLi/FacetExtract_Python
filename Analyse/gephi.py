# -*- coding:utf-8 -*-
import os
import csv
import numpy as np


def norm_max(m):
    m_max, m_min = m.max(axis=1), m.min(axis=1)
    m_max, m_min = m_max.reshape(m_max.shape[0], 1), m_min.reshape(m_min.shape[0], 1)

    norm = (m - m_min) / (m_max - m_min)
    return np.nan_to_num(norm)


def readP(domain):
    p = np.loadtxt('../output/' + domain + '/Algorithm_new/A_generateP/P.txt')
    return norm_max(p)


def generate_unweighted_csv(p, domain):
    p = p > 0.6
    file = open('../output/' + domain + '/Analyse/gephi_unweighted.csv', 'w', newline='')
    fcsv = csv.writer(file)
    headers = ['source', 'target']
    fcsv.writerow(headers)
    size = len(p)
    for i in range(size):
        for j in range(i + 1, size):
            if p[i][j]:
                row = ['node' + str(i), 'node' + str(j)]
                fcsv.writerow(row)
    file.close()



def generate_csv(p, domain):
    file = open('../output/' + domain + '/Analyse/gephi.csv', 'w', newline='')
    fcsv = csv.writer(file)
    headers = ['source', 'target', 'weight']
    fcsv.writerow(headers)
    size = len(p)
    for i in range(size):
        for j in range(i + 1, size):
            row = ['node' + str(i), 'node' + str(j), p[i][j]]
            fcsv.writerow(row)

    file.close()


def generate_gephi(domain):
    p = readP(domain)
    generate_csv(p, domain)

def generate_unweighted_gephi(domain):
    p = readP(domain)
    generate_unweighted_csv(p, domain)


generate_unweighted_gephi('Data_structure_new')
