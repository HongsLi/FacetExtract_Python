# -*- coding: utf-8 -*-
import gensim
from gensim.test.utils import datapath, get_tmpfile
from gensim.scripts.glove2word2vec import glove2word2vec
import re
import os
import numpy as np
from functools import reduce

"""
    师姐的分面树生成代码的一部分，java版本的跑不通，用python重写
"""
np.set_printoptions(suppress=True)


class ProcessSummary(object):

    def __init__(self, domain):
        self.path = '../dataset/domain_summaries/'
        self.domain = domain
        self.summary_path = self.path + self.domain + '/'

    def generate_matrix(self):
        model = self.load_model()

        # 读入文件
        for root, dirs, files in os.walk(self.summary_path):
            for fn in files:
                print('---\nfilename: ' + fn)
                # matrix_file = open('../output/' + self.domain + '/Preprocess/F_process_summary/' + fn, 'w', encoding='utf-8')
                with open(root + fn, 'r', encoding='utf-8') as f:
                    string_list = f.readlines()
                    content = self.remove_null_chars(string_list)

                    matrix = np.array([])
                    print('constructing matrix')
                    # 构建矩阵
                    word_nums = 0
                    for word in content.split(' '):
                        if word in model:
                            embedding = model[word]
                            word_nums += 1
                            matrix = np.r_[matrix, embedding]
                        else:
                            continue
                    matrix = matrix.reshape(word_nums, -1)
                    np.savetxt('../output/' + self.domain + '/Preprocess/F_process_summary/' + fn, matrix)
                # matrix_file.close()
                print('done')

    def remove_null_chars(self, str_list):
        s = ''
        for string in str_list:
            s_tmp = string
            s_tmp = re.sub("\\(", "", s_tmp)
            s_tmp = re.sub("\\)", "", s_tmp)
            s_tmp = re.sub(",", "", s_tmp)
            s_tmp = re.sub("\\.", "", s_tmp)
            s_tmp = re.sub(";", "", s_tmp)
            s_tmp = re.sub("\\[\\d+]", "", s_tmp)
            s_tmp = re.sub("-", " ", s_tmp)
            s_tmp = re.sub("\\[", " ", s_tmp)
            s_tmp = re.sub("—", " ", s_tmp)
            s_tmp = re.sub("\\d+", "", s_tmp)
            s_tmp = re.sub(":", "", s_tmp)
            s_tmp = re.sub("\"", "", s_tmp)
            s += s_tmp
        return s

    def load_model(self):
        print('loading...')
        model = gensim.models.KeyedVectors.load_word2vec_format(r'../dataset/word_embedding/word2vec.6B.50d.txt',
                                                                binary=False)
        print('model loaded.')
        return model

    # 将glove转化为word2vec 暂时用不到了
    def transform_glove2word2vec(self):
        glove_file = datapath('F:\\分面生成\\数据集\\词表\\glove.6B.50d.txt')
        output = get_tmpfile("F:\\分面生成\\数据集\\词表\\word2vec.6B.50d.txt")
        glove2word2vec(glove_file, output)


p = ProcessSummary('Physical_chemistry')
p.generate_matrix()
