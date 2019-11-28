# -*- coding:utf-8 -*-
import numpy as np


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


def do_lp(domain):
    p = np.loadtxt('../output/' + domain + '/Algorithm/A_generateP/P.txt')
    f = np.loadtxt('../output/' + domain + '/Algorithm/B_generateF/F.txt')
    loss = 0.0001
    result = LP(p, f, loss)
    np.savetxt('../output/' + domain + '/Algorithm/C_LP/result' + str(loss) + '.txt', result)
    print('done')

do_lp('Physical_chemistry')
#
# p = np.array([[1, 0.4, 0.8], [0.4, 1, 0.4], [0.8, 0.4, 1]])
# f = np.array([[1, 0, 0], [0, 0, 1], [0, 0, 0]])
# print(p)
# print(f)
# print(LP(p, f, 0.01))