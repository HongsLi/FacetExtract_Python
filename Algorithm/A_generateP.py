# -*- coding:utf-8 -*-
import numpy as np
import utils.consts as consts
import utils.Utils as Utils
import collections


def generate_p(domain):
    topic_dict, topic_index_dict = Utils.get_topic_dict(domain)
    topic_nums = len(topic_dict)
    p = np.eye(topic_nums)

    for i in range(topic_nums):
        print('doing: ', int(i/topic_nums) * 100, 'percent.')
        for j in range(i + 1, topic_nums):
            sim = get_similarity_of_2_topics(domain, topic_index_dict[i], topic_index_dict[j])
            p[i, j] = sim
            p[j, i] = sim
    np.savetxt('../output/' + domain + '/Algorithm/A_generateP/P.txt', p)


def get_similarity_of_2_topics(domain, topic1, topic2):
    word_matrix1 = np.loadtxt('../output/' + domain + '/Preprocess/F_process_summary/' + topic1 + '.txt')
    word_matrix2 = np.loadtxt('../output/' + domain + '/Preprocess/F_process_summary/' + topic2 + '.txt')

    sim = 0
    word_nums = 0
    for word1 in word_matrix1:
        sim += np.max(cal_cos(word1, word_matrix2, type='wm'))
        word_nums += 1

    for word2 in word_matrix2:
        sim += np.max(cal_cos(word2, word_matrix1, type='wm'))
        word_nums += 1

    return sim / word_nums


def cal_cos(v1, v2, type='ww'):
    # word and word
    if (type == 'ww'):
        return np.sum(v1 * v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    # word and matrix
    if (type == 'wm'):
        fenzi = v1.dot(v2.T).reshape(len(v2), 1)
        fenmu = np.linalg.norm(v1) * np.sqrt((v2 * v2).sum(axis=1))
        return fenzi / fenmu.reshape(len(v2), 1)


# print(get_similarity_of_2_topics('Data_structure', 'Hash_table', 'Hash_table'))
generate_p('Data_mining')
