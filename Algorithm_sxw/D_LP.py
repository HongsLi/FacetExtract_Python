# -*- coding:utf-8 -*-
import numpy as np
import json


# 加起来等于1
def norm_by_row(m):
    m_sum = m.sum(axis=1)
    m_sum = m_sum.reshape(m_sum.shape[0], 1)
    m = m / m_sum
    return np.nan_to_num(m)


# 每一个最大值为1
def norm_max(m):
    m_max, m_min = m.max(axis=1), m.min(axis=1)
    m_max, m_min = m_max.reshape(m_max.shape[0], 1), m_min.reshape(m_min.shape[0], 1)

    norm = (m - m_min) / (m_max - m_min)
    return np.nan_to_num(norm)

# normmax可以得到正确的结果
def LP(p, f, loss):
    if p.size == 1:
        p = p.reshape(1, 1)
        f = f.reshape(1, f.shape[0])
    p = norm_by_row(p)
    f0 = f
    [x, y] = np.where(f > 0)
    f_prev = np.zeros(f.shape)
    print('LP start:')
    i = 1
    while (np.max(f - f_prev) > loss):
        print('iterating times: ', i)
        i += 1
        f_prev = f
        f = p.dot(f)
        # 替换
        for x_i in range(len(x)):
            f[x[x_i], y[x_i]] = f0[x[x_i], y[x_i]]

        # 按行归一化
        f = norm_by_row(f)
    return f

def get_part_dict(domain):
    with open('../output/' + domain + '/Algorithm_sxw/B_partition/part_dict.json', 'r', encoding='utf-8') as f:
        part_dict = json.load(f)
    return part_dict

def do_lp(P, F):
    p = P
    f = F
    loss = 0.0001
    result = LP(p, f, loss)
    return result

def D_LP(domain):
    part_dict = get_part_dict(domain)
    part_nums = len(part_dict)
    for k in part_dict.keys():
        print('doing ' + str(k) + 'th cluster')
        P = np.loadtxt('../output/' + domain + '/Algorithm_sxw/B_partition/P' + str(k) + '.txt')
        F = np.loadtxt('../output/' + domain + '/Algorithm_sxw/C_generateF/F' + str(k) + '.txt')
        result = do_lp(P, F)
        np.savetxt('../output/' + domain + '/Algorithm_sxw/D_LP/result' + str(k) + '.txt', result)


D_LP('Physical_chemistry')
